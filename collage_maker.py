import argparse
import os
import sys

import numpy as np
from PIL import Image


def parse_border(border_args):
    if border_args:
        thickness, color = border_args
        if thickness.endswith("%"):
            # Convert percentage to decimal
            thickness = float(thickness.strip("%")) / 100
        else:
            thickness = float(thickness)
        return thickness, color
    return 0, ""


def create_collage(
    folder_path, output_name="collage.jpg", border_args=None, rows=None, columns=None
):
    border_thickness, border_color = parse_border(border_args)

    extensions = (".png", ".jpg", ".jpeg")
    images = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(extensions)
    ]
    loaded_images = [Image.open(image) for image in images]

    if not loaded_images:
        print("No images found in the directory.")
        return

    median_width = int(np.median([img.size[0] for img in loaded_images]))
    median_height = int(np.median([img.size[1] for img in loaded_images]))

    if isinstance(
        border_thickness, float
    ):  # If border thickness is given as a percentage
        border_thickness = int(max(median_width, median_height) * border_thickness)

    resized_images = [
        img.resize((median_width, median_height), Image.Resampling.LANCZOS)
        for img in loaded_images
    ]

    num_images = len(resized_images)
    if rows and columns:
        if rows * columns < num_images:
            print(
                f"Error: The specified rows ({rows}) and columns ({columns}) cannot accommodate all {num_images} images."
            )
            sys.exit(1)

    if not rows and not columns:
        if median_height <= median_width:
            columns = 3 if num_images >= 9 else 2
        else:
            rows = 3 if num_images >= 9 else 2
    if not rows:
        rows = num_images // columns + (num_images % columns > 0)
    if not columns:
        columns = num_images // rows + (num_images % rows > 0)

    collage_width = median_width * columns + border_thickness * (columns - 1)
    collage_height = median_height * rows + border_thickness * (rows - 1)

    collage = Image.new("RGB", (collage_width, collage_height), border_color)

    x_offset, y_offset = 0, 0
    for img in resized_images:
        collage.paste(img, (x_offset, y_offset))
        x_offset += median_width + border_thickness
        if x_offset >= collage_width:
            x_offset = 0
            y_offset += median_height + border_thickness

    collage.save(os.path.join(folder_path, output_name))
    print("Collage created successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a collage from images in a specified folder."
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="folder_path",
        type=str,
        required=True,
        help="Path to the folder containing images.",
    )
    parser.add_argument(
        "-o",
        "--output_name",
        type=str,
        default="collage.jpg",
        help="Name of the output collage image file. Default is 'collage.jpg'.",
    )
    parser.add_argument(
        "-b",
        "--border",
        nargs=2,
        metavar=("THICKNESS", "COLOR"),
        help="Add a border between images with specified thickness (in pixels or percentage, e.g., '5' or '2%%') and color (e.g., 'black', '#FFF').",
    )
    parser.add_argument(
        "-r", "--rows", type=int, help="Custom number of rows for the collage."
    )
    parser.add_argument(
        "-c", "--columns", type=int, help="Custom number of columns for the collage."
    )

    args = parser.parse_args()

    if not args.output_name.lower().endswith(".jpg"):
        args.output_name += ".jpg"

    create_collage(args.folder_path, args.output_name, args.border, args.rows, args.columns)

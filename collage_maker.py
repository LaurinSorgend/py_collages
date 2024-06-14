import argparse
import os
import sys

import logging

import numpy as np
from PIL import Image
from PIL import ImageDraw, ImageFont


def create_collage(
    folder_path,
    output_name="collage.jpg",
    border_args=None,
    rows=None,
    columns=None,
    number_images=False,
    number_font_size=30,
    number_color="white",
    overwrite_img_width=0,
    overwrite_img_heigth=0,
):
    extensions = (".png", ".jpg", ".jpeg")
    images = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(extensions)
    ]
    loaded_images = [Image.open(image) for image in images]
    if not loaded_images:
        logging.error("No images found. stopping.")
        sys.exit(1)
    logging.info(f"Making Collage with {len(loaded_images)} Images")
    print (overwrite_img_heigth, overwrite_img_width)
    if overwrite_img_width == 0:
        median_width = int(np.median([img.size[0] for img in loaded_images]))
    else:
        median_width = overwrite_img_width
    if overwrite_img_heigth == 0:
        median_height = int(np.median([img.size[1] for img in loaded_images]))
    else:
        median_height = overwrite_img_heigth

    border_thickness = 0
    border_color = "white"

    if border_args:
        border_thickness = int(border_args[0])
        border_color = border_args[1]
    resized_images = [
        img.resize((median_width, median_height), Image.Resampling.LANCZOS)
        for img in loaded_images
    ]
    logging.info(f"{border_thickness=}, {border_color=}")
    num_images = len(resized_images)
    if rows and columns:
        if rows * columns < num_images:
            logging.error(
                f"Error: The specified rows ({rows}) and columns ({columns}) cannot accommodate all {num_images} images. stopping."
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
    logging.info(f"{columns=}, {rows=}")
    collage_width = median_width * columns + border_thickness * (columns - 1)
    collage_height = median_height * rows + border_thickness * (rows - 1)
    logging.info(f"{collage_width=}, {collage_height=}")
    collage = Image.new("RGB", (collage_width, collage_height), border_color)

    x_offset, y_offset = 0, 0
    for img in resized_images:
        if number_images:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", number_font_size)
            number_str = str(resized_images.index(img) + 1)
            textbox = draw.textbbox(xy=(0, 0), text=number_str, font=font)
            text_width = textbox[2] - textbox[0]
            text_height = textbox[3] - textbox[1]
            position = (
                median_width - text_width - (median_width / 50),
                median_height - text_height - (median_height / 30),
            )
            draw.text(position, number_str, fill=number_color, font=font)
        collage.paste(img, (x_offset, y_offset))
        x_offset += median_width + border_thickness
        if x_offset >= collage_width:
            x_offset = 0
            y_offset += median_height + border_thickness

    collage.save(os.path.join(folder_path, output_name))
    logging.info("Collage created succesfully. exiting.")
    sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started Main Function")
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
        help="Add a border between images with specified thickness (in pixels) and color (e.g., 'black', '#FFF').",
    )
    parser.add_argument(
        "-r", "--rows", type=int, help="Custom number of rows for the collage."
    )
    parser.add_argument(
        "-c", "--columns", type=int, help="Custom number of columns for the collage."
    )
    parser.add_argument(
        "-n",
        "--number",
        action="store_true",
        help="Enable numbering of images in the collage.",
    )
    parser.add_argument(
        "-fs",
        "--number_font_size",
        type=int,
        default=30,
        help="Font size for numbering images. Default is 30.",
    )
    parser.add_argument(
        "-nc",
        "--number_color",
        type=str,
        default="white",
        help="Color of the numbers. Default is 'white'.",
    )
    parser.add_argument(
        "-oiw",
        "--overwrite_img_width",
        type=int,
        help="overwrite_img_width",
    )
    parser.add_argument(
        "-oih",
        "--overwrite_img_heigth",
        type=int,
        help="overwrite_img_heigth",
    )
    args = parser.parse_args()

    if not args.output_name.lower().endswith(".jpg"):
        args.output_name += ".jpg"
    logging.info("Parsed args")
    create_collage(
        args.folder_path,
        args.output_name,
        args.border,
        args.rows,
        args.columns,
        args.number,
        args.number_font_size,
        args.number_color,
        args.overwrite_img_width,
        args.overwrite_img_heigth,
    )

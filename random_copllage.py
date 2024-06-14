from collage_maker import get_images, create_collage
import argparse
import random
import os
import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser("hehe")
    parser.add_argument(
        "-i",
        "--input",
        dest="folder_path",
        type=str,
        required=True,
        help="Path to the folder containing images.",
    )
    path = parser.parse_args().folder_path
    images = get_images(path)
    if len(images) > 9:
        images = random.choices(images, k=9)
        dir_path = os.path.join(path, "collages")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        output_name = os.path.join(
            dir_path, (datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg")
        )
        collage = create_collage(
            images, output_name, ("10", "pink"), 3, 3, True, 30, "black", 300, 300
        )
        collage.save(output_name)
    else:
        print("ERROR: Not enugh images in folder")

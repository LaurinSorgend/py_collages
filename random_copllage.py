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
    str_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    images = get_images(path)
    if len(images) > 9:
        # images = random.choices(images, k=9)
        # random.shuffle(images)
        # images = images[:9]
        dir_path = os.path.join(path, "collages")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        counter = 0
        while len(images) >= 9:
            collage_images = list()
            while len(collage_images) < 9:
                collage_images.append(images.pop(0))
                print(len(collage_images))

            output_name = os.path.join(dir_path, (str_time + f"_{counter}.jpg"))
            collage = create_collage(
                collage_images,
                output_name,
                ("10", "pink"),
                3,
                3,
                True,
                30,
                "black",
                300,
                300,
            )
            collage.save(output_name)
            counter += 1
    else:
        print("ERROR: Not enugh images in folder")

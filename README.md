# Image Collage Creator

This Python script generates a collage from PNG and JPG images in a specified folder, scaling them to the median size. It allows for customization of the collage layout and the addition of borders between images.

## Requirements
- Python 3.x (I use 3.12)
- Pillow
- numpy

## Installation

Clone the repo. Install the requirements using pip (or conda).

## Usage


### Arguments
```
usage: collage_maker.py [-h] -i FOLDER_PATH [-o OUTPUT_NAME] [-b THICKNESS COLOR] [-r ROWS] [-c COLUMNS] [-n] [-fs NUMBER_FONT_SIZE] [-nc NUMBER_COLOR] [-oiw OVERWRITE_IMG_WIDTH] [-oih OVERWRITE_IMG_HEIGTH]

Create a collage from images in a specified folder.

options:
  -h, --help            show this help message and exit
  -i FOLDER_PATH, --input FOLDER_PATH
                        Path to the folder containing images.
  -o OUTPUT_NAME, --output_name OUTPUT_NAME
                        Name of the output collage image file. Default is 'collage.jpg'.
  -b THICKNESS COLOR, --border THICKNESS COLOR
                        Add a border between images with specified thickness (in pixels) and color (e.g., 'black', '#FFF').
  -r ROWS, --rows ROWS  Custom number of rows for the collage.
  -c COLUMNS, --columns COLUMNS
                        Custom number of columns for the collage.
  -n, --number          Enable numbering of images in the collage.
  -fs NUMBER_FONT_SIZE, --number_font_size NUMBER_FONT_SIZE
                        Font size for numbering images. Default is 30.
  -nc NUMBER_COLOR, --number_color NUMBER_COLOR
                        Color of the numbers. Default is 'white'.
  -oiw OVERWRITE_IMG_WIDTH, --overwrite_img_width OVERWRITE_IMG_WIDTH
                        overwrite_img_width
  -oih OVERWRITE_IMG_HEIGTH, --overwrite_img_heigth OVERWRITE_IMG_HEIGTH
                        overwrite_img_heigth
```
## Examples

Creating a collage with default settings:

`collage_maker.py -i /path/to/images`

Creating a collage with a custom output filename:

`collage_maker.py -i /path/to/images -o my_custom_collage.jpg`

Adding a 5px black border between images:

`collage_maker.py -i /path/to/images -b 5 black`

Specifying a custom layout with 2 rows:

`collage_maker.py -i /path/to/images -r 2`

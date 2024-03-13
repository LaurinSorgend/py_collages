# Image Collage Creator

This Python script generates a collage from PNG and JPG images in a specified folder, scaling them to the median size. It allows for customization of the collage layout and the addition of borders between images.

## Requirements
- Python 3.x
- Pillow
- numpy

## Installation

Clone the repo. Install the Requierments using pip

## Usage

bash collage_maker.py [-h] -i FOLDER_PATH [-o OUTPUT_NAME] [-b THICKNESS COLOR] [-r ROWS] [-c COLUMNS]

### Arguments

- `-h, --help`  
  Show the help message and exit.

- `-i FOLDER_PATH, --input FOLDER_PATH`  
  **Required.** Path to the folder containing images.

- `-o OUTPUT_NAME, --output_name OUTPUT_NAME`  
  Name of the output collage image file. Default is 'collage.jpg'.

- `-b THICKNESS COLOR, --border THICKNESS COLOR`  
  Optional. Add a border between images with specified thickness (in pixels or percentage, e.g., '5' or '2%%') and color (e.g., 'black', '#FFF').

- `-r ROWS, --rows ROWS`  
  Optional. Custom number of rows for the collage.

- `-c COLUMNS, --columns COLUMNS`  
  Optional. Custom number of columns for the collage.

## Examples

Creating a collage with default settings:

collage_maker.py -i /path/to/images

Creating a collage with a custom output filename:

collage_maker.py -i /path/to/images -o my_custom_collage.jpg

Adding a 5px black border between images:

collage_maker.py -i /path/to/images -b 5 black

Specifying a custom layout with 2 rows:

collage_maker.py -i /path/to/images -r 2
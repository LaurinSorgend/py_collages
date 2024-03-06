import os
import sys
from PIL import Image
import numpy as np 

def create_collage(folder_path, output_name="collage.jpg"):
    # Supported image extensions
    extensions = ('.png', '.jpg', '.jpeg')
    
    # Find all images in the folder
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(extensions)]
    
    # Load images
    loaded_images = [Image.open(image) for image in images]
    
    if not loaded_images:
        print("No images found in the directory.")
        return

    # Calculate median width and height
    widths = np.median([img.size[0] for img in loaded_images])
    heights = np.median([img.size[1] for img in loaded_images])
    median_width, median_height = int(widths), int(heights)

    # Resize images to the median size
    resized_images = [img.resize((median_width, median_height), Image.Resampling.LANCZOS) for img in loaded_images]
    num_images = len(resized_images)
    # Determine collage size    
    if median_height <= median_width:
        columns = 3 if num_images >= 9 else 2
        rows = num_images // columns + (num_images % columns > 0)
    else:
        rows = 3 if num_images >= 9 else 2
        columns = num_images // rows + (num_images % rows > 0)


    collage_width = median_width * columns
    collage_height = median_height * rows

    # Create a blank collage image
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    # Paste images into collage
    x_offset, y_offset = 0, 0
    for img in resized_images:
        collage.paste(img, (x_offset, y_offset))
        x_offset += median_width
        if x_offset >= collage_width:
            x_offset = 0
            y_offset += median_height

    # Save the collage
    collage.save(os.path.join(folder_path, output_name))
    print("Collage created successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python collage_maker.py <folder_path> [output_name]")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_name = sys.argv[2]
        if not output_name.lower().endswith('.jpg'):
            output_name += '.jpg'
        create_collage(folder_path, output_name)
    else: create_collage(folder_path)
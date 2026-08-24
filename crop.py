from PIL import Image
import sys

def crop_transparent(image_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img_cropped = img.crop(bbox)
        img_cropped.save(image_path)
        print(f"Cropped {image_path} to {bbox}")
    else:
        print(f"Could not crop {image_path}")

crop_transparent("/Users/app/Desktop/mintlify/docs/logo/dark.png")
crop_transparent("/Users/app/Desktop/mintlify/docs/logo/light.png")
crop_transparent("/Users/app/Desktop/mintlify/docs/favicon.png")

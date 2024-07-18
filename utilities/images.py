from PIL import Image

def crop_center_square(image):
    # Get the width and height of the image
    width, height = image.size

    # Determine the size of the square crop
    crop_size = min(width, height)

    # Calculate the top-left corner of the crop box
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2

    # Crop the image
    cropped_image = image.crop((left, top, left + crop_size, top + crop_size))

    return cropped_image
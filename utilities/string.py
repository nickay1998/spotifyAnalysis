from PIL import Image, ImageDraw, ImageFont

def trim_text(text, max_width):
    # Load the font using the font name
    font = ImageFont.truetype("Arial", 14)

    image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(image)

    # Get the width of the string
    text_width = draw.textlength(text, font)

    if text_width > max_width:
        return text[:int(max_width / text_width * len(text))] + "..."
    else:
        return text
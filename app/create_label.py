from PIL import Image, ImageDraw, ImageFont

from app.file_utils import create_folder

def create_image(text1, text2, name=None, output_path='output/'):
    # Set image properties
    width = 40  # Width in centimeters
    height = 14  # Height in centimeters
    ppm = 110  # Pixels per millimeter
    img_width = int(width * ppm)
    img_height = int(height * ppm)

    # Create a blank image
    image = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1"

    # Set font properties
    font_size1 = 4
    font_size2 = 7
    font1 = ImageFont.truetype("fonts/roboto/Roboto-Medium.ttf", round(font_size1*ppm))  # You can change the font and size
    font2 = ImageFont.truetype("fonts/roboto/Roboto-Medium.ttf", round(font_size2*ppm))  # You can change the font and size

    text2_width, text2_height = draw.textsize(text2, font=font2)
    text2_x = img_width - text2_width
    text2_y = font_size1*ppm + 0*ppm  # Position the second text right below the first text

    # Draw the texts on the image
    draw.text((0, 0), text1, font=font1, fill="black")
    draw.text((0, text2_y), text2, font=font2, fill="black", align="center")

    # Resize the image to the desired dimensions
    # image = image.resize((int(width * 10), int(height * 10)))  # Multiply by 10 to convert from cm to mm

    # Save the image as PNG
    create_folder(output_path)
    image.save(f"{output_path}/{name or text1}.png", dpi=(ppm, ppm))


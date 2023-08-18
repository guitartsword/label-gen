import logging.config
import logging
from PIL import Image, ImageDraw, ImageFont

from app.file_utils import create_folder
from app.logging_config import LOGGING_CONFIG


logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING_CONFIG)


def create_image(text1, text2, name=None, output_path='output/'):
    # Set image properties
    width = 40  # Width in centimeters
    height = 14  # Height in centimeters
    ppm = 110  # Pixels per millimeter
    img_width = int(width * ppm)
    img_height = int(height * ppm)

    # Create a blank image with desired properties
    image = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(image)
    draw.fontmode = '1'

    # Set font properties
    font_size1 = 4  # This is the relative size
    font_size2 = 7  # This is the relative size
    font1 = ImageFont.truetype('fonts/roboto/Roboto-Medium.ttf', round(font_size1*ppm))  # You can change the font and size
    font2 = ImageFont.truetype('fonts/roboto/Roboto-Medium.ttf', round(font_size2*ppm))  # You can change the font and size

    text2_y = font_size1*ppm  # Position the second text right below the first text

    # Draw the texts on the image
    draw.text((0, 0), text1, font=font1, fill='black')  # Text 1
    draw.text((0, text2_y), text2, font=font2, fill='black', align='center')  # Text 2

    # Save the image as PNG
    create_folder(output_path)
    output_file = f'{output_path}{name or text1}.png'
    image.save(output_file, dpi=(ppm, ppm))
    logger.info(f'done >>> {output_file}')


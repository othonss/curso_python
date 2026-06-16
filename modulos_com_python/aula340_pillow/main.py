from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'totoro2.png'
NEW_IMAGE = ROOT_FOLDER / 'newtotoro.png'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size
#exif = pil_image.info['exif']

new_width = 440
new_height = round(height * new_width / width)
# print(width, height)
# print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
)

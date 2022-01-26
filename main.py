from pathlib import Path

import detection

# creating list of image paths in given directory
images = Path('images').rglob('*.png')

for path in images:
    detection.detect_people(path)

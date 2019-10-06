from PIL import Image
from matplotlib import pyplot as plt


PATH_TO_FILE = "./Test Inputs/1.jpg"


im = Image.open(open(PATH_TO_FILE, 'rb'))
plt.imshow(im)
points = plt.ginput(3, show_clicks=True)
print("clicked", points)

from PIL import Image
from matplotlib import pyplot as plt
import sys
import numpy as np

RUN_MODE = -1
PATH_TO_FILE = ""
K = -1
IMAGE = []
IMAGE_3D_MATRIX = []


def kmeans_main(cluster_points):
    #TODO
    return


def kmeans_with_click():
    im = Image.open(open(PATH_TO_FILE, 'rb'))
    plt.imshow(im)
    points = plt.ginput(K, show_clicks=True)
    kmeans_main(points)


def kmeans_with_random():
    points = []
    for i in range(K):
        x = np.random.uniform(0, IMAGE_3D_MATRIX.shape[1])
        y = np.random.uniform(0, IMAGE_3D_MATRIX.shape[1])
        points.append((x, y))

    kmeans_main(points)


def read_image():
    global IMAGE, IMAGE_3D_MATRIX
    IMAGE = Image.open(open(PATH_TO_FILE, 'rb'))
    IMAGE_3D_MATRIX = np.array(IMAGE)


def handle_arguments():
    global PATH_TO_FILE, K, RUN_MODE
    PATH_TO_FILE, K, RUN_MODE = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    if K < 1:
        sys.exit("K should be greater than 1, your K value is {}".format(K))

    if RUN_MODE not in {0, 1}:
        sys.exit("Program mode should be either 0 or 1, your value is {}".format(RUN_MODE))


if __name__ == "__main__":
    handle_arguments()
    read_image()

    if RUN_MODE:
        kmeans_with_random()
    else:
        kmeans_with_click()

    sys.exit("Success: Output file generated!")

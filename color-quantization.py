__author__ = "Alican Safak Ozdek - 2016400069"
__email__ = "safakozdek@gmail.com"
__status__ = "Running"

from PIL import Image
from matplotlib import pyplot as plt
import sys
import numpy as np
import math

RUN_MODE = -1
PATH_TO_FILE = ""
K = -1
IMAGE = []
IMAGE_3D_MATRIX = []


def kmeans_main(cluster_points):
    # rounding pixel values and getting cluster RGB
    centers = []
    for i in range(len(cluster_points)):
        cluster_points[i] = (int(math.floor(cluster_points[i][0])), int(math.floor(cluster_points[i][1])))
        red = IMAGE_3D_MATRIX[cluster_points[i][0]][cluster_points[i][1]][0]
        green = IMAGE_3D_MATRIX[cluster_points[i][0]][cluster_points[i][1]][1]
        blue = IMAGE_3D_MATRIX[cluster_points[i][0]][cluster_points[i][1]][2]
        centers.append([red, blue, green])

    centers = np.array(centers)

    # Initializing class and distance arrays
    classes = np.zeros([IMAGE_3D_MATRIX.shape[0], IMAGE_3D_MATRIX.shape[1]], dtype=np.float64)
    distances = np.zeros([IMAGE_3D_MATRIX.shape[0], IMAGE_3D_MATRIX.shape[1], K], dtype=np.float64)

    for i in range(10):
        # finding distances for each center
        for j in range(K):
            distances[:, :, j] = np.sqrt(((IMAGE_3D_MATRIX - centers[j]) ** 2).sum(axis=2))

        # choosing the minimum distance class for each pixel
        classes = np.argmin(distances, axis=2)

        # rearranging centers
        for c in range(K):
            centers[c] = np.mean(IMAGE_3D_MATRIX[classes == c], 0)

    # changing values with respect to class centers
    for i in range(IMAGE_3D_MATRIX.shape[0]):
        for j in range(IMAGE_3D_MATRIX.shape[1]):
            IMAGE_3D_MATRIX[i][j] = centers[classes[i][j]]


def kmeans_with_click():
    global PATH_TO_FILE
    im = Image.open(open(PATH_TO_FILE, 'rb'))
    plt.imshow(im)
    points = plt.ginput(K, show_clicks=True)
    points = [t[::-1] for t in points]  # reversing tuples
    kmeans_main(points)


def kmeans_with_random():
    global IMAGE_3D_MATRIX
    points = []
    for i in range(K):
        x = np.random.uniform(0, IMAGE_3D_MATRIX.shape[0])
        y = np.random.uniform(0, IMAGE_3D_MATRIX.shape[1])
        points.append((x, y))

    kmeans_main(points)


def read_image():
    global IMAGE, IMAGE_3D_MATRIX
    IMAGE = Image.open(open(PATH_TO_FILE, 'rb'))
    IMAGE_3D_MATRIX = np.array(IMAGE).astype(int)
    print IMAGE_3D_MATRIX


def handle_arguments():
    global PATH_TO_FILE, K, RUN_MODE
    PATH_TO_FILE, K, RUN_MODE = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    if K < 1:
        sys.exit("K should be greater than 1, your K value is {}".format(K))

    if RUN_MODE not in {0, 1}:
        sys.exit("Program mode should be either 0 or 1, your value is {}".format(RUN_MODE))


def save_image():
    global IMAGE_3D_MATRIX
    im = Image.fromarray(IMAGE_3D_MATRIX.astype('uint8'))
    im.save('output.png')


if __name__ == "__main__":
    handle_arguments()
    read_image()

    if RUN_MODE:
        kmeans_with_random()
    else:
        kmeans_with_click()

    save_image()

    sys.exit("Success: Output file generated!")

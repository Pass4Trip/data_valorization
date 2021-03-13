from IPython.display import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_img(location_file, set_size_inches = [19,9]):
    img=mpimg.imread(location_file)
    imgplot=plt.imshow(img)
    plt.gcf().set_size_inches(set_size_inches[0], set_size_inches[1])
    plt.axis('off')
    plt.show()
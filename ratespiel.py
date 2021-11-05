import numpy as np

from prozess import function


def main(grenze_ober, grenze_unter):
    rand_number = np.random.randint(grenze_unter, grenze_ober)
    return function(grenze_ober, grenze_unter, rand_number)

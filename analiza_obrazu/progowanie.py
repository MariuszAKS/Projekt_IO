import skimage.io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

#klasa do generacji maski uzywajac OTSU
#konwertuje obraz do grayscale, znajduje threshold(float) i generuje maske
class ProgowanieOTSU:
    def __init__(self) -> None:
        pass

    #zwraca maske w postaci numpy array
    #image=scierzka do pliku/numpy array
    def maska(self,image):
        if type(image) == str:
            grayscale=rgb2gray(skimage.io.imread(fname=image))
        else:
            grayscale=rgb2gray(image)

        thresh=threshold_otsu(grayscale)
        result=grayscale <= thresh
        return result

    #generuje maske i zapisuje do png (true=255,false=0)
    #image=scierzka do pliku/numpy array
    #path=scierzka do zapisu
    def zapisz_maske(self,image,path="no_name_mask.png"):
        if type(image) == str:
            grayscale=rgb2gray(skimage.io.imread(fname=image))
        else:
            grayscale=rgb2gray(image)

        thresh=threshold_otsu(grayscale)
        result=grayscale <= thresh
        skimage.io.imsave(path,img_as_ubyte(result))
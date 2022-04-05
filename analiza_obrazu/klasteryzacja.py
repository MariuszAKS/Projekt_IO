import numpy as np
import skimage.io
from skimage.color import rgb2lab
from sklearn.cluster import KMeans
from skimage.util import img_as_ubyte

#klasa do wyliczenie centroidow klastrow pikseli (a*,b*)
#obraz jako argument do konstruktora, zmien_obraz aby zmienic obraz
#image=scierzka do pliku/numpy array
class KlastryKSrednich:
    def __init__(self,image) -> None:
        if type(image) == str:
            self.img=rgb2lab(skimage.io.imread(image),"D65","2")
        else:
            self.img=rgb2lab(image,"D65","2")
        self.__obl_klastry()

    def zmien_obraz(self,image):
        if type(image) == str:
            self.img=rgb2lab(skimage.io.imread(image),"D65","2")
        else:
            self.img=rgb2lab(image,"D65","2")
        self.__obl_klastry()

    #trenuje modele k-means
    #wywolywane w konstruktorze/zmien_obraz
    def __obl_klastry(self):
        a=np.array([[x] for x in self.img[:,:,1].flatten()])
        b=np.array([[x] for x in self.img[:,:,2].flatten()])
        self.k_means_a=KMeans(n_clusters=3).fit(a)
        self.k_means_b=KMeans(n_clusters=3).fit(b)
    
    #zwraca centroid kazdego klastara ([[a*1],[a*2],[a*3]],[[b*1],[b*2],[b*3]])
    def centroidy(self):
        return (self.k_means_a.cluster_centers_,self.k_means_b.cluster_centers_)

    #zapisuje wizualizacje klastrów
    #path = scierzka do pliku
    def zapisz_klaster_obraz_A(self,path):
        kl=self.k_means_a.labels_
        kl=np.reshape(kl,(self.img.shape[0],self.img.shape[1]))*127
        skimage.io.imsave(path,img_as_ubyte(kl),check_contrast=False)

    #zapisuje wizualizacje klastrów
    #path = scierzka do pliku
    def zapisz_klaster_obraz_B(self,path):
        kl=self.k_means_b.labels_
        kl=np.reshape(kl,(self.img.shape[0],self.img.shape[1]))*127
        skimage.io.imsave(path,img_as_ubyte(kl),check_contrast=False)
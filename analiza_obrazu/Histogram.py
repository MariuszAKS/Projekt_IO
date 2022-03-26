import math
import numpy as np
import skimage.io
import skimage.color
from skimage.measure.entropy import shannon_entropy

#klasa do generacji cech histogramow
#obraz i maska jako argumenty do konstruktora, zmien_obraz aby zmienic obraz/maske
#image=scierzka do pliku/numpy array
#mask=maska (numpy bool array from Thresholding)
class CechyHistogram:
    def __init__(self,image,mask) -> None:
        if type(image) == str:
            self.img=skimage.io.imread(image)
        else:
            self.img=image
        self.mask=mask
        self.__obl_hist()

    def zmien_obraz(self,image,mask):
        if type(image) == str:
            self.img=skimage.io.imread(image)
        else:
            self.img=image
        self.mask=mask
        self.__obl_hist()

    #wylicza histogramy, wywolywane w konstruktorze/zmien_obraz
    def __obl_hist(self):
        red=self.img[:,:,0]
        green=self.img[:,:,1]
        blue=self.img[:,:,2]
        self.hist_red,bin_edges_red=np.histogram(red[self.mask],bins=256,range=(0,256))
        self.hist_green,bin_edges_green=np.histogram(green[self.mask],bins=256,range=(0,256))
        self.hist_blue,bin_edges_blue=np.histogram(blue[self.mask],bins=256,range=(0,256))
        self.mids_red=bin_edges_red[:-1]
        self.mids_green=bin_edges_green[:-1]
        self.mids_blue=bin_edges_blue[:-1]

        hsv_img=skimage.color.rgb2hsv(self.img)
        hue=hsv_img[:,:,0]
        sat=hsv_img[:,:,1]
        val=hsv_img[:,:,2]
        self.hist_h,bin_edges_h=np.histogram(hue[self.mask],bins=100,range=(0,1))
        self.hist_s,bin_edges_s=np.histogram(sat[self.mask],bins=100,range=(0,1))
        self.hist_v,bin_edges_v=np.histogram(val[self.mask],bins=100,range=(0,1))
        self.mids_h=bin_edges_h[:-1]
        self.mids_s=0.5*(bin_edges_s[1:] + bin_edges_s[:-1])
        self.mids_v=0.5*(bin_edges_v[1:] + bin_edges_v[:-1])

        lab_img=skimage.color.rgb2lab(self.img,"D65","2")
        l=lab_img[:,:,0]
        a=lab_img[:,:,1]
        b=lab_img[:,:,2]
        self.hist_l,bin_edges_l=np.histogram(l[self.mask],bins=100,range=(0,100))
        self.hist_a,bin_edges_a=np.histogram(a[self.mask],bins=256,range=(-128,128))
        self.hist_b,bin_edges_b=np.histogram(b[self.mask],bins=256,range=(-128,128))
        self.mids_l=0.5*(bin_edges_l[1:] + bin_edges_l[:-1])
        self.mids_a=0.5*(bin_edges_a[1:] + bin_edges_a[:-1])
        self.mids_b=0.5*(bin_edges_b[1:] + bin_edges_b[:-1])

    #zwraca srednia histogramow na kazdym kanale [R,G,B]
    def hist_srednia_RGB(self):
        result=[]
        result.append(np.average(self.mids_red,weights=self.hist_red))
        result.append(np.average(self.mids_green,weights=self.hist_green))
        result.append(np.average(self.mids_blue,weights=self.hist_blue))
        return result

    #zwraca srednia histogramow na kazdym kanale [H,S,V]
    def hist_srednia_HSV(self):
        result=[]
        result.append(np.average(self.mids_h,weights=self.hist_h))
        result.append(np.average(self.mids_s,weights=self.hist_s))
        result.append(np.average(self.mids_v,weights=self.hist_v))
        return result

    #zwraca srednia histogramow na kazdym kanale [L,a*,b*]
    def hist_srednia_LAB(self):
        result=[]
        result.append(np.average(self.mids_l,weights=self.hist_l))
        result.append(np.average(self.mids_a,weights=self.hist_a))
        result.append(np.average(self.mids_b,weights=self.hist_b))
        return result

    #zwraca wariancje histogramow na kazdym kanale [R,G,B]
    def hist_var_RGB(self):
        result=[]
        means=self.hist_srednia_RGB()
        result.append(np.average((self.mids_red - means[0])**2, weights=self.hist_red))
        result.append(np.average((self.mids_green - means[1])**2, weights=self.hist_green))
        result.append(np.average((self.mids_blue - means[2])**2, weights=self.hist_blue))
        return result

    #zwraca wariancje histogramow na kazdym kanale [H,S,V]
    def hist_var_HSV(self):
        result=[]
        means=self.hist_srednia_HSV()
        result.append(np.average((self.mids_h - means[0])**2, weights=self.hist_h))
        result.append(np.average((self.mids_s - means[1])**2, weights=self.hist_s))
        result.append(np.average((self.mids_v - means[2])**2, weights=self.hist_v))
        return result

    #zwraca wariancje histogramow na kazdym kanale [L,a*,b*]
    def hist_var_LAB(self):
        result=[]
        means=self.hist_srednia_LAB()
        result.append(np.average((self.mids_l - means[0])**2, weights=self.hist_l))
        result.append(np.average((self.mids_a - means[1])**2, weights=self.hist_a))
        result.append(np.average((self.mids_b - means[2])**2, weights=self.hist_b))
        return result

    #zwraca skosnosc histogramu na kazdym kanale [R,G,B]
    def hist_skos_RGB(self):
        result=[]
        means=self.hist_srednia_RGB()
        result.append((np.sum((self.hist_red-means[0])**3)/self.hist_red.size)/math.sqrt((np.sum((self.hist_red-means[0])**2)/self.hist_red.size)**3))
        result.append((np.sum((self.hist_green-means[1])**3)/self.hist_green.size)/math.sqrt((np.sum((self.hist_green-means[1])**2)/self.hist_green.size)**3))
        result.append((np.sum((self.hist_blue-means[2])**3)/self.hist_blue.size)/math.sqrt((np.sum((self.hist_blue-means[2])**2)/self.hist_blue.size)**3))
        return result

    #zwraca skosnosc histogramu na kazdym kanale [H,S,V]
    def hist_skos_HSV(self):
        result=[]
        means=self.hist_srednia_HSV()
        result.append((np.sum((self.hist_h-means[0])**3)/self.hist_h.size)/math.sqrt((np.sum((self.hist_h-means[0])**2)/self.hist_h.size)**3))
        result.append((np.sum((self.hist_s-means[1])**3)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-means[1])**2)/self.hist_s.size)**3))
        result.append((np.sum((self.hist_v-means[2])**3)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-means[2])**2)/self.hist_v.size)**3))
        return result

    #zwraca skosnosc histogramu na kazdym kanale [L,a*,b*]
    def hist_skos_LAB(self):
        result=[]
        means=self.hist_srednia_LAB()
        result.append((np.sum((self.hist_l-means[0])**3)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-means[0])**2)/self.hist_l.size)**3))
        result.append((np.sum((self.hist_a-means[1])**3)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-means[1])**2)/self.hist_a.size)**3))
        result.append((np.sum((self.hist_b-means[2])**3)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-means[2])**2)/self.hist_b.size)**3))
        return result

    #zwraca kurtoze histogramu na kazdym kanale [R,G,B]
    def hist_kurt_RGB(self):
        result=[]
        means=self.hist_srednia_RGB()
        result.append((np.sum((self.hist_red-means[0])**4)/self.hist_red.size)/math.sqrt((np.sum((self.hist_red-means[0])**2)/self.hist_red.size)**4)-3)
        result.append((np.sum((self.hist_green-means[1])**4)/self.hist_green.size)/math.sqrt((np.sum((self.hist_green-means[1])**2)/self.hist_green.size)**4)-3)
        result.append((np.sum((self.hist_blue-means[2])**4)/self.hist_blue.size)/math.sqrt((np.sum((self.hist_blue-means[2])**2)/self.hist_blue.size)**4)-3)
        return result

    #zwraca kurtoze histogramu na kazdym kanale [H,S,V]
    def hist_kurt_HSV(self):
        result=[]
        means=self.hist_srednia_HSV()
        result.append((np.sum((self.hist_h-means[0])**4)/self.hist_h.size)/math.sqrt((np.sum((self.hist_h-means[0])**2)/self.hist_h.size)**4)-3)
        result.append((np.sum((self.hist_s-means[1])**4)/self.hist_s.size)/math.sqrt((np.sum((self.hist_s-means[1])**2)/self.hist_s.size)**4)-3)
        result.append((np.sum((self.hist_v-means[2])**4)/self.hist_v.size)/math.sqrt((np.sum((self.hist_v-means[2])**2)/self.hist_v.size)**4)-3)
        return result

    #zwraca kurtoze histogramu na kazdym kanale [L,a*,b*]
    def hist_kurt_LAB(self):
        result=[]
        means=self.hist_srednia_LAB()
        result.append((np.sum((self.hist_l-means[0])**4)/self.hist_l.size)/math.sqrt((np.sum((self.hist_l-means[0])**2)/self.hist_l.size)**4)-3)
        result.append((np.sum((self.hist_a-means[1])**4)/self.hist_a.size)/math.sqrt((np.sum((self.hist_a-means[1])**2)/self.hist_a.size)**4)-3)
        result.append((np.sum((self.hist_b-means[2])**4)/self.hist_b.size)/math.sqrt((np.sum((self.hist_b-means[2])**2)/self.hist_b.size)**4)-3)
        return result

    #zwraca entropie obrazu w RGB (float)
    def entropia_RGB(self):
        result=[]
        result.append(shannon_entropy(self.img[:,:,0]))
        result.append(shannon_entropy(self.img[:,:,1]))
        result.append(shannon_entropy(self.img[:,:,2]))
        return result

    #zwraca entropie obrazu w HSV (float)
    def entropia_HSV(self):
        hsv_img=skimage.color.rgb2hsv(self.img)
        result=[]
        result.append(shannon_entropy(hsv_img[:,:,0]))
        result.append(shannon_entropy(hsv_img[:,:,1]))
        result.append(shannon_entropy(hsv_img[:,:,2]))
        return result

    #zwraca entropie obrazu w La*b* (float)
    def entropia_LAB(self):
        lab_img=skimage.color.rgb2lab(self.img,"D65","2")
        result=[]
        result.append(shannon_entropy(lab_img[:,:,0]))
        result.append(shannon_entropy(lab_img[:,:,1]))
        result.append(shannon_entropy(lab_img[:,:,2]))
        return result
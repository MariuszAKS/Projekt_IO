import numpy as np
import skimage.io
import skimage.color

#klasa do generacji cech kolorymetrycznych
#obraz i maska jako argumenty do konstruktora, zmien_obraz aby zmienic obraz/maske
#image=scierzka do pliku/numpy array
#mask=maska (numpy bool array from Thresholding)
class CechyKolorymetryczne:
    def __init__(self,image,mask) -> None:
        if type(image) == str:
            self.img=skimage.io.imread(image)
        else:
            self.img=image
        self.mask=mask

    def zmien_obraz(self,image,mask):
        if type(image) == str:
            self.img=skimage.io.imread(image)
        else:
            self.img=image
        self.mask=mask

    #zwraca srednia pikseli na kazdym kanale [R,G,B]
    def srednia_RGB(self):
        result=[]
        for channel in range(0,3):
            value=0.0
            count=0
            for i in range(0,self.img.shape[0]):
                for j in range(0,self.img.shape[1]):
                    if self.mask[i,j]==True:
                        value+=self.img[i,j,channel]
                        count+=1
            result.append(value/count)
        return result

    #zwraca srednia pikseli na kazdym kanale [H,S,V]
    def srednia_HSV(self):
        hsv_img=skimage.color.rgb2hsv(self.img)
        result=[]
        for channel in range(0,3):
            value=0.0
            count=0
            for i in range(0,hsv_img.shape[0]):
                for j in range(0,hsv_img.shape[1]):
                    if self.mask[i,j]==True:
                        value+=hsv_img[i,j,channel]
                        count+=1
            result.append(value/count)
        return result

    #zwraca srednia pikseli na kazdym kanale [L,a*,b*]
    def srednia_LAB(self):
        lab_img=skimage.color.rgb2lab(self.img,"D65","2")
        result=[]
        for channel in range(0,3):
            value=0.0
            count=0
            for i in range(0,lab_img.shape[0]):
                for j in range(0,lab_img.shape[1]):
                    if self.mask[i,j]==True:
                        value+=lab_img[i,j,channel]
                        count+=1
            result.append(value/count)
        return result

    #zwraca odchylenie standardowe na kazdym kanale [R,G,B]
    def std_RGB(self):
        result=[]
        red=self.img[:,:,0]
        green=self.img[:,:,1]
        blue=self.img[:,:,2]
        result.append(np.std(red[self.mask]))
        result.append(np.std(green[self.mask]))
        result.append(np.std(blue[self.mask]))
        return result

    #zwraca odchylenie standardowe na kazdym kanale [H,S,V]
    def std_HSV(self):
        hsv_img=skimage.color.rgb2hsv(self.img)
        result=[]
        hue=hsv_img[:,:,0]
        sat=hsv_img[:,:,1]
        val=hsv_img[:,:,2]
        result.append(np.std(hue[self.mask]))
        result.append(np.std(sat[self.mask]))
        result.append(np.std(val[self.mask]))
        return result

    #zwraca odchylenie standardowe na kazdym kanale [L,a*,b*]
    def std_LAB(self):
        lab_img=skimage.color.rgb2lab(self.img,"D65","2")
        result=[]
        l=lab_img[:,:,0]
        a=lab_img[:,:,1]
        b=lab_img[:,:,2]
        result.append(np.std(l[self.mask]))
        result.append(np.std(a[self.mask]))
        result.append(np.std(b[self.mask]))
        return result

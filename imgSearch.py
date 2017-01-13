#Copyright (c) 2017, BaoXingce.
#E-mail: 1652256031@qq.com
#License: GPL
from PIL import ImageGrab
from PIL import Image
from method import *
import math
class search():
    pass
class imgSearch(search):
    def __init__(self,im2,im1=ImageGrab.grab()):
        self.im1=im1#.convert("1")
        self.im2=Image.open(im2)#.convert("1")
        self.Threshold1=0.5
        #self.Threshold2=0.3
        self.cmpSize1=(20,20)
        #self.cmpSize2=(64,64)
    #def search(self):
        #imglist=self.split_image(self.im1,self.im2.size)
        #position=[]
        #for index,img in enumerate(imglist):
            #cmp=dHash(im1=img[0],im2=self.im2).value()
        #    cmp=pixelCompare(self.cmpSize1,img[0],self.im2).value()
            
        #    if cmp<self.Threshold1:
        #        position.append((img[1]+0.5*self.im2.size[0],img[2]+0.5*self.im2.size[1]))
        
        #for i in range(imglist.count("n")):
        #    imglist.remove("n")
        #print (imglist)
        #for index,img in enumerate(imglist):
        #    cmp=pixelCompare(self.cmpSize2,img[0],self.im2).value()
        #    if cmp>self.Threshold:
        #        del(imglist[index])
        #    else:
        #        imglist[index]=(img[1]+0.5*self.im2.size[0],img[2]+0.5*self.im2.size[1])
        #return position
    def averagePosition(self):
        position=self.search()
        if len(position)==0:
            return None
        sumx=0
        sumy=0
        for i in position:
            sumx=sumx+i[0]
            sumy=sumy+i[1]
        return round(sumx*1.0/len(position)),round(sumy*1.0/len(position))
    def search(self):
               pw,ph = self.im2.size
               w,h = self.im1.size

               position=[]
               self.im1=self.im1.convert("1")
               self.im2=self.im2.convert("1")
               for i in range(0,w,math.ceil(pw/50)):
                       for j in range(0,h,math.ceil(ph/50)):
                               if i+pw<w and j+ph<h:
                                   sub_image = self.im1.crop((i,j,i+pw,j+ph))#.copy()
                                   cmp=pixelCompare(self.cmpSize1,sub_image,self.im2,mode="1").value()
                                   if cmp<self.Threshold1:
                                        position.append((i+0.5*self.im2.size[0],j+0.5*self.im2.size[1]))
                               elif j+ph>h:
                                   continue
                               elif i+pw>w:
                                   #print (sub_image_list)
                                   return position

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

#the function classfiy_histogram,calculate,split_image,classfiy_histogram_with_split are found on github MashiMaroLjc/Learn-to-identify-similar-images
#All the copyright belongs to MashiMaroLjc 
#Original Copyright information is below.

#This module can classify the image by histogram.
#This method is easy for someone who is a beginner in Image classification.
#
#author MashiMaroLjc
#version 2016-2-16
class method ():
        def __init__(self,im1,im2):
                self.im1=im1
                self.im2=im2
        def value(self):
                pass
class histgram(method):
        def __init__(self,im1,im2,resize=(256,256),split=True,part_size=(64,64)):
                super().__init__(im1,im2)
                self.size=resize
                self.split=split
                self.part_size=part_size
        def value(self):
                if self.split is True:
                        return self.classfiy_histogram(self.im1,self.im2,self.size)
                else:
                        return classfiy_histogram_with_split(self.im1,self.im2,self.size,self.part_size)
#This module can classfiy the image by Average Hash Method with spilt the image to 16 pieces.
#Then calculate every piece ,consider all data and return the result
#
#author MashiMaroLjc
#version 2016-2-17

        def calculate(image1,image2):
                g = image1.histgram()
                s = image2.histgram()
                assert len(g) == len(s),"error"

                data = []

                for index in range(0,len(g)):
                        if g[index] != s[index]:
                                data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )
                        else:
                                data.append(1)
    
                return sum(data)/len(g)



        def split_image(image,part_size):
               pw,ph = part_size
               w,h = image.size

               sub_image_list = []

               assert w % pw == h % ph == 0,"error"

               for i in range(0,w,pw):
                       for j in range(0,h,ph):
                               sub_image = image.crop((i,j,i+pw,j+ph)).copy()
                               sub_image_list.append(sub_image)

               return sub_image_list

        def classfiy_histogram_with_split(image1,image2,size = (256,256),part_size=(64,64)):
            ''' 'image1' and 'image2' is a Image Object.
                  You can build it by 'Image.open(path)'.
                  'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.  
                  'part_size' is size of piece what the image will be divided.It's 64*64 when it default.
                  This function return the similarity rate betweene 'image1' and 'image2'
            '''
            image1 = image1.resize(size).convert("RGB")
            sub_image1 = self.split_image(image1,part_size)

            image2 = image2.resize(size).convert("RGB")
            sub_image2 = self.split_image(image2,part_size)

            sub_data = 0;
            for im1,im2 in zip(sub_image1,sub_image2):
                 sub_data += self.calculate(im1, im2)

            x = size[0]/part_size[0]
            y = size[1]/part_size[1]

            pre = round((sub_data/(x*y) ),3 )
            return  pre    
        def classfiy_histogram(self,image1,image2,size):
                ''' 'image1' and 'image2' is a Image Object.
                  You can build it by 'Image.open(path)'.
                  'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.  
                  This function return the similarity rate betweene 'image1' and 'image2'
                '''
                image1 = image1.resize(size).convert("RGB")
                g = image1.histogram()

                image2 = image2.resize(size).convert("RGB")
                s = image2.histogram()

                assert len(g) == len(s),"error"

                data = []

                for index in range(0,len(g)):
                         if g[index] != s[index]:
                                data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )
                         else:
                                data.append(1)
    
                return sum(data)/len(g)
#the function getCode,compCode,classfiy_dHash are found on github MashiMaroLjc/Learn-to-identify-similar-images
#All the copyright belongs to MashiMaroLjc 
#Original Copyright information is below.


#This module can classfy the image by dHash
#
#author MashiMaroLjc
#version 2016-2-16
class dHash(method):
        def __init__(self,im1,im2,resize=(9,8)):
                super().__init__(im1,im2)
                self.size=resize
        def value(self):
                return classfiy_dHash(self.im1,self.im2,self.size)
        def getCode(self,img,size):

                result = []
                # print("x==",size[0])
                # print("y==",size[1]-1)
    
                x_size = size[0]-1#width
                y_size = size[1] #high
                for x in range(0,x_size):
                        for y in range(0,y_size):
                                now_value = img.getpixel((x,y))
                                next_value = img.getpixel((x+1,y))

                if next_value < now_value:
                        result.append(1)
                else:
                        result.append(0)


                return result
        def compCode(self,code1,code2):
                num = 0
                for index in range(0,len(code1)):
                        if code1[index] != code2[index]:
                                    num+=1
                return num 

        def classfiy_dHash(self,image1,image2,size):
                ''' 'image1' and 'image2' is a Image Object.
                You can build it by 'Image.open(path)'.
                'Size' is parameter what the image will resize to it and then image will be compared to another image by the dHash.
                It's 9 * 8 when it default.  
                The function will return the hamming code,less is correct. 
                '''
                image1 = image1.resize(size).convert('L')
                code1 = self.getCode(image1, size)


                image2 = image2.resize(size).convert('L')
                code2 = self.getCode(image2, size)

                assert len(code1) == len(code2),"error"
    
                return self.compCode(code1, code2)
class pixelCompare(method):
        def __init__(self,im1,im2,resize=-1):
                super().__init__(im1,im2)
                if resize==-1:
                        resize=im2.size
                self.size=resize
                im1=im1.resize(resize)
                im2=im2.resize(resize)
        def value(self):
                return compare_every_dot(im1,im2)
        def compare_every_dot(im1,im2):
                width,height=self.size
                sumpixel=0
                for h in range(0, height):  
                        for w in range(0, width):  
                                pixel1 = im1.getpixel((w, h))
                                pixel2 = im2.getpixel((w, h))
                                for i in range(0,3):
                                        sumpixel=sumpixel+(pixel1[i]-pixel2[i])**2
                return sumpixel
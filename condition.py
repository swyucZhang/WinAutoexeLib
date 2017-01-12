from PIL import ImageGrab
from PIL import Image
from method import *
class condition():
    def __init__(self,funSccd,funFail,expr):
        self.fun1=funSccd
        self.fun2=funFail
        self.expr=expr
    def execute(self):
        if (self.expr.boolean()):
            self.fun1()
        else :
            self.fun2()
class expr():
    def __init__(self):
        pass
    def boolean(self):
        pass
    def grab(self):
        pass
class dotCmp(expr):
    def __init__(self,dotPos,color,strict):
        super().__init__()
        self.dotPos=dotPos
        self.color=color
        self.strict=strict
    def grab(self):
        im = ImageGrab.grab((self.dotPos[0],self.dotPos[1],self.dotPos[0]+1,self.dotPos[1]+1))
        # I am not sure whether the plus one thing above can cause overflow.I think this is right
        #print (im.size)
        red, green, blue=im.getpixel((0, 0))
        return red, green, blue
    def boolean(self):
        red, green, blue=self.grab()
        red, green, blue=self.color[0]-red,self.color[1]-green,self.color[2]-blue
        if (red**2+green**2+blue**2)/256**2<=self.strict:
            return True
        else:
            return False
class imgCmp(expr):
    def __init__(self,imgPos,imgFile,strict,method=None):
        super().__init__()
        self.imgPos=imgPos
        self.imgFile=imgFile
        self.strict=strict
        self.method=method
    def grab(self):
        im1 = ImageGrab.grab((self.imgPos[0][0],self.imgPos[0][1],self.imgPos[1][0],self.imgPos[1][1]))
        #print (im.size)
        im2 = Image.open(self.imgFile)
        return im1,im2
    def boolean(self):
        im1,im2=self.grab()
                
        if self.method is None:
            self.method=histgram()
        self.method.im1=im1
        self.method.im2=im2
        if self.method.value()<= self.strict:
            return True
        else:
            return False
            
        
        
        
            

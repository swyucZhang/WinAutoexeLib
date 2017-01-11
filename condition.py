from PIL import ImageGrab

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
        if red**2+green**2+blue**2<=self.strict:
            return True
        else:
            return False
       
            
            
        
        
        
            

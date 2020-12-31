class figure2d():
    S = None
    P = None
    pi = 3.14
    default_dict = {"mm":[1000,1000000],"cm":[100,10000],"dm":[10,100],"km":[0.001,0.000001]}
    edi = "m"
    def get_data(self):
        return {"S":self.S,"P":self.P,"ED":self.edi,"W":self.get_wersh()}


class rectangle(figure2d):
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.S = self.a * self.b
        self.P = (self.a + self.b) * 2
    
    def recount(self,edinitsa,dct=None):
        if dct == None:
            dct = self.default_dict
        w = dct[edinitsa][0]
        wkv = dct[edinitsa][1]
        self.edi = edinitsa
        self.a = self.a * w
        self.b = self.b * w
        self.P = self.P * w
        self.S = self.S * wkv
    def get_wersh(self):
        return (self.a,self.b)

class circle(figure2d):
    r = 0
    d = 0
    def __init__(self,r,pi=3.14):
        self.pi = pi
        self.r = r
        self.d = r*2
        self.S = (self.pi * self.r) ** 2
        self.P = (self.pi * self.r) * 2
    
    def recount(self,edinitsa,dct=None):
        if dct == None:
            dct = self.default_dict
        w = dct[edinitsa][0]
        wkv = dct[edinitsa][1]
        self.edi = edinitsa
        self.r = self.r * w
        self.d = self.d * w
        self.P = self.P * w
        self.S = self.S * wkv
    
    def get_wersh(self):
        return (self.r,self.d)

class triangle(figure2d):
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.P = a+b+c
    
    def recount(self,edinitsa,dct=None):
        if dct == None:
            dct = self.default_dict
        w = dct[edinitsa][0]
        wkv = dct[edinitsa][1]
        self.edi = edinitsa
        self.a = self.a * w
        self.b = self.b * w
        self.c = self.c * w
        self.P = self.P * w
    def get_wersh(self):
        return (self.a,self.b,self.c)

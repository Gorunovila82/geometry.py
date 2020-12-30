class figure3d():
    Sa = None
    L = None
    V = None
    pi = 3.14
    default_dict = {"mm":[1000,1000000,1000000000],"cm":[100,10000,1000000],"dm":[10,100,1000],"km":[0.001,0.000001,0.000000001]}
    edi = "m"
    def get_data(self):
        return {"S":self.Sa,"L":self.L,"V":self.V,"ED":self.edi}
    
class cube(figure3d):
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.V = a*b*c
        self.Sa = 2*b*c + 2*c*a + 2*a*b
        self.L  = c+b+a * 4

print(cube(1,2,3).get_data())
class Road():
    __le=0
    __wi=0
    def Work(self,__le,__wi):
        mass=__wi*__le*25*5
        print(mass," kg needs")
        return mass


r=Road()
r.Work(10000,20)



class Toffoli_Gate:
    def __init__(self,lains): self.lains=lains

    def use_Toffoli(self,num):
        binar = bin(num)[2:].zfill(4)
        binar = list(map(int, binar))
        binar[self.lains[0]] = binar[self.lains[0]] ^ (binar[self.lains[1]] & binar[self.lains[2]])
        return int(''.join(list(map(str, binar))), 2)

    def __str__(self): return "Toffoly on lains: {}".format(self.lains)
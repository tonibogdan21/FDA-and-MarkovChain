from informatiiAFD_Tema_2 import *


class AFD(object):

    def __init__(self, stari, sigma, stareInit, finale, delta):
        self.stari = stari
        self.sigma = sigma
        self.stareInit = stareInit
        self.finale = finale
        self.delta = delta

    def inputText(self):
        exists = False
        while exists == False:
            string=input("Introduceti un cuvant pentru a fi verificat: ")
            if any(s in self.sigma for s in string):
                exists = True
                return string

    def verify(self):
        cur_state = self.stareInit
        while(1):
            cur_state = self.stareInit
            string = self.inputText()
            
            for symbol in string:
                print("["+str(cur_state)+"]"+"-"+symbol+"->",end="")
                cur_state= self.delta[self.sigma.index(symbol)][cur_state]

            if cur_state in self.finale:
                print("["+str(cur_state)+"]")
                print("Acceptat")
            else:
                print("["+str(cur_state)+"]")
                print("Neacceptat")

            anotherOne = input("Doriti sa mai derivati un alt cuvant? da sau nu: ")
            if anotherOne == "nu":
                break

if __name__ == '__main__':
    ExempluAFD = AFD(stari, sigma, stareInit, finale, delta)
    ExempluAFD.verify()

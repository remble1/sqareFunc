from math import sqrt 

print("Najpierw program zapyta Cię ile razy masz powtórzyć pętlę, później poprosi Cie o podanie współczynników\n")

class Counter():
  def __init__ (self,a,b,c):
    self.a = a
    self.b = b
    self.c = c 
    self.delt = 0
    self.x1 = 0
    self.x2 = 0

  def coutZero(self): 
    self.delt = self.b**2-4*self.a*self.c 
    print(f"Delta wynosi: {self.delt}")
    if self.delt < 0:
      print("brak")
    else: 
      self.x1 = ((-self.b + sqrt(self.delt))/2*self.a)
      self.x2 = ((-self.b - sqrt(self.delt))/2*self.a)
      print(f"Miesca zerowe: {self.x1},{self.x2}")

  def saveToFile(self, delt, x1, x2):
      date = (f"Wspolczynniki: A: {self.a}, B: {self.b}, C: {self.c}, Delta: {delt}, Miejsca zerowe: {x1}, {x2}")
      file_object = open('saveDate.txt', 'w')
      file_object.write(date)
    

try:
  rang = int(input("Ile chcesz policzyć pętli?\n"))
except:
  print("Podaj wartość całkowitą")

for i in range(0,rang):
  try:
    a = float(input("Podaj współczynnik A: "))
    b = float(input("Podaj współczynnik B: "))
    c = float(input("Podaj współczynnik C: ")) 
  except:
    print("Podałeś zły typ danej, mają być całkowiete lub zmiennoprzecinkowe\n Dane wcześniejszej funkcji:")
  
  nazwaObj = i 
  nazwaObj = Counter(a,b,c)
  nazwaObj.coutZero()
  nazwaObj.saveToFile(nazwaObj.delt,nazwaObj.x1,nazwaObj.x2)
  
print("Program skończył pracę")
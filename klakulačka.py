print("Vítejte v kalkulačce, pokud ji chcete ukončit, napište 'konec' do funkce")
while True:  
  cislo1 = float(input("Zadej číslo 1:"))
  cislo2 = float(input("Zadej číslo 2:"))
  operace = input("Zadej operaci' +, -, *, /")

  if operace == "+":
      print(cislo1 + cislo2)
  elif operace == "-":
      print(cislo1 - cislo2)
  elif operace == "*":
      print(cislo1 * cislo2)
  elif operace == "**":
      print(cislo1 ** cislo2)
  elif operace == "//":
      print(cislo1 // cislo2)
  elif operace == "/":
      print(cislo1 / cislo2)
      if cislo2 == 0:
          print("Nulou se nedělí")
      else:
          print(cislo1 / cislo2)
  elif operace == "konec":
      break
  else:
      print("Konec")
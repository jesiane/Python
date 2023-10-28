def add(a,b):
    aswer = a + b
    print(str(a) + " + " + str(b) + " = " + str(aswer) + "\n")

def sub (a,b):
    aswer = a - b
    print(str(a) + " - " + str(b) + " = " + str(aswer) + "\n")

def mult(a,b):
    aswer = a * b
    print(str(a) + " * " + str(b) + " = " + str(aswer) + "\n")

def div(a,b):
    aswer = a / b
    print(str(a) + " / " + str(b) + " = " + str(aswer) + "\n")


while True:
  print ("A. Adição")
  print ("B. Sbtração")
  print ("C. Multiplicação")
  print ("D. Divisão")
  print ("E. Exit")

  choice = input("input your choice: ")

  if choice == "a" or choice == "A":
      print("Adição")
      a = int(input("input first number: "))
      b = int(input("input second number: "))
      add(a,b)
  elif choice == "b" or choice == "B":
      print("Subtração")
      a = int(input("input first number: "))
      b = int(input("input second number: "))
      sub(a,b)
  elif choice == "c" or choice == "C":
      print("Multiplicação")
      a = int(input("input first number: "))
      b = int(input("input second number: "))
      mult(a,b)
  elif choice == "d" or choice == "D":
      print("Divisão")
      a = int(input("input first number: "))
      b = int(input("input second number: "))
      div(a,b)
  elif choice =="e" or choice == "E":
      print("program ended")
      quit()


import random


x: int = random.randint(1, 100)
versuche: int = 0

print("Ich gebe dir eine beliebige Zahl zwischen 1 und 100.\n Du musst mir mitteilen:")
print("Ob sich diese Zahl durch 3 teilen lässt. (Antworte mit 'Fizz')")
print("Ob sich diese Zahl durch 5 teilen lässt. (Antworte mit 'Buzz')")
print("Ob sich diese Zahl durch 3 UND 5 teilen lässt.(Antworte mit 'FizzBuzz')")
print("Wenn nichts davon zutrifft, antworte mit 'weiter'.")

while True:

    if versuche == 5:
        break
    versuche += 1
    x: int = random.randint(1, 100)
    print("Das ist meine Zahl:")
    print(x)


    answ: str = input("Antwort:\n")


    if x % 3 == 0 and x % 5 == 0:
        if answ == "FizzBuzz":
          print("Richtig")
        else:
          print("Falsch, weder teilbar durch 3 noch durch 5")
    elif x % 3 == 0:
        if answ == "Fizz":
          print("Richtig")
        else:
          print("Falsch, teilbar durch 3")
    elif x % 5 == 0:
        if answ == "Buzz":
          print("Richtig")
        else:
           print("Falsch, teilbar durch 5 ")
    elif x % 3 != 0 and x % 5 != 0:
        if answ == "weiter":
          print("Richtig")
        else:
          print("Falsch, weder teilbar durch 3 noch durch 5")
    elif x % 3 != 0:
        if answ == "weiter":
         print("Richtig")
        else:
         print("Falsch, nicht teilbar durch 3")
    elif x % 5 != 0:
        if answ == "weiter":
         print("Richtig")
        else:
            print("Falsch, nicht teilbar durch 5")

import random, time
rocks=random.randint(4,30)
print("Добро пожаловать!!! Играем в кучу камней")
print("Побеждает тот, кто оставит последний камень сопернику")
print(f"Сейчас в куче %d  камней" %rocks)
print("Брать можно от 1 до 3х камней")
rob=chel=0
def hodmashiny():
    if rocks>4:
        taken=random.randint(1,3)
    else:
        taken = random.randint(1, rocks-1)
    print(f"Машина взяла %d камней." %taken)
    print("Осталось %d камней." %(rocks-taken))
    return taken
def hodcheloveka():
    takench=int(input("Сколько камней вы возьмёте?"))
    print("Осталось %d камней." % (rocks - takench))
    return takench

while True:
    rocks-=hodcheloveka()
    if rocks<1:
        print("Error vce")
        break
    elif rocks==1:
        print("Win")
        break
    rocks-=hodmashiny()
    if rocks<1:
        print("Error vce")
        break
    elif rocks==1:
        print("Loose")
        break
    print("\n***Следующий ход***\n")

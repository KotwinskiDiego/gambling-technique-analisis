import math
import random

cel = 20000
loses = 0
j = 1
play = True
money = 10000
all_in = 0
while money>0 and money<cel and play==True: # petla wszystkich gier
    win = False
    i = 0 # reset pętli pojedyńczej gry
    loss = 1 # początkowa stawka

    print(j,".stan konta: " , money)

    while win==False and money>0: # petla pojedyńczej gry
        # zabieramy stawke na początku pętli bo podnosimy stawke w poprzedniej iteracji po przegranej a sprawdzamy czy mamy na to pieniądze na końcu pętli
        money -= loss
        winorlose = random.randint(0,1) #0-wygrana 1-przegraana
        if winorlose == 1:
            win=False
            print(i+1,"Przegrana: ", money, f"zabrało: {loss} zł")
            loss = min(loss*2, money) # jeżeli przegramy i nie stać nas na podwojenie stawki to wchodzimy all in
            if loss < 2**(i+1):
                all_in = j
        elif winorlose == 0:
            money+= 2*loss
            win = True #przerywa pętle po iteracji
            print(i + 1, "Wygrana: ", money)

        if money < loss: #sprawdzenie czy mamy wystarczająco pieniędzy na następną iteracje
            play = False
            break
        i+=1
    j+=1
if all_in:
    print(f"all in został użyty w rundzie {all_in}")


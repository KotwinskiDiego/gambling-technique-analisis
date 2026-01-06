import math
import random

cel = 200000
loses = 0
summ = 0
ilosc_gier = 10
j = 1
poczatkowa_kasa = 10000

for game in range(ilosc_gier):
    gmoney = poczatkowa_kasa   # kasa, którą obstawiamy (bankroll)
    money = 0                  # "skarbonka" — tu odkładamy wygrane
    while gmoney > 0:
        win = False
        i = 0
        total_bet = 0         # ile wydaliśmy w tej serii (przed wygraną)
        # pojedyncza seria martingale
        while not win and gmoney > 0:
            # oblicz stawkę na tę iterację (cap do dostępnego salda)
            loss = min(2 ** i, gmoney)
            if loss <= 0:
                # nie ma już za co postawić
                break

            # postawienie
            gmoney -= loss
            total_bet += loss

            winorlose = random.randint(0, 1)  # 0 - wygrana, 1 - przegrana
            if winorlose == 1:
                # przegrana — przygotuj następną stawkę (zostawiamy gmoney tak jak jest)
                # następna stawka będzie liczona jako 2**(i+1) ale capowana do gmoney
                i += 1
                # jeśli gmoney == 0 to pętla się zakończy
            else:
                # wygrana — otrzymujesz payout = 2 * loss (w momencie wygranej)
                payout = 2 * loss
                profit = payout - total_bet
                # dodajemy rzeczywisty zysk do skarbonki
                money += profit
                # resetujemy bankroll do początkowej wartości (tak jak w Twoim założeniu)
                gmoney = poczatkowa_kasa
                win = True

            # jeśli nie mamy wystarczająco na kolejną iterację (następne 2**i) -> przerwij serie
            # to zabezpieczenie: jeżeli gmoney == 0 pętla while not win zakończy się naturalnie
            # więc tutaj nic więcej nie trzeba robić
        # koniec jednej serii; pętla while gmoney>0 będzie kontynuować dopóki gmoney>0
        j += 1

        # zabezpieczenie (opcjonalne): unikamy nieskończonej pętli, ale Twoja logika resetu gmoney->poczatkowa_kasa
        # po wygranej sprawia, że przy zwycięstwie pętla będzie kontynuować. Tutaj kontynuujemy dopóki
        # gmoney > 0 (czyli aż się wyczerpie).
    # koniec jednej gry (bankroll wyczerpany)
    print(game, ".skarbonka zebrała:", money)
    summ += money

print("SUMA ze wszystkich gier (skarbonka):", summ)


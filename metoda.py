import math
import random

# parametry gry
cel = 20000
poczatkowa_kasa = 10000
liczba_symulacji = 100

# statystyki
wygrane = 0
przegrane = 0
uzyto_all_in = 0
all_in_uratowal = 0  # nowa statystyka

for game in range(liczba_symulacji):
    money = poczatkowa_kasa
    play = True
    j = 1
    all_in = False  # czy w tej grze był all-in

    # główna pętla gry
    while money > 0 and money < cel and play:
        win = False
        i = 0
        loss = 1

        while not win and money > 0:
            money -= loss
            winorlose = random.randint(0, 1)  # 0 - wygrana, 1 - przegrana

            if winorlose == 1:
                win = False
                new_loss = loss * 2
                if new_loss > money:  # brak środków na pełne podwojenie
                    all_in = True
                loss = min(new_loss, money)

            elif winorlose == 0:
                money += 2 * loss
                win = True  # kończy pętlę pojedynczej gry

            if money < loss:
                play = False
                break
            i += 1
        j += 1

    # po zakończeniu gry
    if money >= cel:
        wygrane += 1
        # jeśli wygrał, a wcześniej był all-in → all-in uratował
        if all_in:
            all_in_uratowal += 1
    else:
        przegrane += 1

    if all_in:
        uzyto_all_in += 1

# statystyki końcowe
print("=== STATYSTYKI PO 100 SYMULACJACH ===")
print(f"Wygrane (osiągnięto {cel} zł): {wygrane}")
print(f"Przegrane (bankructwo): {przegrane}")
print(f"All-in wystąpił w: {uzyto_all_in} grach ({uzyto_all_in/liczba_symulacji*100:.1f}%)")
print(f"All-in uratował grę w: {all_in_uratowal} przypadkach ({(all_in_uratowal/liczba_symulacji*100):.1f}% ogółem, {(all_in_uratowal/uzyto_all_in*100 if uzyto_all_in>0 else 0):.1f}% z all-inów)")
print(f"Skuteczność strategii: {wygrane/liczba_symulacji*100:.1f}%")

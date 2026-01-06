from simulation_class import CoinflipSimulation

simulation = CoinflipSimulation(10000,20000)

def generate(bet,iterations,filepath):
    for i in range(1, iterations+1):
        simulation.loop(i, bet, False)
        if i == 1:
            simulation.export_to_csv(filepath)
        else:
            simulation.append_to_csv(filepath)
        print(f"for now {i} loop is exported(bet at {bet})")

def append(bet,iterations,filepath):
    for i in range(1, iterations + 1):
        simulation.loop(i, bet, False)
        simulation.append_to_csv(filepath)
        print(f"for now {i} loop is exported(bet at {bet})")

file = "data.csv"
#generujemy po 100 loopów dla każdego incjalnego-beta i tysiąc betów od 1-1000
for i in range(1,1000):
    if i == 1:
        generate(1,100,file)
    else:
        append(i,100,file)





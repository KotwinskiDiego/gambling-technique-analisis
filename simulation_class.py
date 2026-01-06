import pandas as pd
import random



class CoinflipSimulation:
    def __init__(self, start_money, goal_money):
        self.start_money = start_money
        self.goal_money = goal_money
        self.money = start_money

        self.data = []

    def cycle(self, bet, prints=False):


        temp_bet = bet
        info = {"money":self.money,
                "bet":temp_bet,
                "bets in cycle": 1,
                "all-in":False,
                "all-in-money": 0,
                "lost_cycle": False
                }
        while self.money > 0:

            win = random.randint(0,1)
            if win == 1:

                self.money += bet
                if prints:
                    print(f"you won, now you have {self.money} money")
                break
            else:
                #ustawiamy tutaj bo już przegrałem a niżej daje warunki kolejnego betu
                self.money -= bet
                if prints:
                    print(f"you lost your last bet")
                # powtarzam self.money > 0 bo pieniądze rozliczam wyżej a chce mieć zapisane jak wysoki był all in w danych
                if self.money <= bet*2 and self.money > 0:
                    bet = self.money


                    if prints:
                        print(f"now you have {self.money} money and u forced to bet all of that")
                    info["all-in"] = True
                    info["all-in-money"] = self.money
                else:
                    if self.money <= 0:
                        info["lost_cycle"] = True
                        if prints:
                            print(f"you have {self.money} money :(")
                        break
                    bet *= 2
                    if prints:
                        print(f"now you have {self.money} money and u bet {bet} from that")
            info["bets in cycle"] += 1


        return info


    def loop(self,loop_iteration, bet, prints=False):
        i = 1

        while self.money > 0 and self.money < self.goal_money:
            info1 = {
                "loop_iteration": loop_iteration,
                "cycle_iteration": i
            }
            info2 = self.cycle(bet,prints=prints)
            # użycie merge operator |

            self.data.append(info1 | info2)




            i+=1
        self.money = self.start_money

    def export_to_csv(self, Filepath):
        df = pd.DataFrame(data=self.data)
        df.to_csv(Filepath, index=False,sep=';', encoding='utf-8-sig')
        self.clear_Data()

    def append_to_csv(self, Filepath):
        df = pd.DataFrame(data=self.data)
        df.to_csv(Filepath, index=False, mode='a',sep=';', encoding='utf-8-sig', header=False)
        self.clear_Data()

    def clear_Data(self):
        self.data = []








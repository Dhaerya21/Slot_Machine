import random as r
from Slots_art import symbols,payout

def show_slots(slot,balance):
    print("***************************")
    print(" | ".join(slot))
    balance =Wins(slot,balance)
    print("***************************")
    return balance

def slots(balance):
    if balance < 10:
        print("Insufficient funds! Please Deposit ")
        return balance
    balance-=10
    slot = [r.choice(symbols) for i in range(3)]
    balance=show_slots(slot,balance)
    return balance

def Wins(slot,balance):
    if slot[0]==slot[1]==slot[2]:
        balance +=1000
        print("Congratulations !!!!!")
        print("you won the jackpot")
        print(f"$1000 has been added to your balance")
    elif slot[0]==slot[1] or slot[2]==slot[1] or slot[0]==slot[2]:
            balance+= 50
            print("you won Minor win!!")
            print("$50 has been added to your balance")
    else:
        print("better luck next time")
    return balance


def main():
    pass

if __name__ == "__main__":
    main()       
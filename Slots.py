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
    pass


def main():
    pass

if __name__ == "__main__":
    main()       
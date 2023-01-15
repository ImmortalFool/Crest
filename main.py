import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_counts = {
    "7" : 2,
    "$" : 4,
    "&" : 6,
    "@" : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

# Checks taht user is entering valid amount
def deposit():
    while True:
        amount = input("What would you like to deposit? Rs.")
        if amount.isdigit(): # checks that the input is a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("PLease enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit(): # checks that the input is a number
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("PLease enter a number")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? Rs.")
        if bet.isdigit(): # checks that the input is a number
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be greater than Re.{MIN_BET} and less than Rs.{MAX_BET}")
        else:
            print("PLease enter a number")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"Insufficient Funds. Your current balance is Rs.{balance}")
        else:
            break
    print(f"You are betting Rs.{bet} on {lines}. Total bet is Rs.{total_bet}")



main()

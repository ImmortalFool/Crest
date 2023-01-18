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

symbol_values = {
    "7" : 5,
    "$" : 4,
    "&" : 3,
    "@" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] # Storing the columns not the rows
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    # Transposing the matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Checks that user is entering valid amount
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

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"Insufficient Funds. Your current balance is Rs.{balance}")
        else:
            break
    print(f"You are betting Rs.{bet} on {lines}. Total bet is Rs.{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_counts)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You have won Rs.{winnings}.")
    print(f"You won on lines", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs.{balance}")
        answer = input("Press enetr to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with Rs.{balance}")

main()

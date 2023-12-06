import random

MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 250
MIN_BET = 5

SLOTH_ROWS = 3
SLOTH_COLS = 3

symbol_count = {
    '@': 8,
    '$' : 2,
    '#' : 4,
    '&' : 6
}

symbol_value = {
    '@': 1,
    '$' : 10,
    '#' : 3,
    '&' : 5
}

def main():
    print(f""" Welcome to Sloth Machine Game!\n\n""")
    
    balance = 0
    while True:
        print(f"Your current balance is: {balance}")
        print("1: Add balance\n2: Play\n3: Quit game\n")
        choice = int(input("What you want to do? "))
        
        if choice == 3:
            print("\nThank you for playing!")
            break
        elif choice == 1:
            balance = amounts(action="deposit amount", min_value=1, max_value=10000)
            print()
        elif choice == 2:
            balance = play(balance)
            print()
        else:
            print("\nInvalid choice. Try again.\n")
            
        
    
    
    
# Collects user input
def amounts(action, min_value, max_value):
    while True:
        amount = input(f"Provide {action}, between {min_value} and {max_value}: ")
        if amount.isdigit():
            amount = int(amount)
            if amount in range(min_value, (max_value + 1)):
                break;
            else:
                print("Incorrect value. Out of range. Try again")
        else:
            print("Incorrect value. Not a number. Try again")
            
    return amount

# Generates single spin
def sloth_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    sloth = []
    
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        sloth.append(column)
        
    return sloth

# Draws sloth
def draw_sloth_machine(sloth):
    for row in range(len(sloth[0])):
        for i, item in enumerate(sloth):
            if i != len(sloth) - 1:
                print(item[row], end=" | ")
            else: 
                print(item[row], end="")
                
        print()

# Checks for winnings
def check_gains(sloth, lines, bet, values):
    gains = 0
    for line in range(lines): 
        symbol = sloth[0][line] # Holds the first column of each row 
        for col in sloth:
            symbol_check = col[line]
            if symbol != symbol_check:
                break 
        else: 
            gains += values[symbol] * bet
            
    return gains

# Play a round           
def play(balance):
    lines = amounts(action="number of lines", min_value=MIN_LINES, max_value=MAX_LINES)
    
    while True:
        bet = amounts(action="bet amount on each line", min_value=MIN_BET, max_value=MAX_BET)
        total_bet = bet * lines
        if total_bet < balance:
            balance = balance - total_bet
            break
        else:
            print("Not enough balance for that bet, try lower bets.")
    
    
    print(f"You are betting ${bet} on {lines}. Total bet = ${total_bet}. Your balance is now {balance}")
    print("Spinning machine.....")
    sloth = sloth_spin(SLOTH_ROWS, SLOTH_COLS, symbol_count)
    draw_sloth_machine(sloth)
    
    gains = check_gains(sloth, lines, bet, symbol_value)
    if gains:
        print(f"You won ${gains}. Congrats")
        balance += gains
    else:
        print("Not a win ;(")
    
    return balance
    
main()
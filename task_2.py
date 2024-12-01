from random import randint

def get_numbers_ticket(min, max, quantity):
    win_tickets = []
    try:
        if max-min < quantity:
            return "Please enter a valid range. Not enough unique numbers available."
    
        while len(win_tickets) < quantity:
            num = randint(min, max)
            if num not in win_tickets:
                win_tickets.append(num)
    except TypeError:
        return "Please enter a valid integer."
    else:
        win_tickets.sort()
        return f"Winning numbers: {win_tickets}"

print(get_numbers_ticket(9, 10, 3)) 
print(get_numbers_ticket(1, 10, 3)) 
print(get_numbers_ticket(1, 10, "three")) 
print(get_numbers_ticket("1", 10, 3)) 
from random import randint

def get_numbers_ticket(min, max, quantity):
    win_tickets = []
    try:
        for _ in range(quantity):
            win_tickets.append(randint(min, max))
    except TypeError:
        print("Please enter a valid integer.")
    else:
        return f"Ваші виграшні числа: {win_tickets}"

print(get_numbers_ticket(1, 10, 3)) 
print(get_numbers_ticket(1, 10, "three")) 
print(get_numbers_ticket("1", 10, 3)) 
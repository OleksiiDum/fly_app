

# Seats

def generate_seats():
    rows_econom = 25
    rows_business = 5
    seats_list = []
    current_letter = 0
    current_row = 1
    seats_letters = "ABCDEF"
    for i in range(rows_business):
        for j in range(4):
            t = str(current_row) + seats_letters[current_letter]
            current_letter += 1
            seats_list.append((t, 'business'))
        current_row += 1
        current_letter = 0
    for i in range(rows_econom):
        for j in range(6):
            t = str(current_row) + seats_letters[current_letter]
            current_letter += 1
            seats_list.append((t, 'econom'))
        current_row += 1
        current_letter = 0
    

    print(seats_list)
generate_seats()
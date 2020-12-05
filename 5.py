def seat_id(seat):
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7
    for c in seat[:7]:
        if c == 'F':
            row_max = row_min + (row_max - row_min) // 2
        elif c == 'B':
            row_min = row_min + (row_max - row_min) // 2
        else:
            assert False

    for c in seat[7:]:
        if c == 'R':
            col_min = col_min + (col_max - col_min) // 2
        elif c == 'L':
            col_max = col_min + (col_max - col_min) // 2
        else:
            assert False

    return row_max * 8 + col_max
            

assert seat_id('FBFBBFFRLR') == 357
assert seat_id('BFFFBBFRRR') == 567
assert seat_id('FFFBBBFRRR') == 119
assert seat_id('BBFFBBFRLL') == 820

def highest_seatid(all_seats):
    return max(seat_id(seat.strip()) for seat in all_seats)


def my_seat(all_seats):
    prev_seat = 0
    seat = None
    for seat in sorted(seat_id(seat.strip()) for seat in all_seats):
        print(seat)
        if seat == prev_seat + 2:
            break
        prev_seat = seat

    return seat - 1
    

with open('5.input') as f:
    all_seats = f.readlines()
    print("Highest seatid: ", highest_seatid(all_seats))
    print("My seatid: ", my_seat(all_seats))





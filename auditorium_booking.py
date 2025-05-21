num_rows = int(input("Enter number of rows: "))
s1, s2, s3 = 6, 10, 6
total_seats = s1 + s2 + s3
auditorium = [["-" for _ in range(total_seats)] for _ in range(num_rows)]
def book_seat(row, seat):
    if 0 <= row < num_rows and 0 <= seat < total_seats:
        if auditorium[row][seat] == "-": 
            auditorium[row][seat] = "*"
            print(f"Seat ({row+1}, {seat+1}) booked successfully!")
        else:
            print(f"Seat ({row+1}, {seat+1}) is already booked.")
    else: print("Invalid seat number. Please try again.")
def display_seating():
    print("\nCurrent Seating Arrangement:")
    for row in auditorium:
        print("".join(f" {s}" + (" " if i in [s1-1, s1+s2-1] else "") for i, s in enumerate(row)))
def get_seat_index(section, seat):
    return seat - 1 if section == 1 and 1 <= seat <= s1 else \
          s1 + seat - 1 if section == 2 and 1 <= seat <= s2 else \
          s1 + s2 + seat - 1 if section == 3 and 1 <= seat <= s3 else -1
while True:
    display_seating()
    if input("\nDo you want to book a seat? (yes/no): ").lower() == "no": break
    row = int(input(f"Enter row number to book (1 to {num_rows}): ")) - 1
    section = int(input("Enter section number to book (1, 2, or 3): "))
    if section not in [1, 2, 3]: print("Invalid section. Please try again."); continue
    max_seats = [s1, s2, s3][section - 1]
    seat_in_section = int(input(f"Enter seat number in section {section} (1 to {max_seats}): "))
    seat_index = get_seat_index(section, seat_in_section)
    if seat_index == -1: print("Invalid seat number. Please try again."); continue
    book_seat(row, seat_index)
print("\nFinal Auditorium Seating Arrangement:")
display_seating()
print("Booking process complete. Enjoy the show! 🎭")
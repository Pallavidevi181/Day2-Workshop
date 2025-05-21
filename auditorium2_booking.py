n = int(input("Enter number of rows: "))
a = [[0 for _ in range(5)] for _ in range(n)]
b = [[0 for _ in range(10)] for _ in range(n)]
c = [[0 for _ in range(5)] for _ in range(n)]
section = input("Enter which section you want (a/b/c): ").lower()
row = int(input("Enter row number: "))
column = int(input("Enter column number: "))
seat = f"{section}[{row}][{column}]"
print("Selected seat:", seat)
if section == 'a':
    if 0 <= row < n and 0 <= column < 5:
        a[row][column] = "*"
    else:
        print("Invalid seat in section a.")
elif section == 'b':
    if 0 <= row < n and 0 <= column < 10:
        b[row][column] = "*"
    else:
        print("Invalid seat in section b.")
elif section == 'c':
    if 0 <= row < n and 0 <= column < 5:
        c[row][column] = "*"
    else:
        print("Invalid seat in section c.")
else:
    print("Choose the correct section (a/b/c).")
print("\nSeating Layout:")
for i in range(n):
    rowa = "".join(str(v) for v in a[i])
    rowb = "".join(str(v) for v in b[i])
    rowc = "".join(str(v) for v in c[i])
    print(f"{rowa} {rowb} {rowc}")
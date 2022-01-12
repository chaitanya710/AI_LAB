def clean(floor, row, col):
    i, j, p, q = row, col, len(floor), len(floor[0])
    Right = Down = True
    cleaned = [not any(fl) for fl in floor]
    while not all(cleaned):
        while any(floor[i]):
            print_floor(floor, i, j)
            if floor[i][j]:
                floor[i][j] = 0
                print_floor(floor, i, j)
            if not any(floor[i]):
                cleaned[i] = True
                break
            if j == q - 1:
                j -= 1
                Right = False
            elif j == 0:
                j += 1
                Right = True
            else:
                j += 1 if Right else -1
        if all(cleaned):
            break
        if i == p - 1:
            i -= 1
            Down = False
        elif i == 0:
            i += 1
            Down = True
        else:
            i += 1 if Down else -1
        if cleaned[i]:
            print_floor(floor, i, j)
        
def print_floor(floor, row, col): # row, col represent the current vacuum cleaner position
    for m in range(len(floor)):
        for n in range(len(floor[m])):
            if m == row and n == col:
                print(f" >{floor[m][n]}< ", end = '')
            else:
                print(f"  {floor[m][n]}  ", end = '')
        print(end = '\n')
    print(end = '\n')
m = int(input("Enter the no of rows: 01"))
n = int(input("Enter the no of columns: "))
floor = []
for i in range(m):
  row_tile = [0]*n
  print("Enter the status of row: "+(str(i+1)))
  for j in range(n):
    s = int(input())
    row_tile.append(s)
  floor.append(row_tile)

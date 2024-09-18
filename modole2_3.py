my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
c = 0

while c < len(my_list):
    num = my_list[c]
    c = c + 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif c == len(my_list):
        print(num)
    else:
        print(num)
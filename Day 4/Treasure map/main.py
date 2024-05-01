row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

treasure_map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

position = input('Where do you want to put the treasure? ')

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

treasure_map[vertical][horizontal] = "X"
print(f'{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}')

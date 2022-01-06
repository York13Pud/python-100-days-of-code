# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Split the position variable into a list
position_split = list(position)

# Use each object in the list and convert them to int's. For each one, deduct 1.
position_x = int(position_split[0])-1
position_y = int(position_split[1])-1

# Print out the map
map[position_y][position_x] = "X"

print(f"{row1}\n{row2}\n{row3}")

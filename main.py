months = [
['January', 31],
['February', 28],
['March', 31],
['April', 30],
['May', 31],
['June', 30],
['July', 31],
['August',31],
['September', 30],
['October', 31],
['November', 30],
['December', 31] ]

table = {2019: []}
for i in range(12): #this loop creates the
    print(str(months[i,0]))
    table[2019] = months[i,0] #table[months[i][0]] = list(range(months[i][1]))

print(table)
print(range(0,30))
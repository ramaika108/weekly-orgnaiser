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

table = {}

sellected_day = ('January',1)

for i in range(12): #this loop creates the
    table[months[i][0]] = list(range(1,months[i][1]+1)) #table[months[i][0]] = list(range(months[i][1]))



def create_task():
    #table['January'][-1] = 'last var' 
    #table[sellected_day[0]][sellected_day[1]] = 'last var' 
    print(table[sellected_day[0]][sellected_day[1]]-1)

create_task()

#print(table)

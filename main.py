# Put your function here
def timesTable(num):
    table = []
    for i in range(1, num + 1):
        row = []
        for j in range(1, num + 1):
            row.append (i * j)
        table.append (row)
        
    return table
            

# testing
num = int(input())
print(timesTable(num))

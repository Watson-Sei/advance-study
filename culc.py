import csv 

t = {}

with open ('04data.csv', 'r',encoding='cp932') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row[2] in t:
            t[row[2]]['point'] = t[row[2]]['point'] + int(row[3])
            t[row[2]]['point-second'] = t[row[2]]['point-second'] + int(row[4])
            t[row[2]]['count'] = t[row[2]]['count'] + 1
        else:
            t[row[2]] = {'point':int(row[3]), 'point-second':int(row[4]),'count':1}
 
change = sorted(t)
for i in change:
    print(i, t[i]['point'] / t[i]['count'], t[i]['point-second'] / t[i]['count'])
    
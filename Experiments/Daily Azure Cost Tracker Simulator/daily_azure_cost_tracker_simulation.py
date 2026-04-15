import csv 

filename = 'costs.csv'

with open(filename,'r') as f:

    reader = csv.reader(f)
    data = list(reader)
    headers = data[0]
    
output =  ['Date','ServiceName','Cost']


for header in headers:

    if header in output:

        print(header,end='\t\t')

print()
for line in data[1:4]:

    cost = line[4]
    servicename=line[1]
    date=line[0]
    message = f'{date}\t{servicename:20}\t{cost}'

    print(message)

    
    


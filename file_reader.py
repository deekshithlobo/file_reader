'''def printer(data):
    for i in data:
        print(i,end=" ")

r = open("data.txt",'r')
heading = r.readline().split('|')
printer(heading)
ls = r.readlines()
for ele in ls:
    printer(ele.split('|'))'''

r = open("data.txt",'r')
heading = r.readline().strip().split('|')
s = r.readlines()
ls =[]
for ele in s:
    ls.append(ele.split('|'))
for ele in ls:
    print(ele)
''' extracted data could be converted in to JSON files and also could be validated
change formats etc '''

fh = open('output4.txt','w')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for i in list:
    sum += i

fh.write("The Average of the list element is : " + str( sum / len(list))+'\n')
fh.write("------------------------------------------------------")
fh.close
# creating an emoty list 
my_list = [] 

#Append 10, 20 ,30, 40

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insering 25 at position 2
my_list.insert(1, 15)

# Extendin with another List

my_list.extend([50, 60, 70])

#Removin the last element
my_list.pop()

#sorting the list in  ascending order
my_list.sort()

#Finding and printing the index of 30
indx_30 = my_list.index(30)
print("Index of 30:", indx_30)

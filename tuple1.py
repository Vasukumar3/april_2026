# tuple_1 = ()
# print(tuple_1)
# print(type(tuple_1))


# tuple_2 = (1,2,5.7,"pythonlife",True,(1,2,3),25,25,25)
# print(tuple_2)
# print(type(tuple_2))


# tuple_3 = tuple()
# print(tuple_3)
# print(type(tuple_3))


# a=b=c=d = 1
# print(a)
# print(b)
# print(c)
# print(d)


# a = 1,23,4,5.7,True,"pythonlife"
# print(a)

# a,b,c,d = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)


#swapping of two variables without using third variable
# a = 10
# b = 20
# a,b = b,a
# a = a+b
# b = a-b
# a = a-b
# print(a)#20
# print(b)#10

# person_info = ('John', 25, 'Male')
# print(len(person_info))


# tuple_2 = (1,2,3,4,"pythonlife",True,5.7,(1,2,3),[1,2,3],25,25,25,25,25,0,False)
# print(tuple_2.count(1))

# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# print(tuple1+tuple2)


# tuple1 = (1, 2, 3)
# print(tuple1*3)


# sample = (1,2,3,4)
# print(sample[2])
# print(sample[-2])


# sample = (1,2,3,4)
# #seq[s:s:s]
# print(sample[1:3])
# print(sample[::-1])



# numbers = (1, 2, 3, 4, 3, 5,"pythonlife")
# index_of_three = numbers.index("pythonlife")
# print(index_of_three)



# fruits = ('apple', 'banana', 'orange')
# is_apple_present = 'apple' in fruits
# print(is_apple_present)


# sample = ()
# print(all(sample))


# Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples. It should then iterate over this list to print out each item along with its price. Finally, calculate and print the total cost of all the items

# Item		Price
# --------------------
# Apple		99.00
# Banana	99.00
# Milk		49.00
# --------------------
# Total		247.00


# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# print(f"Item\tPrice")
# print("-"*25)
# total = 0
# for i,j in items:
#     print(f"{i}\t{j}")
#     total += j
# print("-"*25)
# print(f"Total\t{total}")

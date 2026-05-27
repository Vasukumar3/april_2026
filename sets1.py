# sample = {1,}
# print(sample)
# print(type(sample))

# sample_2 = set()
# print(sample_2)
# print(type(sample_2))


# sample = {"pythonlife","pythonlife",389,5.7,87,("sample","sets",35)}
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample.add((1,2,3,4))
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample.clear()
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample_2 = sample.copy()
# sample_2.add("hello everyone")
# print(sample_2)

# print(sample)


# sample = {"pythonlife",389,5.7,87}
# obj = sample.pop()
# print(sample)
# print(obj)

# sample = {"pythonlife",389,5.7,87}
# new = {1,2,3,4,5,6,7,"pythonlife"}
# sample.update(new)
# print(sample)









######################## may 14 2026 ##################

# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.union(set_2)
# print(set_3)




# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.intersection(set_2)
# print(set_3)



# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.symmetric_difference(set_2)
# print(set_3)



# set_1 = {1,2,3,4,5}
# set_2 = {6,7,8,9,1}
# set_3 = set_1.isdisjoint(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.difference(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,2,3,4}
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))


# voter_data = {"vasu","kiran","raju","kumar",}
# voter_data_2 = {"vasu","kiran","raju","kumar","bhanu","bharat",}
# print(voter_data_2.issuperset(voter_data))
# print(voter_data.issubset(voter_data_2))



# set_1 = {1,2,3,4}
# set_1.add(5)
# print(set_1)

# set_1 = {1,2,3,4}
# set_2 = frozenset(set_1)
# print(set_1.union(set_2))
# set_2.add(5)
# print(set_2)


#union
#intersection
#difference
#symmetric diff
#isdisjoint
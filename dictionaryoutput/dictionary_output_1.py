# Program 1
# Comments are for dictionary comprehensions

#doubt in range from where it start and where it ends:
# Ans range starts from 0 and ends at n-1

# def checkrange(n):
#     for i in range(n):
#         print(i)
#
# checkrange(5)



a = {i:  i * i for i in range(6)}
print(type(a))
print (a)

# Program 2
# fromkeys creates new dictionary and intiates with default key and value provided

a ={}
b={}
a.fromkeys(['a', 'b', 'c', 'd'], 98)
b.fromkeys(['a'], 98)

print (a)
print (b)

# Program 3
# in same continuation with example 2 but till the time fromkeys is initialzed till that time it wont work.

a ={}
dict = a.fromkeys(['a', 'b', 'c', 'd'], 98)
print (a)
print (dict)

# Program 4
# O/P - True , False -
# Explanation - till time all of them areiterables then everything is fine.

a = {}
b = a.fromkeys([1, False, 3], 'True')
print (all(a))
print (all(b))


# Program 5
# O/P - False
# Explanation - If both dictionary have same values then true else false.

a = {'geeks' : 1, 'gfg' : 2}
b = {'geeks' : 2, 'gfg' : 1}
print (a == b)


# Program 6
# O/P - True
# Explanation - If value exists then it would be true

dictionary = {"geek":10, "for":45, "geeks": 90}
print("geek" in dictionary)

# Program 7
# O/P - del deletes entire dictionary
# Explanation - If both dictionary have same values then true else false.

dictionary ={1:"geek", 2:"for", 3:"geeks"}
del dictionary

# Program 8
# O/P - 4
# Explanation - dictionary a has 2 key-value pairs

a = {}
a[1] = 1
a['1'] = 2
a[1]= a[1]+1
count = 0
for i in a:
    count += a[i]
print(count)



# Program 9
# O/P - 2
# Explanation - individual keys can be deleted and processed back and forward

test = {1:'A', 2:'B', 3:'C'}
del test[1]
test[1] = 'D'
del test[2]
print(len(test))




# Program 10
# O/P - raises an exception
# Explanation - : It doesn't make sense to slice dictionary

Python = {'Naveen': 100, 'Kumar': 200, 'Tamrakar': 300}
Python ['Naveen':'Tamrakar']

# NOTE: a list of mutable data structure can't be used as key.


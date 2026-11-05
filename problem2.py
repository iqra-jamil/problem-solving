# Given an integer , n, and n  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .hash(t)

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.

# Output Format

# Print the result of hash(t) .



# what is hast(t)

# given integr n (number of elemnts in the tuple)
# given n spce sperated integres as input (create a tuple)(describing the elements in tuple t)
# compute and print the result of hash (t)
my_list=[]
n=int(input("enter the number of elemnts"))
n_space=input("enter elements").split(" ")
for integer in n_space:
    my_list.append(int(integer)) # could apply map 
t=tuple(my_list)
print(hash(t))





#NOTES 

# Hash Function in Python

# • hash() converts a hashable object into an integer called a hash value.

# • Python uses hash values to find data efficiently in dictionaries and sets.

# • Hashing helps Python locate keys quickly.

# • Immutable objects like integers, strings, and tuples (if their elements are hashable) can be hashed.

# • Mutable objects like lists and dictionaries cannot be hashed.

# • Two different objects can have the same hash. This is called a hash collision.

# • Hash values of strings may change between different Python runs.

# • Hashing is not encryption.
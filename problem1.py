# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print:      Print the list.
# remove e:   Delete the first occurrence of integer .
# append e:   Insert integer  at the end of the list.
# sort:       Sort the list.
# pop:        Pop the last element from the list.
# reverse:    Reverse the li


# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
my_list=[]
N=int(input("number of commands"))

for counter in range(1,N+1):
  cmd=input("Enter the command with values i and e").split()

  if cmd[0]=='insert':
     
     i=int(cmd[1])
     e=int(cmd[2])
     my_list.insert(i,e)
  elif cmd[0]=="print":
     print(my_list)
  elif cmd[0]=='remove':
     e=int(cmd[1])
     my_list.remove(e)
  elif cmd[0]=='append':
    e=int(cmd[1])
    my_list.append(e)
  elif cmd[0]=='sort':
     my_list.sort()
  elif cmd[0]=='pop':
    my_list.pop()
  elif cmd[0]=='reverse':
     my_list.reverse()


#keep in mind to solve a problem

# 1. What information am I receiving?
# 2. What am I expected to do with that information?
# 3. What should the output be?
# Don't immediately start writing code. First, understand the input format and expected behavior.

# That's how you develop problem-solving skills.
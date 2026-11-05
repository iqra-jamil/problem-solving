# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string s.
# Constraints
# 0<len(s)<=1000

# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# s="HackerRank.com"
s=input("")
m_string=""
def swap_case(s):
    global m_string
    for char in s:
        if char.islower():
           m_string+="".join(char.upper())

        else : #isupper()
            m_string+="".join(char.lower())

    return m_string
print(swap_case(s))

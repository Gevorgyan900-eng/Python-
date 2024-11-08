# Question:1
#  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

L =[]

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        L.append(str(i))

print(",".join(L))

# Question: 2
#  Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program:
#  8 Then, the output should be: 40320


def  fact(x):
    if x ==0:
        return 1
    else:
        return x*fact(x-1)
    

x=int(input("Write a number"))

print(fact(x))


# Question: 3 
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#  Suppose the following input is supplied to the program:
#  8 Then, the output should be: 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def abr(n):
    d =dict()
    for i in range(1,n+1):
        d[i] = i*i
    return d

n =int(input("write a number"))
result =abr(n)
print(result)


# Question: 4
#  A website requires the users to input username and password to register.
#  Write a program to check the validity of password input by users. 
# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria. Passwords that match the criteria are to be printed,
# each separated by a comma. Example 
# If the following passwords are given
# as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

# import re
# value =[]
# items =[x for x in input().split(",")]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))




import re

# Configuration for password rules
MIN_LENGTH = 6
MAX_LENGTH = 12
REQUIRED_SPECIAL_CHARS = "$#@"
REQUIRED_LOWERCASE = True
REQUIRED_UPPERCASE = True
REQUIRED_DIGIT = True
REQUIRED_SPECIAL = True

def validate_password(password):
    """Check if the password meets all specified requirements."""
    # Check length
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False
    
    # Conditional checks based on configurations
    if REQUIRED_LOWERCASE and not re.search("[a-z]", password):
        return False
    if REQUIRED_UPPERCASE and not re.search("[A-Z]", password):
        return False
    if REQUIRED_DIGIT and not re.search("[0-9]", password):
        return False
    if REQUIRED_SPECIAL and not re.search(f"[{re.escape(REQUIRED_SPECIAL_CHARS)}]", password):
        return False
    if re.search(r"\s", password):  # No whitespace allowed
        return False

    return True

# Read comma-separated passwords and validate each
passwords = input("Enter passwords (comma-separated): ").split(',')
valid_passwords = [pwd for pwd in passwords if validate_password(pwd.strip())]

# Output valid passwords
print("Valid passwords:", ",".join(valid_passwords))








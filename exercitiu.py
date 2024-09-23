def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# Your previous Plain Text content is preserved below:

# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.

# Enjoy your interview!




# > You're given a list of cities and their corresponding populations. Write a program to output a random city from the list. The probability of each city to appear in the output should be proportional to its population. Assume the program will be repeatedly called many times. 


# Example: 

# NY: 7.(3)M
# SF: 5M
# LA: 8M
# -------
# 1k - 
# NY = 7.3/(SUM)
# SF = 5/SUM


# Example2: 

# NY: 7, SF: 1

# list = [NY] *7 + [SF]
# random (len(list))
# [0, 7.3/20, (7.3+5)/20.3, ]
# n = randn()


# ---------------
(name,pop)
n = len(city_list)
def get_random_city(city_list, chosen_city):
    limits = [0]
    norm = sum([x[1] for x in city_list]) O(n)
    
    cum_sum = 0
    for city in city_list:
        cum_sum +=city[1]
        limits.append(cum_sum/norm) # [0, 7.3/20, (7.3+5)/20.3, ]
    O(n)
    
    pick = rand.ramdom() #0-1
    i = 0 
    while limits[i]<pick:
        i++

[0, 3 ,  5, 10]

pick = 4

    li = 0
    ri = len(limits)

    while (li<ri):
        mi = (li+ri)//2 #  2

        if (pick) < limits[mi]:
            li = li #1
            ri = mi #2
        else:
            li =mi+1  #1 
            ri = ri #3
    return city_list[mi][0]

    return city_list[i][0]
    





# Given a string representing an arithmetic expression with only addition and 
# multiplication operators, return the result of the calculation.
# For example, for "28818*3+400100120", return 10
    
      +
    *      *
   1  2    3  4

1. tokenize
number / operator
exp_list = [(2,'number'),(*, operator), (3,'number') , (+)]
[3, +,  5,  +,  5, + 4 *  5  * 6 * 7 +]


currnt_sum, op, next_val, next_op

if *
   current_val =  current_val * next
elif +
   
current_sum = 0
c_prod 

while
 




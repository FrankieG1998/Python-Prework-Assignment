#Question 1
def hello_name(user_name):
    print("hello_"+user_name)
user_name = input('hello_USERNAME: ')
hello_name(user_name)

#Question 2
def first_odds():
    odd_numbers = list(range(1,100,2))
    return odd_numbers

print (first_odds())

#Question 3
def max_num_in_list( a_list ):  
    max = a_list[ 0 ]  
    for a in a_list:  
        if a > max:  
            max = a  
    return max  
print(max_num_in_list([1, 2, 3, 4]))  

#Question 4
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True
    else:
       return False
print(is_leap_year(2020))
print(is_leap_year(2021))

#Question 5
def is_Consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list1 = [2, 3, 4, 5, 6, 7]
a_list2 = [1, 2, 4, 5]
print(is_Consecutive(a_list1))
print(is_Consecutive(a_list2))

# ITERATORS ====================================================================

# FOR LOOPS ====================================================================
print('4 For Loops ===========================================================')

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

# sum of all ints
sum = 0
for num in l:
    sum = sum + num
print(f"Sum using list: {sum}")

print('15 Using Range Generator')

for num in range(5): #grabs 5 numbers in l list
    print(l[num])

sum = 0
for num in range(len(l)):
    sum = sum + l[num]
print(f"Sum using Range Generator: {sum}")

#===============================================================================

print('25 Run Times')

run_times = int(input('How many times would you like to run the program? '))
for num in range(run_times):
    print(f"Run: {num+1}")

# ==============================================================================
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

print('32 Using my_dict')

for item in my_dict.items():
    key, value = item
    print(f"key is {key}, value is {value}")

for key, value in my_dict.items(): #using unpacking
    print(f"key is {key}, value is {value}")

# LISTS COMPREHENSION ==========================================================
print('45 List Comprehension =================================================')

# generate a random integer between 1 and 1000
from random import randint, choice
from string import ascii_lowercase

l1 = []
for num in range(100):
    l1.append(randint(1,100))
print(l1)

print('55 Using List Comp.')

l2 = [randint(1,100) for num in range(100)] #list comp.
print(l2)

l3 = [choice(ascii_lowercase) for num in range(100)]
print(l3)

# WHILE LOOPS ==================================================================
print('While Loops ===========================================================')

truth_condition = True

while truth_condition:
    print('hello')
    break

i = 0
while i < 10:
    print(i)
    i += 1

rand_i = [randint(1,100) for num in range(1000)]
num_to_search = 20
while i < len(rand_i):
    if rand_i[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
    i += 1
    # can add a break after if block to break after first instance

# ENUMERATE FUNCTION ===========================================================
print('Enumerate Function ====================================================')

enum_i = [randint(1,100) for num in range(1000)]
num_to_find = 20
for index, num in enumerate(enum_i):
    if num == num_to_find:
        print(f"{num_to_find} found at index {index}")
        break

# REAL WORLD WHILE EXAMPLE =====================================================
print('While Example =========================================================')

while True:
    print('Please choose an option from the list below')
    print('Press 1 for option 1')
    print('Press 2 for option 2')
    print('Press 3 to quit')
    selection = input('Enter your choice -> ')
    if int(selection) == 3:
        break

# ZIP FUNCTION =================================================================
print('Zip Function ==========================================================')

list_1 = ['.py', '.js', '.rb', '.java', '.c']
list_2 = ['python', 'javascript', 'ruby', 'java', 'c']

tupled_list = list(zip(list_2, list_1))
# without casting the object will not print, only show the memory location
print(tupled_list)

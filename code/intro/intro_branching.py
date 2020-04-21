# Boolean, Conditions, If/Else =================================================

print('Welcome to the calculator')
print('-'*30)
choice = input('Choose 1 to multiple, Choose 2 to divide ')
if choice == '1' or choice == '2':
    num1 = int(input('Enter your first number-> '))
    num2 = int(input('Enter your second number-> '))
    if choice == '1':
        print(f'{num1} multiplied by {num2} is: {num1*num2}')
    else:
        print(f'{num1} divided by {num2} is: {num1/num2}')
else:
    print('You have made an invalid selection')

# ==============================================================================

made_payment = True
pay = 'Please submit your montly payment'
hello = 'Welcome to your homepage'

if not made_payment:
    print(pay)
else:
    print(hello)

print(pay) if not made_payment else print(hello)
print(hello) if made_payment else print(pay)

# ==============================================================================

i = 5
j = 10
k = 30

if i < j and i < k:
    print('i is less than j and k')
elif i == j or i ==k:
    print('i is equal to eith j or k')
elif i == j and i ==k:
    print('i is equal to j and k')
else:
    print('something else')

# ==============================================================================

course1 = 'python'
course2 = 'java'
python = 'enrolled in a python course'
java = 'enrolled in a java course'

print(python) if course1 == 'python' else print(java)
print(java) if not course2 == 'python' else print(python)

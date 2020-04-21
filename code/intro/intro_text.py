# STRINGS ======================================================================
print('(String2) Hello World') # use double quotes when using '

print("""(Triple Quote4) THIS WILL
(Triple Quote4) ALLOW MULTI
(Triple Quote4) LINE STRINGS""") #very unique uses

print('(Escape Character8) Hello world I\'m using single quotes')
#\ escape character. ignores special properties

#  VARIABLES ===================================================================

my_message = '(Variable13) Hello World'
other_message = '(Variable14) Other Message'
print(my_message)
print(other_message)

# Python runs top to bottom. Always intrdouce variables prior to calling

# STRINGS (Concatenation, Indexing, Slicing) ===================================

print("(Concat22)The stock price for this is:"+" "+"$1000.")
# Concatenation combines two STRINGS

price = '$1000.'
print('(Concat w/ var26) The price for this is:'+' '+price)

name = 'Interstellar'
print('(Index29) ' + name[0])
# index finds index of character that is called upon

print('(Slice32) ' + name[0:5])
# starts at index 1 and stops at index 5, showing 'Inter'
print('(Slice34) ' + name[5:])
#  starts at 5 and goes to the end of the string. showing 'stellar'
nums ="0123456789"
print('(Slice37 )' + nums[2:6:2])
# third number is step size, will output 24

# STRING METHODS ===============================================================

greeting = "hello"
user = 'conor'
message = 'Welcome to Algorithms'
languages = ['Python', 'Ruby', 'Javascript']
print('(Methods45)',len(message))
# len() gives you length
print('(Methods47)', type(user))
# type gives you the type of object
print('(Methods49)', user.capitalize())
# capitalizes user variable
print('(Methods51)', dir(user))
# show methods avail
print('(Methods53)', message.strip().lower())
# removes whitespace, and chains lowercase function
print('(Methods55)', message.find('to'))
# find index of beginning of 'to'
print('(Methods57)', message.split())
# returns all strings in a list. splits based on whitespace
print('(Methods59)', '-'.join(languages))
# joins a list of strings

# IMPORT STRINGS ===============================================================

import string
# imported letters a-z
print(string.ascii_lowercase)
# this lowercases all letters in string that are a-z

# PRINT FORMATTING =============================================================

stock_price = '$1000'
print("(Format73) Today's stock price for google is: {}".format(stock_price))
print(f"(Format74) Today's stock price for google is: {stock_price}")
# string interpolation needs a f at the beginnin gof a string
today_price = '$1000'
yesterday_price = '$1100'
print(f"""(Format78) Today's Price: {today_price}.
           Yesterday's Price: {yesterday_price}""")

# SPECIAL CHARACTERS ===========================================================

# \ - escape character
# \t - inputs a tab
# \n - specifys new line within the string

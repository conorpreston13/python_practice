# COMPOUND DATA TYPES ==========================================================
# "Collections"

# LISTS ========================================================================
print('LISTS =================================================================')
print([1, 2, 'Conor', None, False])
my_data = [1, 2, 'Conor', None, False]
# print(type(my_data))
# print(my_data[2])

my_num_list = [13, 82, 32, 47, 57, 642, 7785, 8, 1023, 1]
my_str_list = ['conor', 'preston', 'python']

print(f"Ints: {my_num_list}")
print(f"Strings: {my_str_list}")

print("16 Sorting:")
# sort as a function
sorted_num = sorted(my_num_list)
print(f"(Sort Function 19)Sorted Ints: {sorted_num}")

# sort as a method
my_num_list.sort()
print(f"(Sort Method 23)Sorted Ints: {my_num_list}")

print('25 Finding Info:')

print('Physics' in my_str_list) #checks if 'Physics' is in list
print('python' in my_str_list)
print(len(my_str_list)) # length
print(min(my_num_list)) # min value
print(max(my_num_list)) # max value
print(dir(my_num_list)) #gives methods available
print(my_num_list.count(13))

print('35 Adding/Removing Info:')

my_num_list.append(1313) # append add to end of list
print(my_num_list)

my_num_list.insert(3, 10000) # insert add to anywhere of list
print(my_num_list)

my_new_list = ['Hello', "Who", 'What']
my_str_list.extend(my_new_list) # extend add new list to end of first list
print(my_str_list)

my_str_list.remove('preston') #removes given vlue
print(my_str_list)

my_str_list.pop() #removes last value (will return removed value if printed)
print(my_str_list)

print('54 Sublists')

print(my_num_list[0:4]) #slice returns values at indicies (index 4 not included)
print(my_num_list[5:])
print(my_num_list[::])
print(my_num_list[::2]) #steps values by two

print('61 For Loop Iteration:')

for item in my_num_list:
    print(item)

# Dictionaries =================================================================
print('Dictionaries ==========================================================')

my_dict = {'name': 'Conor', 'course': 'Python'}

phone_dict = {
                'conor': '555-555-5555',
                'mom': '444-444-4444',
                'dad': '333-333-3333'
             }

word_dict = {
                'a':
                    {
                    'apple': 'round red fruit, grown on trees',
                    'ant': 'strong insect with six legs'
                    },
                'b':
                    {
                    'bad': 'of poor or low quality',
                    'business': 'place of work or service'
                    }
            }

print('90 Methods')

print(word_dict['a']) #returns values associated with 'a' key
print(word_dict['b']['business'])

print(my_dict.get('name')) #get returns value of given key

my_dict['job'] = 'python programmer' #adds key and value (can also mutate)
print(my_dict)

print(my_dict.keys()) #returns all keys
print(my_dict.values()) #returns all values
print(my_dict.items()) #returns all pairs (returns tuples)

print('104 For Loop Iteration')

for k, v in my_dict.items():
    print(k,v)

# Tuples =======================================================================
print('Tuples ================================================================')
# immutable, cannot change value

my_rand_tuple = ('first', 1, 7, 6, 4, 5, 8, 'hi there', 2, 3, 1, 5, 2, 1, 9, 10)
my_tuple = ('first value', 'second_value', 'third_value')

print('116 Methods')

print(dir(my_rand_tuple)) #returns available methods

first_var, second_var, third_var = my_tuple #tuple unpacking for use
print(third_var)

print('first' in my_rand_tuple) #looks to see if value is present

for item in my_rand_tuple:
    print(item)

# Sets =========================================================================
print('Sets ==================================================================')
# sets do not allow duplicate values. No ordering, no indexing
my_set = {1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 'python', 6}

print(my_set) #prints random order with no duplicates

my_setlist = [1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 6, 'python', 'java']
print(my_setlist)
my_set = set(my_setlist) #casts my setlist to a set
print(my_set)

print('140 Finding Info')

print('java' in my_set)

print('144 Set Optimization')

programming_set = {'java', 'ruby', 'javascript', 'python', 'c'}
print(my_set.intersection(programming_set)) #gives common elements
print(my_set.union(programming_set)) #returns all elements between two sets
print(my_set.difference(programming_set)) #returns all non common elements
print(programming_set.difference(my_set)) #returns all non common elements

print('152 For Loop Iteration')

for item in my_set:
    print(item)

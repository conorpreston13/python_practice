# FUNCTIONS ====================================================================

def get_input_from_user():
    return input('Enter your response here -> ')

print("Welcome to the program, what is your name?")
name_result = get_input_from_user()

print("What did you think of the food you ate today?")
food_result = get_input_from_user()

print("What tv shoe ending did you dislike the most ever?")
show_result = get_input_from_user()

print(f"To summarize,: your name is {name_result. capitalize()}, \
you ate {food_result} food today and hate the ending \
of {show_result.upper()}")

# ===================================

def func_0(start_num): #start_num is local to these functions
    start_num += 1 #integers are immutable
    return func_1(start_num)

def func_1(start_num):
    start_num += 1
    return start_num

start_num = 1
print(f"start_num\t->{start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t->{finish_num}")
print(f"start_num\t->{start_num}")

# ## if changed from integers to lists, the start_num variable mutates
# ## see example below with integers canged to lists

# def func_0(start_num):
#     start_num[0] += 1
#     return func_1(start_num)
#
# def func_1(start_num):
#     start_num[0] += 1
#     return start_num
#
# start_num = [1]
# print(f"start_num\t->{start_num}")
# finish_num = func_0(start_num)
# print(f"calc'd_num\t->{finish_num}")
# print(f"start_num\t->{start_num}")

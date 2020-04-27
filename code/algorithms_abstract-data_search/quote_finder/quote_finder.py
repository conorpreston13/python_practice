from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['example1.com', 'example2.com', 'example3.com', 'example4.com', 'example5.com']

quotes = ['My name is Conor Preston', 'python is fun',
          'we just got a new fridge', 'snickers is a good cat']

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

# def generate_quotes(length_of_quote):
#     return ''.join(choice(letters) for i in range(length_of_quote))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def generate_records(length_of_name, list_of_domains, total_records, list_of_quotes):
    with open('data.txt', 'w') as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+'@'+get_domain(list_of_domains)
            value = get_quotes(quotes)
            to_write.write(key + ':' + value + '\n')
        to_write.write('hello@example.com:Hello how are you')
        to_write.write('what@example.com:What is going on')

generate_records(10, list_of_domains, 100000, quotes)

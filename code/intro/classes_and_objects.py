# CLASSES AND OBJECTS ==========================================================
# everything in python is an object (strings, integers, lists, dicts, etc.)
# functions associated with instances of objects are known as Methods

class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in {course} course.")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} course not found")

    def find_in_file(self, filename):
        with open(file_name) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return 'Record already exists'
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, 'a+') as to_write:
                to_write.write(record_to_add+'\n')
            return 'Record Added'

    @staticmethod
    def prep_record(line):
        line = line.split(':')
        first_name, last_name = line[0].split(',')
        course_details = line[1].rstrip().split(',')
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name+','+last_name
        courses = ','.join(courses)
        return full_name+':'+courses

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}',\
'{self.courses}')"

    def __str__(self):
        return f"First Name: {self.first_name.capitalize()}\nLast name: \
{self.last_name.capitalize()}\nCourses: \
{', '.join(map(str.capitalize, self.courses))}"

# courses_1 = ['python', 'ruby', 'javascript']
# courses_2 = ['c', 'c++', 'php']

conor = Student('conor', 'preston', ['python', 'ruby', 'javascript'])
# john = Student('john', 'doe', courses_2)

# conor.add_course('python')
# conor.add_course('c')
# conor.remove_course('ruby')
# conor.remove_course('django')
# print(conor.first_name, conor.last_name, conor.courses)
# print(john.first_name, john.last_name, john.courses)
# print(conor)
# print(dir(conor))
# print(conor.__dict__)
# print(len(conor))
# print(repr(conor))
file_name = 'data.txt'

# print(conor.find_in_file(file_name))
# print(conor.add_to_file(file_name))

joe = Student('john', 'schmoe', ['python', 'ruby', 'java'])
# print(joe.find_in_file(file_name))
# print(joe.add_to_file(file_name))

# INHERITENCE ==================================================================

class StudentAthelete(Student):

    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)
        self.sport = sport



jane = StudentAthelete('jane', 'doe', ['python'], 'hockey')
print(jane.sport)
# print(help(jane))

print(isinstance(jane, StudentAthelete))

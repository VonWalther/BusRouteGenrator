# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random

maxStudents = 200
gridSize = 200
xyFavoring = 0.5
name_file = "names.txt"
name_output_file = "gridCity.txt"


# Ask the User how many students need bussing.
def get_number_of_students():
    print("How many students?")
    num_students = input("-->")
    if num_students == "":
        s_num = random.randint(1, maxStudents)  # If the user enter nothing a random number of students is created.
    else:
        s_num = int(num_students)
    return s_num


# Create a list student addresses, an uniques one for each student.
def assign_student_housing(num):
    housing = []
    name_list = read_in_names(name_file)
    for i in range(num):
        # Create the two types of grid coordinates need, on the 50s, and the other on the block.
        address = get_address_pair()
        address = random.choice(name_list).strip() + " " + address
        housing.append(address)

    return housing


# Create Text File Output of Student Housing
def create_data_file(h_list, output_name=name_output_file):
    out = open(output_name, "w", encoding="utf-8")
    for i in range(2):
        address = get_address_pair()
        out.write(address + '\n')
    for i in h_list:
        out.write(i + '\n')
    out.close()
    print(h_list)

# Returns an address pair in Grid City
def get_address_pair():
    num_street = random.randrange(0, gridSize, 50)
    num_address: int = random.randint(0, gridSize)
    x_or_y = random.random()
    #
    if x_or_y >= xyFavoring:
        address = str(num_address) + " " + str(num_street)
    else:
        address = str(num_street) + " " + str(num_address)
    return address

# Read in Text File of Names in to Name List
def read_in_names(f_url):
    with open(f_url) as n_file:
        lines = n_file.readlines()
    n_file.close()
    return lines


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    student_number = get_number_of_students()
    student_housing = assign_student_housing(student_number)
    create_data_file(student_housing)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

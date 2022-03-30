def load_in_grid_file(input_file):
    with open(input_file) as f_grid:
        address = f_grid.readlines()
    return address


def load_in_solution_file(solution_file):
    with open(solution_file) as f_sol:
        solutions = f_sol.readlines()
    return solutions

def draw_grid(block_size = 3):

    line = ""
    for x in range(20*block_size+20+2):
        line += "x"
    print(line)   #Look for better way of doing this.
    for i in range(20):  # Columns
        print('x')
        for j in range(20): # Rows
            print(" #*block_size")
        print('x')
    for x in range(20*block_size+20+2):
        print('x')

if __name__ == '__main__':
    student_address = load_in_grid_file("gridCity.txt")
    address_busbarn = student_address.pop(0)
    address_school = student_address.pop(0)

    draw_grid()

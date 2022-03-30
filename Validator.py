def load_in_grid_file(input_file):
    with open(input_file) as f_grid:
        address = f_grid.readlines()
    return address


def load_in_solution_file(solution_file):
    with open(solution_file) as f_sol:
        solutions = f_sol.readlines()
    return solutions


def build_city_matrix(block_size):
    city_size = 1000
    streets_on_the = 50
    blocks_per_row = int(city_size / streets_on_the)
    matrix_size = block_size * blocks_per_row
    city_matrix = []
    for i in range(matrix_size):  # Row
        city_row = []
        for j in range(matrix_size): # Column
            city_row.append("#")
        city_matrix.append(city_row)
    city_matrix[3][5] = "X"
    return city_matrix


def draw_grid(city_matrix, block_size):
    num_buildings = len(city_matrix[0])
    street_length = num_buildings + int(num_buildings/(block_size-1))s
    street = "." * (street_length)
    top = "/" + "-" * street_length + "\\"
    bottom = "\\" + "-" * street_length + "/"
    # Start Printing the grid
    print(top)
    for i in range(len(city_matrix)):
        # Every third line, print a street.
        if i % (block_size ) == 0:
            line = '|..' + street + "..|\n|"
        else:
            line = "|"
        for j in range(len(city_matrix[i])):
            if j % (block_size) == 0:
                line = line + '..'
            line = line + city_matrix[i][j]
        line = line + "..|"
        print(line)
    print(bottom)


if __name__ == '__main__':
    student_address = load_in_grid_file("gridCity.txt")
    address_busbarn = student_address.pop(0)
    address_school = student_address.pop(0)

    block_size = 2

    the_city = build_city_matrix(block_size)
    draw_grid(the_city, block_size)

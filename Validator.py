def load_in_grid_file(input_file):
    with open(input_file) as f_grid:
        address = f_grid.readlines()
    return address


def load_in_solution_file(solution_file):
    with open(solution_file) as f_sol:
        solutions = f_sol.readlines()
    return solutions


def build_city_matrix(block):
    city_size = 1000
    streets_on_the = 50
    blocks_per_row = int(city_size / streets_on_the)
    matrix_size = block * blocks_per_row
    city_matrix = []
    for i in range(matrix_size):  # Row
        city_row = []
        if i % block == 0:
            # Add a street to matrix.
            for j in range(1 + matrix_size + int(matrix_size/block)):
                city_row.append(".")
            city_matrix.append(city_row)
            city_row = []
        for j in range(matrix_size): # Column
            if j % block == 0:
                city_row.append('.')
            city_row.append("#")
        city_row.append('.')
        city_matrix.append(city_row)

    return city_matrix


def draw_grid(city_matrix):
    num_buildings = len(city_matrix[0])
    street_length = num_buildings
    top = "/" + "-" * (street_length + 2) + "\\"
    bottom = "\\" + "-" * (street_length + 2) + "/"

    print(top)
    for i in range(len(city_matrix)):
        line = "| "
        for j in range(len(city_matrix[i])):
            line = line + city_matrix[i][j]
        line = line + " |"
        print(line)
    print(bottom)



if __name__ == '__main__':
    student_address = load_in_grid_file("gridCity.txt")
    address_busbarn = student_address.pop(0)
    address_school = student_address.pop(0)

    block_size = 2

    the_city = build_city_matrix(block_size)
    draw_grid(the_city)

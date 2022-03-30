def load_in_grid_file(input_file):
    with open(input_file) as f_grid:
        address = f_grid.readlines()
    return address


def load_in_solution_file(solution_file):
    with open(solution_file) as f_sol:
        solutions = f_sol.readlines()
    return solutions


def build_city_matrix(size=200):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("#")
        grid.append(row)
    return grid


def get_grid_coordinates(str_cord):
    string_list = str_cord.split()
    if(string_list[0].isalnum()):
        cord = (int(str_cord[0]),int(str_cord[1]))
    else:
        cord = (int(str_cord[1]),int(str_cord[2]), str_cord[0])

    return cord


def place_location(grid, school, type = 'X'):
    cord = get_grid_coordinates(school)
    print(cord)
    grid[cord[0]][cord[1]] = type

    return grid


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
    print(address_busbarn)
    address_school = student_address.pop(0)

    city_grid = build_city_matrix()
    place_location(city_grid, address_school, 'S')
    place_location(city_grid, address_busbarn, 'B')
    draw_grid(city_grid)

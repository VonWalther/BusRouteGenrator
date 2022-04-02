# ************************************ Utility Functions ********************************************
def load_in_file(input_file):
    with open(input_file) as f_grid:
        string_list = f_grid.readlines()
    return string_list


def strip_empties_from_list(d_list, unwanted):
    output = []
    for el in d_list:
        if el not in (unwanted):
            output.append(el)
    return output

def remove_new_lines(d_list):
    output = []
    for el in d_list:
        output.append(el.replace('\n',''))
    return output

# ************************************ Graphics and Visualisation ************************************
def build_city_matrix(size=1001):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("#")
        grid.append(row)
    return grid


def get_grid_coordinates(str_cord):
    string_list = str_cord.split(" ")
    if string_list[0].isnumeric():
        cord = (int(string_list[0]), int(string_list[1]))
    else:
        cord = (int(string_list[1]), int(string_list[2]), string_list[0])
    return cord


def place_location(grid, data_point, symbol='X'):
    cord = get_grid_coordinates(data_point)
    if symbol == 'X':
        name = str(cord[2])
        grid[cord[0]][cord[1]] = name[0]
    else:
        grid[cord[0]][cord[1]] = symbol

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


# **************************************** Bus Routes Validation *******************************************


if __name__ == '__main__':
    student_address = load_in_file("gridCity_one.txt")
    address_busbarn = student_address.pop(0)
    address_school = student_address.pop(0)
    # print(student_address)

    city_grid = build_city_matrix()
    city_grid = place_location(city_grid, address_school, 'S')
    city_grid = place_location(city_grid, address_busbarn, 'B')
    for student in student_address:
        place_location(city_grid, student)  # Yes I know, abusing mutability here, or maybe above.
    # draw_grid(city_grid)

    # Load in Bus Routs
    bus_routs = load_in_file("gridCityBusses.txt")
    bus_routs = strip_empties_from_list(bus_routs, '\n')
    bus_routs = remove_new_lines(bus_routs)


    print(bus_routs)

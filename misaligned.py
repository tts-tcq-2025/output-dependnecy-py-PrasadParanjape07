
def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    output = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            output.append(f'{i * 5 + j:2} | {major:<6} | {minor:<6}')
    return output
def print_color_map():
    color_map = generate_color_map()
    for line in color_map:
        print(line)
    return len(color_map)
    
if __name__ == "__main__":
    result = print_color_map()
    assert(result == 25)
    print("All is well (maybe!)")



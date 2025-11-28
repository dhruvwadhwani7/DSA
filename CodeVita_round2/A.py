class BuildingSpecs:
    def __init__(self, width, height, min_y, max_y, direction):
        self.width = width
        self.height = height
        self.min_y = min_y
        self.max_y = max_y
        self.direction = direction


class ASCIIHouseMaker:
    def render(self, input_line: str):
        asciiChars = input_line.strip().split()

        building_list = []
        total_width = 0
        global_min_y = 0
        global_max_y = 0

        for chars in asciiChars:
            x_index = chars.find('x')
            length = int(chars[:x_index])
            remaining = chars[x_index + 1:]

            index = 0
            while index < len(remaining) and remaining[index].isdigit():
                index += 1

            height = int(remaining[:index])
            direction = remaining[index]

            if direction in ('L', 'R'):
                final_width = height
                final_height = length
            else:
                final_width = length
                final_height = height

            roof_height = final_width // 2

            if direction == 'D':
                y_min = -(final_height + roof_height)
                y_max = 0
            else:
                y_min = 0
                y_max = final_height + roof_height

            building_list.append(BuildingSpecs(final_width, final_height, y_min, y_max, direction))

            global_min_y = min(global_min_y, y_min)
            global_max_y = max(global_max_y, y_max)
            total_width += final_width

        canvas_height = global_max_y - global_min_y
        canvas = [[" " for _ in range(total_width)] for _ in range(canvas_height + 1)]

        current_x = 0

        for b in building_list:
            width = b.width
            height = b.height
            roof = width // 2
            inverted = b.direction == 'D'

            left_wall = '@'
            right_wall = '&'
            left_roof = '/'
            right_roof = '\\'

            if b.direction in ('L', 'D'):
                left_wall, right_wall = right_wall, left_wall

            if inverted:
                left_roof, right_roof = '\\', '/'

            base_row = global_max_y
            if 0 <= base_row <= canvas_height:
                for k in range(width):
                    canvas[base_row][current_x + k] = '#'

            for i in range(1, height + 1):
                y = -i if inverted else i
                row = global_max_y - y
                if 0 <= row <= canvas_height:
                    canvas[row][current_x] = left_wall
                    canvas[row][current_x + width - 1] = right_wall

            for i in range(roof):
                y_dist = height + 1 + i
                y = -y_dist if inverted else y_dist
                row = global_max_y - y
                if 0 <= row <= canvas_height:
                    canvas[row][current_x + i] = left_roof
                    canvas[row][current_x + width - 1 - i] = right_roof

            current_x += width

        output_lines = []
        for row in canvas:
            output_lines.append("".join(row).rstrip())

        return "\n".join(output_lines)


renderer = ASCIIHouseMaker()
print(renderer.render("6x3U 4x2U 8x4L 2x2H"))
print(renderer.render("4x6R 12x8H 2x6D"))

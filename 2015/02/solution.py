from pathlib import Path

# part 1
def calculate_sqftage(line):
    dimensions = line_to_dimensions(line)
    [l, w, h] = dimensions["unsorted"]
    
    sqft = 0
    # add sqftage for all sides
    sqft += (2*l*w) + (2*w*h) + (2*h*l)
    # add slack (based on area of smallest side)
    sqft += dimensions["sorted"][0] * dimensions["sorted"][1]

    return sqft

# part 2
def calculate_ribbon_length(line):
    # only need the smallest two dimensions, so we need sorted dimensions
    dimensions = line_to_dimensions(line)["sorted"]

    # ribbon wraps around the shortest distance around its sides (i.e. 2 * two smallest sides' area)
    wraparound = (2 * dimensions[0]) + (2 * dimensions[1])
    # bow requires ribbon length equal to volume of present
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    
    return wraparound + bow

# unpacks a line into a dictionary of unsorted and sorted dimensions (reusability+)
def line_to_dimensions(line):
    dimensions = list(map(int, line.split('x')))
    return {
        "unsorted": dimensions,
        "sorted": sorted(dimensions)
    }


f = Path(__file__).with_name("input.txt")
data = f.read_text().splitlines()

sqft_paper = 0
ribbon_length_ft = 0
for line in data:
    sqft_paper += calculate_sqftage(line)
    ribbon_length_ft += calculate_ribbon_length(line)

print(f'The elves need to order {sqft_paper} ft² of wrapping paper.')
print(f'The elves need {ribbon_length_ft} feet of ribbon.')

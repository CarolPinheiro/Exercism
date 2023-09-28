def equilateral(sides):
    unique_sides = set(sides)
    if validate_triangle(sides) == False:
        return False
    return len(unique_sides) == 1 and 0 not in unique_sides


def isosceles(sides):
    unique_sides = set(sides)
    print(unique_sides)
    if validate_triangle(sides) == False:
        return False
    return len(unique_sides) <= 2 and 0 not in unique_sides


def scalene(sides):
    unique_sides = set(sides)

    if validate_triangle(sides) == False:
        return False

    return len(unique_sides) == 3 and 0 not in unique_sides


def validate_triangle(sides):
    result = True
    for idx, side in enumerate(sides):
        if (result == False):
            break
        if idx == 0:
            result = sides[1] + sides[2] > side
        if idx == 1:
            result = sides[0] + sides[2] > side
        if idx == 2:
            result = sides[0] + sides[1] > side
    return result


# Python Tuples
# Tuples store related values together.
# Unlike lists, tuples are immutable.

# 1. Create a tuple containing RGB values
steel_blue = (70, 130, 180)

print(steel_blue)

# 2. Access tuple values using indexes
print(steel_blue[0])
print(steel_blue[1])
print(steel_blue[2])

# 3. Tuples are immutable
# Uncomment the next two lines to see the TypeError.
# steel_blue[0] = 300
# print(steel_blue[0])

# 4. Unpacking a tuple
red, green, blue = steel_blue

print(red)
print(green)
print(blue)

# 5. Store multiple RGB tuples inside a list
color_palette = [
    (70, 130, 180),
    (240, 128, 128),
    (60, 179, 113)
]

# Access the first tuple and unpack its values
red, green, blue = color_palette[0]
print(f"RGB: {red}, {green}, {blue}")

# Access the second tuple and unpack its values
red, green, blue = color_palette[1]
print(f"RGB: {red}, {green}, {blue}")

# Access the third tuple and unpack its values
red, green, blue = color_palette[2]
print(f"RGB: {red}, {green}, {blue}")
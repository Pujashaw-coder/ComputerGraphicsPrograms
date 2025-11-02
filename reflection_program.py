def reflect_point(x, y, axis):
    if axis.lower() == 'x':
        return x, -y
    elif axis.lower() == 'y':
        return -x, y
    elif axis.lower() == 'origin':
        return -x, -y
    else:
        return x, y

# Example
x, y = 4, 5
axis = 'x'
new_x, new_y = reflect_point(x, y, axis)
print(f"Reflected Point about {axis}-axis: ({new_x}, {new_y})")

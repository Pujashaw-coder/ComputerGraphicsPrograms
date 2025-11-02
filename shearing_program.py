def shear_point(x, y, shear_type, shear_factor):
    if shear_type.lower() == 'x':
        x_new = x + shear_factor * y
        y_new = y
    elif shear_type.lower() == 'y':
        x_new = x
        y_new = y + shear_factor * x
    else:
        x_new, y_new = x, y
    return x_new, y_new

# Example
x, y = 2, 3
shear_type = 'x'
shear_factor = 1.5

new_x, new_y = shear_point(x, y, shear_type, shear_factor)
print(f"After {shear_type}-shearing: ({new_x}, {new_y})")

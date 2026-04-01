# Check if two rectangles overlap (given coordinates)
def do_rectangles_overlap(rect1, rect2):
    # Unpack rectangle coordinates
    x1_min, y1_min, x1_max, y1_max = rect1
    x2_min, y2_min, x2_max, y2_max = rect2

    # Check if one rectangle is to the left of the other
    if x1_max <= x2_min or x2_max <= x1_min:
        return False

    # Check if one rectangle is above the other
    if y1_max <= y2_min or y2_max <= y1_min:
        return False

    # If neither of the above conditions are true, the rectangles overlap
    return True
# Example usage
if __name__ == "__main__":
    rect1 = (0, 0, 2, 2)  # (x_min, y_min, x_max, y_max)
    rect2 = (1, 1, 3, 3)
    print(do_rectangles_overlap(rect1, rect2))  # Output: True

    rect3 = (3, 3, 4, 4)
    print(do_rectangles_overlap(rect1, rect3))  # Output: False


# other way to check if two rectangles overlap
def do_overlap(rec1, rec2):
    # rec1 = [x1, y1, x2, y2]
    # rec2 = [x3, y3, x4, y4]
    
    # Check if one rectangle is to the left of the other
    if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
        return False

    # Check if one rectangle is above the other
    if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
        return False

    return True

# Example Usage
rect_a = [0, 0, 2, 2]
rect_b = [1, 1, 3, 3]
print(f"Overlap: {do_overlap(rect_a, rect_b)}") # Output: True

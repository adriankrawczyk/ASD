# Element Insertion
def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        raise ValueError("Invalid position for insertion")
    arr.insert(position, element)
    return arr


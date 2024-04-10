# Element Deletion
def delete_element(arr, position):
    if position < 0 or position >= len(arr):
        raise ValueError("Invalid position for deletion")
    arr.pop(position)
    return arr


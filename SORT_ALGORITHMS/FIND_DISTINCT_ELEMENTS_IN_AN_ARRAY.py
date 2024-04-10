# Find distinct elements in an array
def find_distinct_elements(arr):
    distinct_elements = []
    for x in arr:
        if x not in distinct_elements:
            distinct_elements.append(x)
    return distinct_elements


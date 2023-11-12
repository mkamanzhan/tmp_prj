def divide_chunks(array, size):
    result = []
    for i in range(0, len(array), size):
        result.append(array[i : i + size])
    return result

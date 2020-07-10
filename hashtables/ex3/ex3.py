def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    for array in arrays:
        for i in array:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
    result = [value[0] for value in cache.items() if value[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

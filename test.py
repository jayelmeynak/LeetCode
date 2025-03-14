def pair_sums(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            result.append(arr[i] + arr[j])

    return result


# Пример использования:
arr = [1, 2, 3, 4]
print(pair_sums(arr))  # [3, 4, 5, 5, 6, 7]

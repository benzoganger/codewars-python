def two_sum(numbers, target):
    for n1 in enumerate(numbers):
        for n2 in enumerate(numbers):
            if n1[0] != n2[0]:
                if (n1[1] + n2[1]) == target:
                    return [n1[0], n2[0]]

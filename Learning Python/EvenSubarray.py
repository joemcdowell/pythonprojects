def evenSubarray(numbers, k):
    count = 0
    n = len(numbers)
    mem = set()

    for i in range(n):
        temp = []
        odd = 0
        for j in range(i, n):
            if numbers[j] % 2:
                odd += 1
            temp.append(numbers[j])
            temp2 = tuple(temp)
            if odd <= k and temp2 not in mem:
                count += 1

            mem.add(temp2)

    return count




def evenSubarray(numbers, k):
    count = 0
    n = len(numbers)
    prefix = [0] * (n + 1)
    odd = 0
    mem = set()


    # traverse in the array
    for i in range(n):
        temp = []
        prefix[odd] += 1

        # if array element is odd
        if numbers[i] % 2:
            odd += 1
        temp.append(numbers[i])
        temp2 = tuple(temp)
        # when number of odd elements>=M
        if odd <= k and temp2 not in mem:
            count += prefix[odd - k]

    return count
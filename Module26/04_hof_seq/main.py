def qhofstadter(nums):
    if nums != [1, 1]:
        return
    seq = nums[:]
    while True:
        q = seq[-seq[-1]] + seq[-seq[-2]]
        seq.append(q)
        yield q


count = 1
for x in qhofstadter([1, 1]):
    if count > 16:
        break
    print(x, end=' ')
    count += 1

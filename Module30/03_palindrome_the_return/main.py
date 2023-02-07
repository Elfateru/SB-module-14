from collections import Counter


def can_be_poly(value: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(value).values()))) < 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('aabc'))
print(can_be_poly('aa'))
print(can_be_poly('aab'))

import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    test_case = list(map(int, input().split()))
    k, s = test_case[0], test_case[1:]

    if k == 0:
        break

    lotto_combs = list(combinations(s, 6))

    for lotto_comb in lotto_combs:
        print(*lotto_comb)
    print()

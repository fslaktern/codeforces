#!/usr/bin/env python3

x = 0

n = int(input())
assert(1 <= n <= 150)

for _ in range(n):
    op = input()
    if op[1] == "+":
        x += 1
    else:
        x -= 1

print(x)

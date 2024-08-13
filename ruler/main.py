#!/usr/bin/env python3

from math import ceil

test_cases = int(input())
MAX = 998
MIN = 2

for _ in range(test_cases):
    a, d = MIN, MAX
    c = a + ceil((d - a) // 3 * 2)
    b = a + (d - a) // 3

    while True:
        print(f"? {b} {c}")
        jury = int(input())

        expected = b * c
        one_off = b * (c + 1)
        two_off = (b + 1) * (c + 1)

        if jury == expected:
            if d - a <= 1:
                print(f"! {d + 1}")
                break
            a = c
            b = a + (d - a) // 3
            c = a + ceil((d - a) / 3 * 2)
        elif jury == one_off:
            if c - b <= 1:
                print(f"! {c}")
                break
            elif c - b == 2:
                a, d = b, c
                b += 1
            else:
                a, d = b, c
                b = a + (d - a) // 3
                c = a + ceil((d - a) / 3 * 2)
        elif jury == two_off:
            if d - a <= 1:
                print(f"! {a}")
                break
            d = b
            b = a + (d - a) // 3
            c = a + ceil((d - a) / 3 * 2)
        else:
            exit(1)



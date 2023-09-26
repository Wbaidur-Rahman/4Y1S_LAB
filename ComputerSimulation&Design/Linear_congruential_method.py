# x(i+1) = (a*x(i)+c) mod m 

import sys

def main():
    x, a, c, m, n = 0, 0, 0, 0, 10

    print("Enter seed, multiplier, increment, and modulus:")
    x, a, c, m = map(int, input().split())

    with open("Linear_congruential_method.txt", "w") as file:
        for _ in range(n + 1):
            x = (x * a + c) % m
            file.write(str(float(x) / float(m)) + " ")

if __name__ == "__main__":
    main()

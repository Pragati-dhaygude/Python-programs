N = int(input())
K = int(input())

pins = ["I"] * N

for _ in range(K):
    start, end = map(int, input().split())
    
    for i in range(start - 1, end):
        pins[i] = "."

print("".join(pins))
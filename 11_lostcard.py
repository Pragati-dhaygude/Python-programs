#11 Find the lost card

N = int(input("Enter value of N: "))

print("Enter the remaining", N-1, "numbers:")
numbers = list(map(int, input().split()))

total_sum = N * (N + 1) // 2
remaining_sum = sum(numbers)

lost_card = total_sum - remaining_sum

print("Lost card number is:", lost_card)




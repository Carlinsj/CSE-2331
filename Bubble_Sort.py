a = [1, 2, 5, 6, 3, 9, 8, 12, 17]

for i in range(len(a) - 1):
    # Flag to check if any swapping occurred
    swapped = False
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    # If no swaps occurred in this pass, the array is already sorted
    if not swapped:
        break

# Printing the sorted array
for i in range(len(a)):
    print(a[i], end=", ")

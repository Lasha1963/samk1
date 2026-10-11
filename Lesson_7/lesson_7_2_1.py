numbers = [34, 56, 78, 90, 45, 56, 45, 77, 103]
result = []
print(numbers)
i = 0
while True:
    if numbers[i] % 2 == 0:
        result.append(numbers[i])
    i += 1
    if i == len(numbers):break
print('ლუწი რიცხვებია: ', result)
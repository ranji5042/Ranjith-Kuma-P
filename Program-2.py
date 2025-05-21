def generate_odd_series(a):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result

try:
    a = int(input("Enter a number: "))
    result = generate_odd_series(a)
    print("Output:", end=" ")
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i])
        else:
            print(result[i], end=", ")
except ValueError:
    print("Please enter a valid integer.")

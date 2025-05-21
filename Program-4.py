def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

try:
    user_input = input("Enter numbers separated by commas: ")
    number_strings = user_input.split(",")
    numbers = []
    for s in number_strings:
        numbers.append(int(s.strip()))

    counts = count_multiples(numbers)
    print("Output:")
    for key in counts:
        print(f"{key}: {counts[key]}")
except ValueError:
    print("Please enter valid integers separated by commas.")

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return round(total / len(numbers), 2)

def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return round(max_number)

def get_numbers():
    # se fosse digitado nada ou o input não fosse inteiro, ele retornaria um erro
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        return numbers
    except ValueError:
        return []

def main():
    numbers = get_numbers()
    if numbers:
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    main()
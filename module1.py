def write_numbers_to_file(filename, numbers):
    with open(filename, 'w', encoding='utf-8') as f:
        for num in numbers:
            f.write(str(num) + '\n')

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers

def compute_product(numbers):
    if not numbers:
        return 1.0
    prod = 1.0
    for num in numbers:
        prod *= num
    return prod

def generate_sequence(n):
    sequence = []
    num = 1
    while len(sequence) < n:
        sequence.extend([str(num)] * min(num, n - len(sequence)))
        num += 1
    return ''.join(sequence[:n])


if __name__ == '__main__':
    n = int(input('Введите n: '))
    print(generate_sequence(n))

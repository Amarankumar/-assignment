a = int(input('a value is:'))
b = int(input('b value is: '))
fibonacci_sequence = []
fibonacci_sequence.append(b)
while b < 34:
    a, b = b, a + b
    fibonacci_sequence.append(b)
print(' '.join(str(num) for num in fibonacci_sequence))





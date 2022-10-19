#h06_square_value.py

numbers= []

def squares():
    for i in range(1,51):
        numbers.append(i ** 2)

squares()
print(numbers)

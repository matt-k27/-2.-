print('DZ2')

inputtedNumber = int(input('Enter your number pls : '))

numerator, denominator = divmod(inputtedNumber, 1000)
print(numerator)
numerator, denominator = divmod(denominator, 100)
print(numerator)
numerator, denominator = divmod(denominator, 10)
print(numerator)
print(denominator)

print('Thank you for using')
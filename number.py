print('Enter a Number..')
Num = int(input())
digit_2=  Num % 1000
digit_3 = Num % 100

print(float((digit_2 - digit_3)/100))
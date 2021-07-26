def fizzbuzz(test_number):
    # every line that is indented belongs to fizzbuzz function (be consistent with indentation)
    print(test_number)
    if(test_number % 3 == 0 and test_number % 5 == 0):
        print("FizzBuzz")
    elif(test_number % 5 == 0):
        print("Buzz")
    elif(test_number % 3 == 0):
        print("Fizz")

numbers =[3, 5, 15, 8, 10, 30, 1, 0, -10, 1000, 900, 150, 297, 16, 22]

for num in numbers:
    fizzbuzz(num)
# This is FizzBuzz Algorithm
# when, i is times of 3 return Fizz
# when, i is times of 5 return Buzz
# when, i is times of 15 return FizzBuzz
# else, print i

for i in range(1,20+1):
    if (i % 15 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)

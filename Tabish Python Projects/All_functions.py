import time
from math import sqrt

start = time.time()
global pi
pi = 3.14

def add(a, b):
    print("Addition is " + str(a+b))


def substrate(a, b):
    print("Substraction is " + str(a-b))


def multiply(a, b):
    print("Multiplication is " + str(a*b))


def divide(a, b):
    print("Division is " + str(float(a/b)))


def are_of_circle(r):
    print("Area of the Circle with Radius "+str(r)+" is "+str(pi*r*r))


def perimeter_of_circle(r):
    print("Perimeter of Circle with Radius "+str(r) + " is " + str(2*pi*r))


def surface_area_of_cylinder(r, h):
    answer = 2*pi*r*r+2*pi*r*h
    print("The Surface Area of Cylinder with radius " +
          str(r) + " and height "+str(h) + " is " + str(answer))


def volume_of_cylinder(r, h):
    print("The Volume of Cylinder with Radius "+str(r) +
          " and Height "+str(h) + " is " + str(pi*r*r*h))


def ferenheit_to_celsius(t):
    print("Given Temperature in Celsius is " + str(float(0.555 * (t-32))))


def ferenheit_to_kelvin(t):
    print("Given Temperature in Kelvin is " + str(float(t + 273.15)))


def final_velocity(u, a, t):
    print("Final Velocity is " + str(u + a * t))


def distance_traveled(u, a, t):
    print("Distance Traveled is " + str(u + a * t * t))


def perimeter_and_area_of_ring():

    i = float(input("Enter the Inner Radius\n"))
    o = float(input("Enter the Outer Radius\n"))

    print("Perimeter of the ring is " + str(float(2 * pi * (i + o))))
    print("Area of the ring is " + str(float(pi(o**2 - i**2))))


def arithmetic_mean():

    n = int(input("Enter the number of elements"))
    total = 0

    for i in range(n):
        no = int(input("Enter the no "))
        total += no

    mean = total/n

    print("The arithmetic mean is " + str(mean))


def harmonic_mean():

    a = int(input("Enter the first number\n"))
    b = int(input("Enter the sencond number\n"))

    print("The Harmonic mean is " + str(float((a*b)/(a + b))))


def surface_area_of_cuboid():

    l = float(input("Enter the Length\n"))
    b = float(input("Enter the Breadth\n"))
    h = float(input("Enter the Height\n"))

    print("The Surface Area of the Cuboid is " + str(2 * (l*b + l*h + b*h)))


def volume_of_cuboid():

    l = float(input("Enter the Length\n"))
    b = float(input("Enter the Breadth\n"))
    h = float(input("Enter the Height\n"))

    print("The Volume of the Cuboid is " + str(l * b * h))


def previous_and_next_character():

    char = str(input("Enter the Character\n"))
    x = ord(char)  # convert character into ascii value
    prev = int(x - 1)  # Decrement
    nxt = int(x+1)  # Increment
    previous = chr(prev)  # Reconvert ascii value into the decreased character
    next = chr(nxt)  # Reconvert ascii value into the increased character

    print("previous character is " + previous)

    print("Next character is " + next)


def distance_using_coordinate():

    x1 = int(input("Enter X1\n"))
    x2 = int(input("Enter X2\n"))
    y1 = int(input("Enter y1\n"))
    y2 = int(input("Enter y2\n"))

    print("The Distance between the points is " +
          str((sqrt((x1 - x2) - (y1 - y2)))))


# def asscii_value():

    #x = input("Enter a Character Or Number")
    #print("The ASCII value for " +str(x)+ " is " + str(ord(x)))


def interchange_using_temp():

    a = int(input("Enter First Number\na ="))
    b = int(input("Enter Second Number\nb ="))

    temp = a
    a = b
    b = temp

    print("Interchanged Number are \n a =  " +
          str(a) + "\nand\n b =  " + str(b))


def interchange():

    a = int(input("Enter First Number\na ="))
    b = int(input("Enter Second Number\nb ="))

    a = a+b
    b = a-b
    a = a-b
    print(a, b)


def net_sal():

    e_id = int(input("Enter the Emp ID\n"))
    base_sal = int(input("Enter the Basic Salary\n"))

    hr = (10/100) * base_sal
    da = (30/100) * base_sal
    pt = (5/100) * base_sal

    net_sal = base_sal + hr + da - pt
    print("The Net Salary for " + str(e_id) + " is " + str(net_sal))


def currency_notes():

    amount = int(input("Enter the amount to be withdrawn\n"))

    note_10 = int(amount / 10)
    amount = amount % 10

    note_5 = int(amount / 5)
    amount = amount % 5

    note_1 = int(amount)
    print("\n")
    print("The number of notes of 10 is " + str(note_10))
    print("The number of notes of 5 is " + str(note_5))
    print("The number of notes of 1 is " + str(note_1))


def even_odd():

    no = int(input("Enter the number\n"))

    if no % 2 == 0:
        print(str(no) + " is Even")
    else:
        print(str(no) + " is Odd")


def positive_negative():

    no = int(input("Enter the no\n"))

    if no > 0:
        print(str(no) + " is Positive")
    else:
        print(str(no) + " is Negative")


def Floyd_traingle():

    n = int(input("Enter the no of lines you want"))
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end='')
            num += 1
        print("\n")


def reverse_number():  # if the input ends with 0 (zero) then this code will eat the 0 in the output

    n = int(input("Enter the no to be reversed"))

    if n <= 9:
        raise ValueError("ENTER A POSITIVE NO OF ATLEAST 2 DIGITS")

    else:
        rev = 0
        while n > 0:
            rev = (rev * 10) + n % 10
            n //= 10

        print(rev)


def no_of_digits(n):
    n = abs(n)
    r = 0
    cnt = 0
    while n != 0:
        r = n % 10
        n //= 10
        cnt += 1
    return cnt


def is_palindrome(n):
    if n < 0:
        raise ValueError("ENTER A POSITIVE NUMBER OF MINIMUM 2 DIGITS")

    elif n >= 0 and n <= 9:
        raise ValueError("ENTER A POSITIVE NUMBER OF MINIMUM 2 DIGITS")

    else:
        rev = 0
        x = n
        while n > 0:
            rev = (rev * 10) + n % 10
            n //= 10

    if rev == x:
        print(str(x)+" is a PALINDROME")

    else:
        print(str(x) + " is not a PALINDROME")


def fibonacci(n):

    t1 = 0
    t2 = 1
    i = 3

    if n <= 0:
        raise ValueError("PLEASE ENTER A POSITIVE NUMBER MORE THAN 0")

    elif n == 1:
        print("THE FIBONACCI SERIES UPTO " + str(n) + " TERM IS:\n")
        print(t1)

    else:
        print("THE FIBONACCI SERIES UPTO " + str(n) + " TERMS IS:\n")
        print(t1)
        print(t2)
    while i <= n:
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
        i += 1


def sum_of_digits(n):

    if n >= 0 and n <= 9:
        return n

    else:
        n = abs(n)
        sum = 0
        while n != 0:
            r = n % 10
            sum += r
            n //= 10

    return sum


def is_prime(n):

    if n == 0 or n == 1:
        print("GIVEN NUMBER IS NOT A PRIME NUMBER")

    else:
        for i in range(2, n+1):
            if (n % i) == 0:
                break

        if i == n:
            print("GIVEN NUMBER IS A PRIME NUMBER")

        else:
            print("GIVEN NUMBER IS NOT A PRIME NUMBER")


def Armstrong_between(a, b):
    i = a
    if a < 10:

        raise ValueError("START RANGE MUST BE ATLEAST 2 DIGIT")

    elif a > b or a == b:

        raise ValueError("START RANGE SHOULD BE LESS THAN THE END RANGE")

    else:
        cnt = 0
        while i <= b and i >= a:

            digits = int(len(str(i)))
            cube = 0
            remain = 0
            x = i
            for j in range(digits):
                remain = x % 10
                cube += pow(remain, 3)
                x //= 10

            if i == cube:
                cnt += 1
                if cnt == 1:
                    print("THE ARMSTRONG NUMBERS BETWEEN " +
                          str(a)+" AND " + str(b)+" ARE:\n ")

                print(i)

            i += 1

        print("THE COUNT OF ARMSTRONG NUMBERS BETWEEN " +
              str(a)+" AND " + str(b)+" IS: " + str(cnt))


def bubble_sort(array):  # Swaps if left element is smaller than the right element
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


def selection_sort(array):  # Places the smallest number at the beginning on each iteration
    for step in range(len(array)):
        minimum = step
        for i in range(step, len(array)):
            if array[i] < array[minimum]:
                minimum = i

        array[minimum], array[step] = array[step], array[minimum]

    return array


# Armstrong_between(50, 500)
# print(selection_sort([57, 86, 34, 76, 11, 12, 98, 56, 89, 52, 55, 36, 14, 78, 95, 22, 33, 11, 78, 95, 30]))
print(time.time() - start)
print()
print()

# fibonacci(9)

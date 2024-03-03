global n


def triangle_patterns():
    print('                          ')
    print('--------------------------')
    print('**** Triangle Pattern ****')
    print('--------------------------')
    print('                          ')
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print("")


def inverted_right_angled_triangle():
    # n=int(input("enter number no of rows for inverted_right_angled_triangle:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Inverted right angled triagle *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print(" ")


def pyramid_pattern():
    # n = int(input("enter number no of rows for pyramid_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Pyramid Pattern *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(n):
        for j in range(i, n):
            print("_", end=" ")
        for j in range(i + 1):
            print("*", end=" ")

        for j in range(i):
            print("*", end=" ")
        for j in range(i, 5):
            print("_", end=" ")
        print(" ")


def diamond_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Diamond Pattern *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(n - 1):  # decreased n to n-1 because we have to merge upper and lower pyramid
        for j in range(i, n):
            print("_", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i, n):
            print("_", end=" ")

        print("")

    # reverse pyramid
    for i in range(n):

        for j in range(i + 1):
            print("_", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        for j in range(i, n - 1):  # decreased
            print("*", end=" ")
        for j in range(i + 1):
            print("_", end=" ")

        print(" ")


def fibnocci_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Fibanocci Pattern *****')
    print('----------------------------------------')
    print('                          ')
    # n = int(input("enter number no of rows for fibnocci_pattern:"))
    a = 0
    b = 1
    c = a + b
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(c, end=" ")
            c = a + b
            a = b
            b = c
        print(" ")


def pascals_triangle_pattern():
    # n = int(input("enter number no of rows for pascals_triangle_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Pascal Triangle Pattern *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(' ', end='')

        # first element is always 1
        c = 1
        for j in range(1, i + 1):
            # first value in a line is always 1
            print(' ', c, sep='', end='')

            # using Binomial Coefficient
            c = c * (i - j) // j
        print()


def generate_next_prime(prev):
    if prev == 0:
        prev = 2
    else:
        prev = prev + 1
    for i in range(prev, 100000):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            return i


def prime_number_pattern():
    # n = int(input("enter a number for prime_number_pttern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Prime number Pattern *****')
    print('----------------------------------------')
    print('                          ')
    prev_prime = 0
    current_prime = 0

    for i in range(n):
        for j in range(i):
            # print("*", end=" ")
            current_prime = generate_next_prime(prev_prime)
            prev_prime = current_prime
            print(current_prime, end=" ")
        print("")


# def number_triangle_pattern():
#     # n=int(input("enter a number for number_triangle_pattern"))
#     for i in range(n):
#         for j in range(i,n):
#             print(" ",end=" ")
#         for j in range(i+1):
#             print("*",end=" ")
#         print()


def number_triangle_pattern():
    # n = int(input("enter a number for number_triangle_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Number triangle Pattern *****')
    print('----------------------------------------')
    print('                          ')
    p = 1

    for i in range(n):

        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print(p, end=" ")
        p = p+1
        print()


def alphabetic_pyramid():
    # n = int(input("enter a number for alphabetic_pyramid_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Alphabetic pyramid Pattern *****')
    print('----------------------------------------')
    print('                          ')
    p = 1
    p = 65
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(0, i + 1):
            print(chr(p), end="")
            p = p + 1  # for colomn printing
        for j in range(0, i):  # decreased for adjustment
            print(chr(p), end="")
            p = p + 1
        for j in range(i, n):
            print(" ", end="")

        print("")


def alphabetic_square_pattern():
    # n = int(input("enter a number for alphabetic_square_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** Alphabetic square Pattern *****')
    print('----------------------------------------')
    print('                          ')
    p = 1
    p = 65
    for i in range(n):
        for j in range(n):
            print(chr(p),end=" ")
            p = p+1
        print("")


def alphabetic_triangle_pattern():
    # n = int(input("enter a number for alphabetic_triangle_pattern:"))
    print('                          ')
    print('----------------------------------------')
    print('**** alphabertic triangle Pattern *****')
    print('----------------------------------------')
    print('                          ')
    p = 65
    for i in range(n):
        for j in range(0, i + 1):
            print(chr(p), end="")
        p = p + 1
        print("")



def alphabetic_diamond_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** alphabetic Diamond Pattern *****')
    print('----------------------------------------')
    print('                          ')
    p = 65
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end="  ")
        for j in range(0, i + 1):
            print(chr(p), end="  ")
            p = p + 1  # for colomn printing
        for j in range(0, i):  # decreased for adjustment
            print(chr(p), end="  ")
            p = p + 1

        print("")

    for i in range(n):
        for j in range(i + 1):
            print(" ", end="  ")
        for j in range(i, n):
            print(chr(p), end="  ")
            p = p + 1  # for colomn printing
        for j in range(i, n - 1):  # decreased for adjustment
            print(chr(p), end="  ")
            p = p + 1

        print("")

def square_star_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** square star pattern *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(n):
        for j in range(n):
            print("*", end=" ")

        print("")




    #p = 65
    for i in range(n):
        for j in range(i + 1):
            print(" ", end="  ")
        for j in range(i, n):
            print(chr(p), end="  ")
            p = p + 1  # for colomn printing
        for j in range(i, n - 1):  # decreased for adjustment
            print(chr(p), end="  ")
            p = p + 1

        print("")


def square_star_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** square star pattern *****')
    print('----------------------------------------')
    print('                          ')
    for i in range(n):
        for j in range(n):
            if i == 0 or i == 4 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ")

def hollow_diamond_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** hollow diamond pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n - 1):  # decreased n to n-1
        for j in range(i, n - 1):
            print(" ", end=" ")
        for j in range(i):

            if j == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        for j in range(i + 1):
            if j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

    # reverse pyramid

    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(i, n):
            if j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(i, n - 1):
            if j == n - 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print(" ")

def rectangle_star_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Rectangle Star Pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n):
        for j in range(n + 5):
            print("*", end=" ")
        print()

def hollow_pyramid_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Hollow Pyramid Pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            if i == 4 or j == 0 or j == i:

                print("*", end=" ")
            else:
                print(" ", end=" ")

        for j in range(i + 1):
            if i == 4 or i == 0 or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print(" ")

def hollow_diamond_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Hollow Diamond Pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n - 1):  # decreased n to n-1
        for j in range(i, n - 1):
            print(" ", end=" ")
        for j in range(i):

            if j == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        for j in range(i + 1):
            if j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(i, n):
            if j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(i, n - 1):
            if j == n - 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print(" ")

def arrow_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Arrow Pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n):

        for j in range(i):  # decreased for correct position
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")

        print("")

    for i in range(n):

        for j in range(i, n):
            print(" ", end="")
        for j in range(i, n):
            print("*", end="")

        print("")


def hourglass_pattern():
    print('                          ')
    print('----------------------------------------')
    print('**** Hourglass Pattern*****')
    print('----------------------------------------')
    print('                          ')

    for i in range(n):

        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        for j in range(i, n - 1):  # decreased n to adjust the triangle
            print("*", end=" ")
        for j in range(i + 1):
            print(" ", end=" ")
        print(" ")

    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        for j in range(i):  # decreased n to adjust
            print("*", end=" ")
        for j in range(i, n):
            print(" ", end=" ")

        print("")


if __name__ == "__main__":
    n = int(input("enter a number: "))
    triangle_patterns()
    inverted_right_angled_triangle()
    pyramid_pattern()
    diamond_pattern()
    fibnocci_pattern()
    pascals_triangle_pattern()
    prime_number_pattern()
    number_triangle_pattern()
    alphabetic_pyramid()
    alphabetic_square_pattern()
    alphabetic_triangle_pattern()
    alphabetic_diamond_pattern()
    square_star_pattern()
    hollow_diamond_pattern()
    rectangle_star_pattern()
    hollow_pyramid_pattern()
    hollow_diamond_pattern()
    arrow_pattern()
    hourglass_pattern()




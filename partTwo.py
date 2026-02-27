import math

def main():
A = int(input("Enter side A: "))
B = int(input("Enter side B: "))
C = pythag(A, B)
print(f"The hypotenuse is {C}")

def pythag(A,B):
    return math.sqrt(A ** 2 + B ** 2)

main()

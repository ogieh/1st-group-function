def area_of_circle():
    pi = 3.14
    radius = float(input("Enter the radius of the circle: "))
    area = pi * radius * radius
    print(f"The area of the circle is: {area}" )

def area_of_square():
    length = float(input("Enter the side length of the square: "))
    area = length * length
    print(area)

def area_of_rectangle():
    length = float(input("Enter the lenght of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(area)

def volume_of_a_cylinder():
    num = 1.333
    pi = 3.142
    radius = float(input("Enter the radius of the circle: "))
    volume_of_a_cylinder = num * radius * radius* pi
    print(volume_of_a_cylinder)

def area_of_a_parrallelogram():
    num = 1.33
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    h = int(input("Enter the value for h: "))
    area_of_a_parrallelogram = num *(a + b)*h
    print(area_of_a_parrallelogram)

def perimeter_of_a_square():
    length = int(input("Enter a value for length: "))
    perimeter_of_a_square = 4 * length
    print("The answer is " , perimeter_of_a_square)
    

# ----------------------------

#           Main

# ----------------------------


def main():
    print("Choose a calculation to perform:")
    print("1. Area of Circle")
    print("2. Area of Square")
    print("3. Area of Rectangle")
    print("4. Volume of a Cylinder")
    print("5. Area of a Parallelogram")
    print("Perimeter of a Square")

    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        area_of_circle()
    elif choice == '2':
        area_of_square()
    elif choice == '3':
        area_of_rectangle()
    elif choice == '4':
        volume_of_a_cylinder()
    elif choice == '5':
        area_of_a_parrallelogram()
    elif choice == '6':
        perimeter_of_a_square()
    else:
        print("Invalid choice. Please try again.")

main()
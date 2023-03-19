def calculateerea(input,dim,default=10):
    input = input("Enter the shape you want to calculate area of: ")
    pie = 3.14
    area = 0
    if input =="square":
        dim = int(input("Enter the side"))
        area == area+(dim ** 2)
    elif input == "Circle":
        radius = int(input("Enter the dim: "))
        area = area + (2 * pie * dim)
    elif input == "Rectangle":
        dim = int(input("Enter the length: "))
        area = (dim * default)
    elif input == "Triangle":
        dim = int(input("Enter the base: "))
        area = area + (0.5 * dim * default)
    else:
        print("Select a valid shape")
    print("%.2f" % area)




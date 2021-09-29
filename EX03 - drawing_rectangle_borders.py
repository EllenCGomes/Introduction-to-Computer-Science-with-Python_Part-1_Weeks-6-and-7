w = int(input("Enter the rectangle width: "))
h = int(input("Enter the rectangle height: "))
              
height = 1
width = 1

while height <= h:
    # print first and last columns
    if height == 1 or height == h:
        while width <= w:
           print ("#", end = "")
           width = width + 1
        height = height + 1
        width = 1
        print ()
    else:
        # print middle columns
        while width <= w:
            if width == 1 or width == w:
                print ("#", end = "")
                width = width + 1
            else:
                print (" ", end = "")
                width = width + 1
        height = height + 1
        width = 1
        print ()

length = int (input ("length:" ))
height = int (input ("height: ")) 
for i in range (0, length):
    for k in range (0, height):
        print ("*" ,  end = " ")
        print ()
    
    length = int (input("Lenght: " ))
    for i in range(1, length + 1):
        print (" " * (length - i) , end="")
        print(" * " * i)
    
        
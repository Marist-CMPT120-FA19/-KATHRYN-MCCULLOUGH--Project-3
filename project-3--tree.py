def tree():
    print("How many branches does the tree have?")
    print()
    height= input("Number of branches: ")
    length= int(height)*2-1
    space= (length-1)/2
    x=1

    while x < int(height):
        print (" "* (int(space) - x +1), "#"*(2*x -1))
        x= x+1
    print(" "* (int(height) -1), "#")
    
    
tree()

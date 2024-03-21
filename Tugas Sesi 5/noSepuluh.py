for i in range(5):
    print()
    for j in range(5, i, -1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(3, end=" ")
            else:
                print(2, end=" ")
        else:
            if j % 2 != 0:
                print(3, end=" ")
            else: 
                print(2, end=" ") 
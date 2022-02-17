def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError as e:
    print("There is an error => ", e)
else:
    print("Succssefuly")

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

additoin(10, 20)   

try:
    additoin(10, 20)
# except Exception as e:
#     print("the error is: ", e)
except NameError:
    print("variable 'b' is not defined")
else:
    print("the operation is successful")
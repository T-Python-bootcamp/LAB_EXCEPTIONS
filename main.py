
class MyCustomError(Exception):
    ''' This is some meaningless Exception '''

try: 
    def additoin(x, y):
        if x != 10 or y != 20:
            raise MyCustomError("x or y doesn't have acceptable value(s). \nhint: attempt 10,20 respectively")
        x = 10
        y = 20
        print("Addition:", x + b)
    additoin(10, 20)
except Exception as e:
    print("Error in the code: ",e)
else:
    print("the operation is successful")
finally:
    print("Operation ended.")
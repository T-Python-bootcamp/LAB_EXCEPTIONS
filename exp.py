

from multiprocessing.sharedctypes import Value


def additoin(x, y):
    try:
          x = 10
          y = 20
          print("Addition:", x + b)
    except Exception as error:
        raise SyntaxError(f"{error}") 
    else :
        print("the operation is successful")


additoin(10, 20)

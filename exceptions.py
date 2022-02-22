from asyncio import exceptions


def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except Exception as e:
        print(e)
        raise ValueError("variable not defined")
    else:
        print("the operation is successful")
addition(10, 20)


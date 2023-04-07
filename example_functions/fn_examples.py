import time
from example_functions.face_detection import face_detection


def fn_example_1(num):
    n = num[0]
    t = 10 * n  # 10 seconds Execution
    print("Function Execution fn_example_1")
    time.sleep(t)
    return True


def fn_example_2(num):
    n = num[0]
    t = 20 * n  # 20 seconds Execution
    print("Function Execution fn_example_2")
    time.sleep(t)
    return True


def fn_example_3(imagePath: str):
    imgPath = imagePath[0]
    face_detection(imagePath=imgPath)

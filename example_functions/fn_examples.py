import time
from example_functions.face_detection import fd


def image_recognition(num):
    n = num[0]
    t = 3 * n  # 3 seconds Execution
    print("Function Execution image_recognition")
    time.sleep(t)
    return True


def video_conversion(num):
    n = num[0]
    t = 20 * n  # 20 seconds Execution
    print("Function Execution video_conversion")
    time.sleep(t)
    return True


def face_detection(imagePath: str):
    imgPath = imagePath[0]
    fd(imagePath=imgPath)

def gif_creation(num):
    n = num[0]
    t = 2*n
    print("Function Execution gif_creation")
    time.sleep(t)
    return True

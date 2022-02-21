from threading import *
from time import sleep
import keyboard

scrollKey = 1
#
# # Threading
# def run1():
#     for i in range(50):
#         print('hello')
#         sleep(1)
#     return 0
#
#
# def run2():
#     for i in range(50):
#         print('bye')
#         sleep(1)
#     return 0
#
#
# def run3():
#     for i in range(50):
#         print('hi')
#         sleep(1)
#     return 0
#
#
# thread1 = Thread(target = run1)
# thread2 = Thread(target = run2)
# thread3 = Thread(target = run3)
#
# thread1.start()
# thread2.start()
# thread3.start()


def speech_listening():
    global scrollKey
    sleep(5)
    scrollKey = 0
    return 0


# defining the scroll function
def scroll(function):
    thread_1 = Thread(target = function)
    thread_2 = Thread(target = speech_listening)

    thread_1.start()
    thread_2.start()
    return 0


def scrollDown():
    global scrollKey
    while scrollKey == 1:
        keyboard.press_and_release("down")
        keyboard.press_and_release("down")
        sleep(1)
    return 0


def scrollUp():
    global scrollKey
    while scrollKey == 1:
        keyboard.press_and_release("up")
        keyboard.press_and_release("up")
        sleep(1)
    return 0

scroll(scrollDown)
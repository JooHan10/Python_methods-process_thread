#####################################
# print('hello, os')
#####################################

#####################################
# import os

# print('hello, os')
# print('ijh\'s pid is', os.getpid())
#####################################

#####################################
# from multiprocessing import Process
# import os

# def ijh():
#     print('child process', os.getpid())
#     print('my parent is', os.getppid())

# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child = Process(target=ijh).start()
#####################################

#####################################
# from multiprocessing import Process
# import os

# def ijh():
#     print('같은 작업 중')
#     print('child process', os.getpid())

# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child1 = Process(target=ijh).start()
#     child2 = Process(target=ijh).start()
#     child3 = Process(target=ijh).start()
#####################################

#####################################
from multiprocessing import Process
import os

def I():
    print('This is I')
def Joo():
    print('This is Joo')
def Han():
    print('This is Han')

if __name__ == '__main__':
    child1 = Process(target=I).start()
    child2 = Process(target=Joo).start()
    child3 = Process(target=Han).start()
#####################################
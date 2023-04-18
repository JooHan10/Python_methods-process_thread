#####################################
# import threading
# import os

# def ijh():
#     print('thread id', threading.get_native_id())
#     print('process id', os.getpid())

# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread = threading.Thread(target=ijh).start()
#####################################

#####################################
# import threading
# import os

# def ijh():
#     print('thread id', threading.get_native_id())
#     print('process id', os.getpid())

# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=ijh).start()
#     thread2 = threading.Thread(target=ijh).start()
#     thread3 = threading.Thread(target=ijh).start()
#####################################

#####################################
import threading
import os

def I():
    print('This is I')

def Joo():
    print('This is Joo')

def Han():
    print('This is Han')

if __name__ == '__main__':
    thread1 = threading.Thread(target=I).start()
    thread2 = threading.Thread(target=Joo).start()
    thread3 = threading.Thread(target=Han).start()
#####################################
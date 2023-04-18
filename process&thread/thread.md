# Python으로 thread 다루기 연습


## thread 만들기
code
```
import threading
import os

def ijh():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

if __name__ == '__main__':
    print('process id', os.getpid())
    thread = threading.Thread(target=ijh).start()
```
result
```
process id 19764
thread id 22484
process id 19764
```
1. thread = threading.Thread(target=ijh).start() code는 ijh라는 함수를 실행하는 thread를 만들고 실행하라는 의미입니다.
2. process 내에서 ID가 22484라는 thread를 만들어낸 것이 주목할 부분 입니다.


## 같은 작업을 하는 thread 생성
code
```
import threading
import os

def ijh():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=ijh).start()
    thread2 = threading.Thread(target=ijh).start()
    thread3 = threading.Thread(target=ijh).start()
```
result
```
process id 13300
thread id 20976
process id 13300
thread id 27036
process id 13300
thread id 18112
process id 13300
```
같은 작업을 하는 세개의 thread가 서로 다른 thread id를 가지지만 동일한 process 내에서 작업이 이뤄지므로 process id는 같은 것을 알 수 있습니다.


## 각기 다른 작업을 하는 thread 생성 
code
```
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
```
result
```
This is I
This is Joo
This is Han
```
한 개의 process 내에서 여러 thread를 생성할 수도 있습니다. 

process에서와 차이점
1. thread가 더 경량화된 방식 입니다.
2. 하나의 thread가 오류 난다면 다른 thread에 영향을 끼칩니다.
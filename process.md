# Python으로 process 다루기 연습


## process 만들기
code
```
print('hello, os')
```
result
```
hello, os
```
실행된 순간 문자열을 출력하는 process가 생성됩니다.


## process PID 확인하기
code
```
import os

print('hello, os')
print('ijh\'s pid is', os.getpid())
```
result
```
hello, os
ijh's pid is 28016
```
PID 값은 운영체제가 그때그때 부여하는 값이기 때문에 실행 할 때마다 다른 PID값이 출력됩니다.


## 여러(자식) process 생성
code
```
from multiprocessing import Process
import os

def ijh():
    print('child process', os.getpid())
    print('my parent is', os.getppid())

if __name__ == '__main__':
    print('parent process', os.getpid())
    child = Process(target=ijh).start()
```
result
```
parent process 3472
child process 9984
my parent is 3472
```
1. print('parent process', os.getpid()) code 는 ‘parent process + PID값’ 형태로 출력하는 코드
2. child = Process(target=ijh).start() code 는 ijh 라는 함수를 실행하는 자식 프로세스를 만들고 실행하는 코드
3. ijh 함수는 print('child process', os.getpid()), print('my parent is', os.getppid()) 두 줄의 코드를 실행


## 같은 작업을 하는 process 생성
code
```
from multiprocessing import Process
import os

def ijh():
    print('같은 작업 중')
    print('child process', os.getpid())

if __name__ == '__main__':
    print('parent process', os.getpid())
    child1 = Process(target=ijh).start()
    child2 = Process(target=ijh).start()
    child3 = Process(target=ijh).start()
```
result
```
parent process 14588
같은 작업 중
child process 15212
같은 작업 중
child process 21876
같은 작업 중
child process 21776
```
내용이 같은 작업을 하고 있지만 process는 각각 별개로 실행되기 때문에 PID 또한 서로 다르다는 것을 알 수 있습니다.


## 각기 다른 작업을 하는 porcess 생성
code
```
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
```
result
```
This is I
This is Joo
This is Han
```
1. 위와 같이 process를 사용하여 각기 다른 작업을 동시에 수행하는 code를 작성할 수도 있습니다.
2. process들은 각각 독립적으로 실행되므로 서로의 작업에 거의 영향을 미치지 않습니다.

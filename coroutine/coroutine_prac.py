name_num = {"JooHan": "1", "Jane": "2", "Max": "3"}

def search():
    name = yield
    while True:
        if name in name_num:
            number = name_num[name]
        else:
            number = "정보 없음"
        name = yield number

# 코루틴 객체 생성
search_coroutine = search()
next(search_coroutine)

# 검색 에시
result = search_coroutine.send("JooHan")
print(result) # 1

result = search_coroutine.send("Jane")
print(result) # 2

result = search_coroutine.send("Sarah")
print(result) # 정보 없음
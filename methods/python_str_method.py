# 문자열 메소드


# 1.count: 문자열 내에서 특정문자가 몇 개나 있는지 세는 메소드
text = "I study at home 12 hours a day"
ijh = text.count("a")
print(ijh)  # 3


# 2. find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메소드 (없을 경우 -1 return)
text = "I study at home 12 hours a day"
ijh = text.find("home")
print(ijh)  # 11


# 3. index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메소드 (없을 경우 VallueError) 
text = "I study at home 12 hours a day"
try:
    ijg = text.index("home")
    print(ijh)
except ValueError:
    print("찾는 문자열이 없습니다.")


# 4. join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메소드
ijh = ["I", "Joo", "Han"]
joined_ijh = ", ".join(ijh)
print(joined_ijh)


# 5-1. upper: 문자열 내의 모든 알파벳 소문자를 대문자로 바꿔주는 메소드
# 5-2. lower: 문자열 내의 모든 알파벳 대문자를 소문자로 바꿔주는 메소드
text = "I study at home 12 hours a day"
uppercase_text = text.upper()
print(uppercase_text)

lowercase_text = text.lower()
print(lowercase_text)


# 6. replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메소드
text = "I study at home 12 hours a day"
replaced_text = text.replace("study", "work out")
print(replaced_text)


# 7. split: 문자열을 특정 문자를 기준으로 나누는 메소드 (결과는 리스트 형태로 반환)
ijh = "I, Joo, Han"
ijh_list = ijh.split(",")
print(ijh_list)
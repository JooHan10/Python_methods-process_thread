# 딕셔너리 메소드


# 1. 딕셔너리 쌍 추가
ijh_dict_2 = {"Samsung": 1, "Microsoft": 1, "Apple": 4}
ijh_dict_2["LG"] = 1
print(ijh_dict_2)


# 2. del: 딕셔너리에서 특정 요소를 삭제
ijh_dict_3 = {"Samsung": 1, "Microsoft": 1, "Apple": 4}
del ijh_dict_3["Apple"]
print(ijh_dict_3)


# 3. 딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법(딕셔너리에 Key가 업는 경우. KeyError)
ijh_dict_4 = {"Samsung": 1, "Microsoft": 1, "Apple": 4}
print(ijh_dict_4["Apple"])


# 4. Keys: 딕셔너리에서 모든 Key를 리스트로 만들기
ijh_dict_5 = {"Samsung": 1, "Microsoft": 1, "Apple": 4}
ijh_list_1 = list(ijh_dict_5.keys())
print(ijh_list_1)


# 5. Values: 딕셔너리에서 모든 Key를 리스트로 만들기
ijh_dict_6 = {"Samsung": 1, "Microsoft": 1, "Apple": 4}
ijh_list_2 = list(ijh_dict_6.values())
print(ijh_list_2)


# 6. items: 딕셔너리의 모든 Key와 Value값을 튜플 형태 리스트로 반환
ijh_1 = {"name": "I Joo Han", "age": 30, "gender": "male"}
ijh_info = ijh_1.items()
print(ijh_info)


# 7. clear: 딕셔너리의 모든 요소를 삭제
ijh_2 = {"name": "I Joo Han", "age": 30, "gender": "male"}
ijh_2.clear()
print(ijh_2)


# 8. get: 딕셔너리에서 지정한 Key에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
ijh_3 = {"name": "I Joo Han", "age": 30, "gender": "male"}
name = ijh_3.get("name")
print(name)

email = ijh_3.get("email")
print(email)

email = ijh_3.get("email", "unknown") # 기본값을 설정할 수 있음
print(email)

    # Django에서 request.POST['key'] 와 request.POST.get('key') 의 공통점 & 차이점
    # 공통점
        #두 방식 모두 딕셔너리에서 'key'에 해당하는 데이터를 가져옵니다.
    #차이점
        #request.POST['key']: key가 존재하지 않을 경우 KeyError를 출력하는 예외가 발생합니다.
        #request.POST.get['key']: key가 존재하지 않을 경우 None을 반환하며, None대신 반환할 디폴트 값을 지정할 수 있습니다.


# 9. in: 해당 Key가 딕셔너리 안에 있는지 확인
ijh_4 = {"name": "I Joo Han", "age": 30, "gender": "male"}
print("name" in ijh_4)
print("email" in ijh_4)
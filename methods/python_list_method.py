# 리스트 메소드


# 1. len: 리스트의 길이를 반환하는 내장 함수
ijh_1 = [1, 2, 3, 4, 5]
print(len(ijh_1))


# 2. del: 리스트에서 특정 요소를 삭제하는 연산자
ijh_2 = [1, 2, 3, 4, 5]
del ijh_2[2]
print(ijh_2)


# 3. append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메소드
ijh_3 = [1, 2, 3, 4, 5]
ijh_3.append(6)
print(ijh_3)


# 4. sort: 리스트를 오름차순으로 정렬하는 메소드
ijh_4 = [1, 2, 3, 4, 5]
ijh_4.sort()
print(ijh_4)


# 5. reverse: 리스트의 요소 순서를 반대로 뒤집는 메소드
ijh_5 = [1, 2, 3, 4, 5]
ijh_5.reverse()
print(ijh_5)


# 6. index: 리스트에서 특정 요소의 인덱스를 반환하는 메소드
ijh_6 = ['I', 'Joo', 'Han']
print(ijh_6.index('Joo'))


# 7. insert: 리스트의 특정 위치에 요소를 삽입하는 메소드
ijh_7 = [1, 2, 3, 4, 5]
ijh_7.insert(2, 10)
print(ijh_7)


# 8. remove: 리스트에서 특정요소를 제거하는 메소드
ijh_8 = [1, 2, 3, 4, 5]
ijh_8.remove(3)
print(ijh_8)


# 9. pop: 리스트에서 마지막 요소를 빼낸뒤, 그 요소를 삭제하는 메소드 
ijh_9 = [1, 2, 3, 4, 5]
ijh_9.pop(3)
print(ijh_9)


# 10. conut: 리스트에서 특정요소의 개수를 세는 메소드
ijh_10 = [1, 2, 3, 3, 4, 5]
print(ijh_10.count(3))


# 11-1. extend: 리스트를 확장하여 새로운 요소들을 추가하는 메소드
# 11-2. +=: extend는 '+='을 사용하여 구현 할 수도 있음. 
ijh_11 = [1, 2, 3]
ijh_11.extend([4, 5, 6])
print(ijh_11)

ijh_12 = [1, 2, 3]
ijh_12 += [4, 5, 6]
print(ijh_12)
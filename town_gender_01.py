# town_gender_01.py
# 성별 데이터 불러오기

import csv

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)

# 헤더 파일
header = next(data)

print(header)

# 남, 여 데이터 시작 위치 찾기
print("남 데이터 시작 인덱스: ", header.index('2021년07월_남_0세'))
print("여 데이터 시작 인덱스: ", header.index('2021년07월_여_0세'))

# 남, 여 데이터 확인.
print(header[3:104])
print(header[106:])

# town_gender_01.py
# 성별 데이터 불러오기

import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)

# 헤더 파일
header = next(data)

print(header)

# 남, 여 데이터 시작 위치 찾기
# print("남 데이터 시작 인덱스: ", header.index('2021년07월_남_0세'))
# print("여 데이터 시작 인덱스: ", header.index('2021년07월_여_0세'))

# 남, 여 데이터 확인
# print(header[3:104])
# print(header[106:])

result_f = []
result_m = []
# 우리 동네 자료 추출
for one in data:
    if '범계' in one[0]:
        result_m = one[3:104]
        result_f = one[106:]
        break

def make_num(res, i = 1):
    res = [one.replace(',', '') for one in res]
    res = map(int, res)
    res = [one * i for one in res]

    return res

# 데이터 처리
result_m = make_num(result_m)
result_f = make_num(result_f, -1)

# 그래프 그리기
plt.style.use('ggplot')
plt.figure(figsize=(10, 8), dpi=150)
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # -기호가 안나올 경우
plt.title('범계동 남여 인구 분포 ')
plt.barh(range(101), result_m)
plt.barh(range(101), result_f)
plt.show()

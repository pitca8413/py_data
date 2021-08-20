# town_01.py
# 데이터 불러오기

import csv
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')

# 데이터 불러오기
f = open('age.csv', encoding='cp949')
data = csv.reader(f)

# 헤더
header = next(data)

# 우리 동네 인구수 기록 변수
result = []

# 우리 동네 데이터 추출하기
for one in data:
    if '범계동' in one[0]:
        result = one[3:]

# 데이터 처리
result = [one.replace(',', '') for one in result]
result = list(map(int, result))

# 우리 동네 인구 출력하기
for idx, one in enumerate(result):
    print(f'{idx}세: {one}명')

# 그래프 출력하기
plt.title('범계동 나이별 인구수')
plt.barh(range(101), result)
plt.show()

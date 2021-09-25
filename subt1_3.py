# 지하철 시간대별 데이터 시각화
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
# 지하철 시간대별로 가장 많은 사람이 승하차 하는 역 찾기
# 07:00:00~07:59:59 ~ 08:00:00~08:59:59

import csv

# 1. 데이터 불러오기
f = open('202108_subtime.csv')
data = csv.reader(f)

# 2. 필드명 추출
header = next(data)

print(header)
next(data) # 불필요한 데이터 스킵

# 출근 시간 인덱스 찾기
go_to_work_idx = header.index('07:00:00~07:59:59')
print('출근시간 인덱스: ', go_to_work_idx)

# 3. 출근 시간 데이터 추출
max_num = 0
max_sta = ''
result = []
for one in data:
    num1 = one[go_to_work_idx].replace(',', '')
    num1 = int(num1)
    num2 = one[go_to_work_idx + 2].replace(',', '')
    num2 = int(num2)
    result.append(num1 + num2)

    if num1 + num2 > max_num:
        max_num = num1 + num2
        max_sta = f'{one[3]} {one[1]}'

print(result)

# 4. 바 그래프 그리기
import matplotlib.pyplot as plt
result.sort()
plt.bar(range(len(result)), result)
plt.show()

# 5. 최다 승차 인원역
print(max_num, max_sta)
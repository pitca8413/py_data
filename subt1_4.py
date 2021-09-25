# 지하철 시간대별 데이터 시각화
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
# 지하철 시간대별로 가장 많은 사람이 승하차 하는 역 찾기
# 07:00:00~07:59:59 ~ 08:00:00~08:59:59

import csv
import matplotlib.pyplot as plt

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
result = []
for one in data:
    # 문자데이터 수치화
    one[4:-1] = [tmp.replace(',', '') for tmp in one[4:-1]]
    one[4:-1] = map(int, one[4:-1])
    # print(one)
    num = sum(one[go_to_work_idx:go_to_work_idx + 3:2]) # 출근 시간대 합 구하기
    result.append(num)

print(result)

# 4. 바 그래프 그리기
result.sort()
plt.bar(range(len(result)), result)
plt.show()

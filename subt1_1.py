# 지하철 시간대별 데이터 시각화
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
# 지하철 시간대별로 가장 많은 사람이 승하차 하는 역 찾기

import csv

# 1. 데이터 불러오기
f = open('202108_subtime.csv')
data = csv.reader(f)

# 2. 필드명 추출
header = next(data)

print(header)
next(data) # 불필요한 데이터 스킵

# 3. 데이터 보기
for i in range(5):
    one = next(data)
    print(one)

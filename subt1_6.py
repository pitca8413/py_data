# 밤 10시에 사람들이 가장 많이 타는 역 찾기

import csv

# 1. 데이터 불러오기
f = open('202108_subtime.csv')
data = csv.reader(f)

# 2. 필드명 추출하기
header = next(data)

print(header)
next(data) # 불필요한 데이터 스킵

# 3. 밤 10시 인덱스 찾기
idx = header.index('22:00:00~22:59:59')
# idx = header.index('23:00:00~23:59:59')
print("밤 10시 인덱스: ", idx)

# 4. 최대 승차 인원 찾기
max_val = 0
max_sta = ''

for one in data:
    num_10 = int(one[idx].replace(',', ''))
    if num_10 > max_val:
        max_val = num_10
        max_sta = f'{one[3]}({one[3]})'

print(max_sta, max_val)

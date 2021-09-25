# 지하철 시간대별 데이터 시각화
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
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
max_in_val = 0
max_in_sta = ''
max_out_val = 0
max_out_sta = ''

for one in data:
    # 문자데이터 수치화
    one[4:-1] = [tmp.replace(',', '') for tmp in one[4:-1]]
    one[4:-1] = map(int, one[4:-1])
    # print(one)
    num_in = sum(one[go_to_work_idx:go_to_work_idx + 5:2]) # 출근 시간대 승차인원 합 구하기
    num_out = sum(one[go_to_work_idx + 1:go_to_work_idx + 6:2]) # 출근 시간대 하차인원 합 구하기

    if num_in > max_in_val:
        max_in_val = num_in
        max_in_sta = f'{one[3]} {one[1]}'
    if num_out > max_out_val:
        max_out_val = num_out
        max_out_sta = f'{one[3]} {one[1]}'

# 4. 결과 출력
print('최다 승차역:', max_in_sta, max_in_val)
print('최다 하차역:', max_out_sta, max_out_val)


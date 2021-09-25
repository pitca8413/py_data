# 시간대별로 사람들이 가장 많이 타고 내리는 역

import csv

f = open('202108_subtime.csv')
data = csv.reader(f)

header = next(data)
print(header)
print(next(data))

mx = [0] * 24
mx_station = [''] * 24
mx_idx = 0

for one in data:
    in_num = one[4:len(header)-1:2]
    for idx, one_num in enumerate(in_num):
        num = int(one_num.replace(',', ''))
        if num > mx[idx]:
            mx[idx] = num
            mx_station[idx] = f'{one[3]} ({one[1]}{idx+4}시)'

print(mx_station)
print(mx)

import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)
plt.show()

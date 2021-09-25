import csv

f = open('202108_subtime.csv')
data = csv.reader(f)

header = next(data)
print(header)
print(next(data))

in_num = [0] * 24
out_num = [0] * 24

for one in data:
    in_out = one[4:len(header) - 1]
    for idx in range(24):
        in_num[idx] += int(in_out[idx * 2].replace(',', ''))
        out_num[idx] += int(in_out[idx * 2 + 1].replace(',', ''))
        print(idx, in_out[idx], out_num)

print(in_num)
print(out_num)

import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(in_num, label='승차')
plt.plot(out_num, label='하차')
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()

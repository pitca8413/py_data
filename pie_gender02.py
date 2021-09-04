import csv
import matplotlib.pyplot as plt

f = open('gender.csv', encoding='cp949')
data = csv.reader(f)

header = next(data)

number = 100
m_cnt = 0
f_cnt = 0

m_idx = header.index('2021년07월_남_0세')
f_idx = header.index('2021년07월_여_0세')

area = input('조회할 지역명: ')
for one in data:
    if area in one[0]:
        for idx in range(100):
            m_cnt += int(one[m_idx + idx].replace(',', ''))
            f_cnt += int(one[f_idx + idx].replace(',', ''))
        break

# 그래프 그리기
plt.rc('font', family='AppleGothic')
plt.title('범계동 지역의 남여 성별 인구')
label = ['남', '여']
plt.pie([m_cnt, f_cnt], labels=label, autopct='%.1f%%')
plt.legend()
plt.show()

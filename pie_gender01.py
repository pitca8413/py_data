import csv
import matplotlib.pyplot as plt

# 1. 파일 불러오기
f = open('gender.csv', encoding='cp949')
data = csv.reader(f)

header = next(data)

m_idx = header.index('2021년07월_남_0세')
f_idx = header.index('2021년07월_여_0세')

m_lst = []
f_lst = []

# 범계동 성별 인구 리스트 만들기
for one in data:
    if '범계' in one[0]:
        m_lst = one[m_idx:m_idx + 100]
        f_lst = one[f_idx:f_idx + 100]
        break

# 성별 인구 데이터 정리하기
m_lst = [one.replace(',', '') for one in m_lst]
m_lst = map(int, m_lst)
m_sum = sum(m_lst)
f_lst = [one.replace(',', '') for one in f_lst]
f_lst = map(int, f_lst)
f_sum = sum(f_lst)

# 성별 인구수 합 리스트 만들기
gen_data = [m_sum, f_sum]
print(gen_data)

# 그래프 그리기
plt.rc('font', family='AppleGothic')
plt.title('범계동 지역의 남여 성별 인구')
# label = [f'남\n{gen_data[0]}명', f'여\n{gen_data[1]}명']
label = ['남', '여']
plt.pie(gen_data, labels=label, autopct='%.1f%%')
plt.legend()
plt.show()

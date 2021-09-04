import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
data = [244, 231, 103, 123]
label = ['A', 'B', 'AB', 'O']
color=['darkmagenta', 'pink', 'skyblue', 'hotpink']
plt.axis('equal')
plt.title('혈액형 비율')
plt.pie(data, labels=label, autopct='%.1f%%', colors=color, explode=(0, 0, 0.1, 0))
plt.legend()
plt.show()

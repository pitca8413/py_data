import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
data = [244, 231, 103, 123]
label = ['A', 'B', 'AB', 'O']
plt.axis('equal')
plt.pie(data, labels=label)
plt.show()

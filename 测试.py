import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
path = 'E:\\jupyter-notebook\\20230219\\'
data=pd.read_excel(path+'不锈钢fs-1.1.xlsx')

X=data.iloc[:,0]
y=data.iloc[:,1]

# 寻找光谱峰
peaks, _ = sig.find_peaks(data.iloc[:, 1], height=1000)

# 匹配光谱峰与元素谱线
element_lines = {'Fe': [259.94, 259.96, 260.06, 260.08], 'Cu': [324.75, 327.39, 327.40]}
element = 'Fe'
match_lines = []
for p in peaks:
    for l in element_lines[element]:
        if abs(data[p, 0] - l) < 0.1:  # 匹配精度为0.1nm
            match_lines.append(p)
            break

# 计算元素含量
element_content = np.sum(data[match_lines, 1]) / np.sum(data[:, 1]) * 100  # 相对含量

print('The content of', element, 'is', element_content, '%')

p=plt.figure(figsize=(12,4))
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(X,y)
plt.show()


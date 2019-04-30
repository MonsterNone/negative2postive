# 测试
# 通过最小和最大的r/g/b分量计算y=kx+b公式然后替换

from PIL import Image
import numpy as np

import os

def single_np(arr, target):
    arr = np.array(arr)
    mask = (arr == target)
    arr_new = arr[mask]
    return arr_new.size


def reverse(p):
    ap = np.array(p)

    x1 = np.min(ap)
    x2 = np.max(ap)

    '''
    while True:
        if single_np(ap, x1) <= 1:
            x1 = x1 + 1
        else:
            break
    while True:
        if single_np(ap, x2) <= 1:
            x2 = x2 - 1
        else:
            break
    '''
    
    y1 = 255
    y2 = 0

    f_k = (y2 - y1) / (x2 - x1)
    f_b = y1 - f_k * x1

    tmp = ap * f_k + f_b
    return tmp


def process(file_name):
    src = Image.open('in/' + file_name)
    r, g, b = src.split()
    tmp_r = reverse(r)
    tmp_g = reverse(g)
    tmp_b = reverse(b)

    r = Image.fromarray(tmp_r).convert('L')
    g = Image.fromarray(tmp_g).convert('L')
    b = Image.fromarray(tmp_b).convert('L')

    img = Image.merge('RGB', (r, g, b))
    img.save('out/' + file_name[:-4] + '.jpg', dpi=(300,300))


print('本程序会读取in文件夹中的所有.tif文件并输出到out文件夹中。按回车继续')
input()


for i in os.listdir('in/'):
    if i[-4:] != '.tif':
        continue
    print('处理', i)
    process(i)

print('\n全部完成！按回车关闭程序。')
input()

# -*- coding: UTF-8 -*-
# 通过最小和最大的r/g/b分量计算y=kx+b公式然后替换

from PIL import Image, ImageCms
import numpy as np
import io
import os

srgb = ImageCms.createProfile('sRGB')


# https://stackoverflow.com/questions/31865743/pil-pillow-decode-icc-profile-information
def convert_to_srgb(icc_profile, img):
    f = io.BytesIO(icc_profile)
    icc = ImageCms.ImageCmsProfile(f)
    img = ImageCms.profileToProfile(img, icc, srgb)
    return img
    

def single_np(arr, target):
    arr = np.array(arr)
    mask = (arr == target)
    arr_new = arr[mask]
    return arr_new.size


def reverse(p):
    ap = np.array(p)

    x1 = np.min(ap)
    x2 = np.max(ap)

    while True:
        if single_np(ap, x1) <= 100 :
            x1 = x1 + 2
        else:
            print('x1 =', x1)
            break
    while True:
        if single_np(ap, x2) <= 100:
            x2 = x2 - 1
        else:
            print('x2 =', x2)
            break
    
    y1 = 255
    y2 = 0

    f_k = (y2 - y1) / (x2 - x1)
    f_b = y1 - f_k * x1

    tmp = ap * f_k + f_b

    return tmp


def process(file_name):
    src = Image.open('in/' + file_name)
    icc_profile = src.info.get('icc_profile', '')
    
    r, g, b = src.split()
    tmp_r = reverse(r)
    tmp_g = reverse(g)
    tmp_b = reverse(b)

    r = Image.fromarray(tmp_r).convert('L')
    g = Image.fromarray(tmp_g).convert('L')
    b = Image.fromarray(tmp_b).convert('L')

    img = Image.merge('RGB', (r, g, b))

    if icc_profile:
        print('色彩空间转换...')
        img = convert_to_srgb(icc_profile, img)
    img.save('out/' + file_name[:-4] + '.jpg',
             format = "JPEG",
             quality = 100,
             icc_profile=img.info.get('icc_profile', ''),
             dpi=(300,300))


print('本程序会读取in文件夹中的所有.tif文件并输出到out文件夹中。按任意键继续')
input()

for i in os.listdir('in/'):
    if i[-4:] != '.tif':
        continue
    print('处理', i)
    process(i)
    print()
    
print('全部完成！按任意键关闭程序。')
input()

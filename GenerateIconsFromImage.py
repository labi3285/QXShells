#!/usr/local/bin/python3

# 使用方法：将本代码放到图标的相同目录并执行，将生成dist目录

import sys
import os
import shutil
from PIL import Image # pip3 install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple

# 创建文件
def generate_text_file(file, text):
    fs = open(file, 'w')
    fs.write(text)
    fs.close()
    print('创建文件：' + file)

# 创建文件夹
def generate_fold(path):
    if not os.path.exists(path):
        os.makedirs(path) 
        print('创建路径：' + path)
        return True
    else:
        return False

# 生成图标
def generate_icons_from_image_file(file, out_path):
    (file_path, file_name) = os.path.split(file)
    (file_name, extension) = os.path.splitext(file_name)    
    image = Image.open(file)
    (w,h) = image.size

    out_image_set_path = os.path.join(out_path, file_name + '.imageset')
    generate_fold(out_image_set_path)
    generate_text_file(os.path.join(out_image_set_path, 'Contents.json'), '{"images":[{"idiom":"universal","filename":"icon@1x.png","scale":"1x"},{"idiom":"universal","filename":"icon@2x.png","scale":"2x"},{"idiom":"universal","filename":"icon@3x.png","scale":"3x"}],"info":{"version":1,"author":"xcode"}}')
    
    for s in [1, 2, 3]:
        out_image = image.resize((30 * s, 30 * s), Image.ANTIALIAS)
        out_image_path = os.path.join(out_image_set_path, 'icon@' + str(s) + 'x.png')
        out_image.save(out_image_path)
        print('创建图片：' + out_image_path)

# 批量生成图标
def generate_icons_from_image_fold(path):
    out_path = os.path.join(path, 'dist')
    if os.path.exists(out_path):
        shutil.rmtree(out_path)

    for root, dirs, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith('.png'):
                generate_icons_from_image_file(os.path.join(root, file_name), out_path)
        break


def main():
    generate_icons_from_image_fold(sys.path[0])

if __name__ == '__main__':
    main()




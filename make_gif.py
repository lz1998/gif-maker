import os
import imageio
from PIL import Image

INPUT_DIR = 'src'  # 输入文件夹
OUTPUT_FILE = 'output.gif'  # 输出文件
DURATION = 0.1  # 间隔(秒)
MAX_WIDTH = 300  # 图片最大宽度
MAX_HEIGHT = 300  # 图片最大高度


def compress_image(img):
    '''压缩图片'''
    img.convert('RGB')
    w, h = img.size
    scale = min(MAX_WIDTH / w, MAX_HEIGHT / h)  # 计算压缩比
    if scale < 1:
        w *= scale
        h *= scale
        img = img.resize((int(w), int(h)), Image.ANTIALIAS)  # 压缩图片
    return img


img_file_list = os.listdir(INPUT_DIR)  # 获取输入文件夹下的所有文件
img_file_list.sort()  # 根据名称排序

img_file_list = [INPUT_DIR + '/' + img_file for img_file in img_file_list]  # 拼接文件名

gif_frames = []
for img_file in img_file_list:
    print(img_file)
    img = Image.open(img_file)  # 读入图片
    img = compress_image(img)  # 压缩图片
    gif_frames.append(img)  # 加入GIF

imageio.mimsave(OUTPUT_FILE, gif_frames, 'GIF', duration=DURATION)  # 生成并保存文件
print('OK')

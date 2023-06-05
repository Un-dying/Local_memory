'''
1.输入url，存为url_main
2.定义变量image_path，值为word/media/image
3.开始循环，定义变量image_name，初始值为1.jpg，此后每次循环image_name+1，拼合url，image_path，image_name，存为image_path_all，以get方式打开image_path_all，如果返回状态码为200，保存图片在本地/new/word/media，并打印image_name下载成功，如果返回404，中止程序

'''
import requests
import os
from read import url_list

a = 0
a_1 = '0'
while a < len(url_list):
    flag = True
    url_read_a = str(url_list[a])
    url_read = url_read_a[2:-2]
    url_main = url_read
    image_jpgend = '.jpg'
    image_pngend = '.png'
    image_path = 'word/media/image'
    image_name = '1'
    i_n = 1
    image_path_all = url_main + image_path + image_name + image_jpgend
    image = requests.get(image_path_all)
    if os.path.exists('cache/' + a_1 + '/word/media') == False:
        os.makedirs('cache/' + a_1 + '/word/media')   
    print(url_read)
    while flag == True:
        if image.status_code == 200:
            with open('cache/' + a_1 + '/word/media/image' + image_name + '.jpg', 'wb') as f:
                f.write(image.content)
            print('image' + image_name + '.jpg 获取成功')
            image_name = str(int(image_name) + 1)
            image_path_all = url_main + image_path + image_name + image_jpgend
            image = requests.get(image_path_all)
        elif image.status_code == 404:
            image_path_all = url_main + image_path + image_name + image_pngend
            image = requests.get(image_path_all)
            if image.status_code == 404:
                flag = False
                print('image' + image_name + '.png 获取失败')
                continue
            else:
                with open('cache/' + a_1 + '/word/media/image' + image_name + '.png', 'wb') as f:
                    f.write(image.content)
                print('image' + image_name + '.png 获取成功')
                image_name = str(int(image_name) + 1)
                image_path_all = url_main + image_path + image_name + image_jpgend
                image = requests.get(image_path_all)
    a = a + 1
    a_1 = str(int(a_1) + 1)
#    print(a_1)
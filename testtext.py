'''
1.输入url，存为url_main
2.定义变量html_num和html_end，值分别为0和.html
3.拼合url_main，html_num，html_end，存为url_all
4.定义空变量html_all，形式为string
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
    if os.path.exists('cache/' + a_1) == False:
        os.makedirs('cache/' + a_1)   
    html_num = '0'
    html_end = '.html'
    url_all = url_main + html_num + html_end
#html_1 = requests.get(url_all).text
    html_1 = ''
    flag = True
    html_2 = html_1
    while flag == True:
        if requests.get(url_all).status_code == 200:
            print('page' + html_num + '获取成功')
            html_1 = requests.get(url_all).text
            html_2 = html_2 + html_1
            html_num = str(int(html_num) + 1)
            url_all = url_main + html_num + html_end
        elif requests.get(url_all).status_code == 404:
            with open('cache/' + a_1 + '/document.html', 'w', encoding='utf-8') as f:
                f.write(html_2)
            flag = False
            print('page' + html_num + '获取失败')
            print('document.html 获取成功')
            continue
    a = a + 1
    a_1 = str(int(a_1) + 1)
    print(a_1)
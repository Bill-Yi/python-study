'''

tag=soup.find(name='title') #获取title标签
print(tag.string)  #title标签里面的内容

#获取超链接
tags=soup.find_all(name='a') #获取a标签
for tag in tags:
    print(tag['href'])#获取的a标签的属性值

#具有class="sister"的所有标签
tags=soup.find_all(attrs={'class':"sister"})
for tag in tags:
    print(tag)

def myFilter(tag):
    if (tag.text).endswith('cie'):
        print(tag)

soup=BeautifulSoup(content,"html.parser")
tags=soup.find_all("a")
for tag in tags:
    myFilter(tag)

soup=BeautifulSoup(content,"html.parser")
tags=soup.find_all("p")
#while tag:
   # print(tag.name)
    #tag=tag.parent
for tag in tags:
    for x in tag.descendants:  #获取第一个p标签的子孙节点
        print(x)


soup=BeautifulSoup(content,"html.parser")
#tags=soup.find("a")
#print(tags.next_sibling) #右兄弟
tags=soup.find("body")
print(tags.previous_sibling) #左兄弟

'''
# *******************2019年中国大学排名表*********************************************

import requests
import bs4
from bs4 import BeautifulSoup
from openpyxl import Workbook  # 操作excel表格


# 1.获取网页
def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                      '(KHTML, like Gecko) Chrome/64.0.3282.140Safari/537.36 Edge/17.17134'}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.content


# 2.解析网页
def fillUlist(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])
    return ulist


# 3.保存数据
def save_UnivList(ulist):
    fn = r"中国大学2019年排名表.xlsx"
    wb = Workbook()  # 创建工作簿
    ws = wb.worksheets[0]  # 第一张表
    ws.title = "2019中国大学排名信息表"  # 更改表的名称
    ws.append(["2019排名", "学校名称", "省份", "分数"])  # 添加表头信息
    for i in range(len(ulist)):  # 前num名学校信息
        u = ulist[i]
        ws.append(u)
    wb.save(fn)  # 保存工作簿


url = r'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
html = getHtml(url)
ulist = []
univerList = fillUlist(html, ulist)
save_UnivList(univerList)

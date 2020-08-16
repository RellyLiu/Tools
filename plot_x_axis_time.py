#!/usr/bin/python
#coding=utf-8

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # 打开文本文件 读取数据
    with open("data.txt", 'r') as f:
        data_lines = f.readlines()

    l_time    = []
    l_article = []
    l_fans    = []
    l_like    = []
    l_remark  = []
    l_level   = []
    l_visit   = []
    l_score   = []
    l_rank    = []

    num = len(data_lines)

    # ################
    #     整理数据
    # ################
    for i in range(0,num):
        line = data_lines[i]
        if len(line) < 2:
            continue    #这行明显不是有效信息

        data = line.split(' ')
        time = data[0]
        # 使用最新日期的数据
        if len(l_time) != 0:
            #如果这一行时间与上一行的时间相等，删除上一行数据
            if time == l_time[-1]:
                print('删除上一行:' + time)
                l_time.pop(-1) #删除上一行记录的数据
                l_article.pop(-1)
                l_fans.pop(-1)
                l_like.pop(-1)
                l_remark.pop(-1)
                l_level.pop(-1)
                l_visit.pop(-1)
                l_score.pop(-1)
                l_rank.pop(-1)


        arti = int(data[1])
        fans = int(data[2])
        like = int(data[3])
        rmak = int(data[4])
        leve = int(data[5])
        visi = int(data[6])
        scor = int(data[7])
        rank = int(data[8])
        l_time.append(time)
        l_article.append(arti)
        l_fans.append(fans)
        l_like.append(like)
        l_remark.append(rmak)
        l_level.append(leve)
        l_visit.append(visi)
        l_score.append(scor)
        l_rank.append(rank)

    # ################
    #       画图
    # ################
    # X坐标，将str类型的数据转换为datetime.date类型的数据，作为x坐标
    #xs = [datetime.strptime(d, '%Y/%m/%d').date() for d in l_time] 时间是年/月/日
    xs = [datetime.strptime(d, '%H:%M:%S.%f') for d in l_time]
    
    plt.figure(1)
#    plt.subplot(1, 3, 1)
    plt.title('Visit Number')
    plt.plot(xs, l_visit, 'o-')
    plt.xlabel('Time')
    plt.ylabel('Visit Number')

    # 只画最后一个元素点 - 数据点在文字的↘右下，文字在↖左上
    plt.text(xs[-1], l_visit[-1], l_visit[-1], ha='right', va='bottom', fontsize=10)


#    plt.subplot(1, 3, 2)
#    plt.title('Rank')
#    plt.plot(xs, l_rank, 'o-')
#    plt.xlabel('Time')
#    plt.ylabel('Rank')
#    # 只画最后一个元素点 - 数据点在文字的↗右上，文字在↙左下
#    plt.text(xs[-1], l_rank[-1], l_rank[-1], ha='right', va='top', fontsize=10)
#
#
#
#    plt.subplot(1, 3, 3)
#    plt.title('Score')
#    plt.plot(xs, l_score, 'o-')
#    plt.xlabel('Time')
#    plt.ylabel('Score')
#    # 只画最后一个元素点 - 数据点在文字的↘右下，文字在↖左上
#    plt.text(xs[-1], l_score[-1], l_score[-1], ha='right', va='bottom', fontsize=10)


#    plt.gcf().autofmt_xdate()  # 自动旋转日期标记

    # show
    plt.show()

import os
import datetime
import sqlite3

from neu_news_interface import get_content
class test:
    def __init__(self):
        self.pid = []
        self.con = sqlite3.connect('./users.db')  # 打开数据库 没有则创建
        self.cur = self.con.cursor()  # 获取游标
    def view_post(self):  # 查看帖子
        global res
        print("选择查看帖子的方式：1.按时间/热度排序 2.按类别排序  3.根据输入内容进行查找")
        k = int(input())
        while not 1 <= k <= 3:
            k = int(input())
        post_actor = post()
        if k == 1:  # 按类别
            res = post_actor.sort_post()
        elif k == 2:  # 按时间或者热度排序
            res = post_actor.select_post()
        else:
            res = post_actor.find_content()
        # res = self.cur.execute('SELECT * from post where label1 = ?',(label[k-1][1],))
        title = []
        content = []
        print(res)
        for i in res:
            # 类别 +  标题 + 作者 + 发帖时间 + 评论数量
            print(i[6])
            name = self.cur.execute("SELECT name from user where id = ?", (i[6],)).fetchone()
            print(name)
            string = str(i[1]) + ' ' + str(i[8]) + ' ' + name[0] + ' ' + str(i[5]) + ' ' + str(i[4])
            self.pid.append(i[0])
            content.append(i[-3])
            title.append(string)
        print(title)
        print("请选择你选择的是第几个帖子 1~10")
        k = int(input())
        content0 = content[k - 1]  # 内容
        content1 = []  # 评论
        comment = self.cur.execute("SELECT reply from comment where post_id = ?", (self.pid[k - 1],))
        for i in comment:
            content1.append(i[0])
        print(content0, content1)


    def result_key(self,content):
        sql = 'SELECT * FROM post WHERE content like ? or title like ?'
        res2 = self.cur.execute(
            sql, ('%' + content + '%', '%' + content + '%',))
        title = ["空", "空", "空", "空", "空", "空", "空", "空", "空", "空"]
        k = 0
        for i in res2:
            # 类别 +  标题 + 作者 + 发帖时间 + 评论数量
            name = self.cur.execute("SELECT name from user where id = ?", (i[6],)).fetchone()
            string = str(i[1]) + ' ' + str(i[8]).title() + ' ' + name[0] + ' ' + str(i[5]) + ' ' + str(i[4])
            title[k] = string
            k = k+1
            #title.append(string)
        return title


class post():
    def __init__(self):
        self.con = sqlite3.connect('./users.db')  # 打开数据库 没有则创建
        self.cur = self.con.cursor()  # 获取游标

    def sort_post(self):  # 排序帖子
        global res
        print('请选择排序方式')
        num = int(input('0 最新发布；1 最高热度'))
        if num == 0:
            sql = 'select * from post order by time desc'
            res = self.cur.execute(sql)
            self.con.commit()
        if num == 1:
            sql = 'select * from post order by count desc'
            res = self.cur.execute(sql)
            self.con.commit()
        return res

    def select_post(self):  # 筛选帖子
        print('请选择筛选方式')
        label = ((1, "活动"), (2, "闲聊"), (3, "交友"), (4, "自习"),
                (5, "拼单"), (6, "交易"), (7, "咨询"), (8, "公告"))
        print("请选择你发布帖子的类别：1 活动 2 闲聊 3 交友 4 自习 5 拼单 6 交易 7 咨询 8 公告")
        k = int(input())
        while not 1 <= k <= 8:
            k = int(input())
        tag = label[k - 1][1]
        sql = "select * from post where label1=?"
        res1 = self.cur.execute(sql, (tag,))
        return res1

    def find_content(self):
        print("请选择输入要查找帖子的标题或内容")
        content = input("输入贴子标题/内容（部分）")
        sql = 'SELECT * FROM post WHERE content like ? or title like ?'
        res2 = self.cur.execute(
            sql, ('%' + content + '%', '%' + content + '%',))
        return res2
if __name__ == "__main__":
    t=test()
    t.view_post()
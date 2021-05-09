import sqlite3
import datetime

con = sqlite3.connect('./users.db')  # 打开数据库 没有则创建
cur = con.cursor()  # 获取游标
"""
user表中
name表示其名称   id 唯一标识用户账号 注册时随机生成  password 密码
attribute 表示身份为用户user/管理员admin  state 表示用户是否被加锁 1加锁 0 解锁
question - answer 为密码问题 用于用户忘记密码时找回
"""
# 创建用户表
cur.execute('''CREATE TABLE  IF NOT EXISTS  
              user(
              id INTEGER PRIMARY KEY,
              name VARCHAR(30),
              password CHAR(8),
              attribute VARCHAR(6),
              state INTEGER,
              question VARCHAR(50),
              answer VARCHAR(50))'''
            )  # 调用SQL语句
con.commit()  # 提交

# 创建帖子表
'''
post_id 唯一标识帖子 可以用一个全局变量从1开始分配
label 表示 闲置二手/交友/自习等等
count 评论数  time 发布时间 可以用两者进行排序
uid 发布者id   content title 标题和内容
top  标识该帖子是否置顶
'''
cur.execute('''CREATE TABLE  IF NOT EXISTS  
              post(
              post_id INTEGER PRIMARY KEY,
              label1 TEXT,
              label2 TEXT,
              label3 TEXT,
              count INTEGER,
              time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
              uid INTEGER,
              content TEXT,
              title TEXT,
              top INTEGER,
              FOREIGN KEY(uid) REFERENCES user(id))'''
            )  # 调用SQL语句
con.commit()  # 提交

# 插入时间的方法
# INSERT INTO t2 VALUES (CURRENT_TIMESTAMP);

# 创建评论表
'''
 post_id 帖子id
 rid 回复者id   reply 回复内容
'''
cur.execute('''CREATE TABLE IF NOT EXISTS 
                comment(
                post_id INTEGER,
                rid INTEGER,
                reply TEXT,
                FOREIGN KEY(post_id) REFERENCES post(post_id) ON DELETE CASCADE,
                FOREIGN KEY(rid) REFERENCES user(id) ON DELETE CASCADE
                )''')  # 调用SQL语句
con.commit()  # 提交

# cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
#             '("安凯凯",20182369,"12345678","user",0,"生日是什么时候","2000-02-14")')
# con.commit()
#
# cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
#             '("刘济霆",20182499,"12345678","admin",0,"爱好是什么","套娃")')
# con.commit()
# cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
#             '("丁子恒",20181111,"12345678","user",0,"爱好是什么","套娃")')
# con.commit()

'''
con = sqlite3.connect('./users.db')  # 打开数据库 没有则创建
cur = con.cursor()  # 获取游标


cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
             '("安凯凯",20182369,"akk12345","admin",0,"生日是什么时候","2000-02-14")')
con.commit()

cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
             '("刘济霆",20182499,"12345678","admin",0,"爱好是什么","套娃")')
con.commit()
cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
             '("丁子恒",20181111,"12345678","user",0,"爱好是什么","套娃")')
con.commit()
cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
             '("卖鱼强",20185656,"12345678","user",0,"替身是什么","白金之星")')
con.commit()
cur.execute('INSERT INTO user(name,id,password,attribute,state,question,answer) VALUES '
            '("擦镜人",20182333,"12345678","user",0,"王骨是什么","钜子舌")')
con.commit()


cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (1,"交易",null,null,4,CURRENT_TIMESTAMP,20181111,"有人买吗","出洗发膏",0)')
con.commit()
cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (1,20182499,"我要")')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
             'VALUES (1,20182499,"多少钱一瓶")')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
             'VALUES (1,20182499,"在哪交易")')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (1,20182499,"怎么联系")')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (17,"活动","校级",null,0,CURRENT_TIMESTAMP,20182369,"暑期夏令营","XX大学暑期夏令营",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
             'VALUES (2,"公告",null,null,3,CURRENT_TIMESTAMP,20182369,"四六级成绩查询","四六级考试成绩查询已开放，请大家到www.wbzdssm.com.cn官网自行查询",0)')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (2,20181111,"好耶")')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (2,20182333,"好耶")')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (2,20185656,"好耶")')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (3,"公告",null,null,0,CURRENT_TIMESTAMP,20182369,"停水通知","因水管检修，5月31日下午停水，请大家做好停水准备",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (4,"活动","院级","计算机学院",0,CURRENT_TIMESTAMP,20182333,"考研讲座","上岸前辈讲述亲身经历，可加二课分，报名从速",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (5,"活动","校级",null,0,CURRENT_TIMESTAMP,20181111,"校庆活动征集","如题，征集校庆活动，包括但不限于歌舞、杂技、曲艺、相声、魔术，报名者请联系团支部***",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (6,"活动","校级",null,0,CURRENT_TIMESTAMP,20181111,"校庆活动征集","如题，征集校庆活动，包括但不限于歌舞、杂技、曲艺、相声、魔术，报名者请联系团支部***",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (7,"交友",null,null,0,CURRENT_TIMESTAMP,20185656,"轻音部招新","欢迎热爱乐队的同学参与！",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (8,"咨询",null,null,1,CURRENT_TIMESTAMP,20182333,"咨询跨考计算机学院研究生相关事宜","rt，有偿，欢迎dd",0)')
con.commit()

cur.execute('INSERT INTO comment(post_id,rid,reply)'
            'VALUES (8,20185656,"加Q详谈，12345")')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (9,"自习",null,null,0,CURRENT_TIMESTAMP,20185656,"约图书馆","跨考生物，来个研友一起啊",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (10,"公告",null,null,0,CURRENT_TIMESTAMP,20182499,"东北大学98周年生日快乐！","东北大学98周年生日快乐！",1)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (11,"活动","校级",null,0,CURRENT_TIMESTAMP,20182499,"华服日","华服日活动，周日早上9：00，南湖公园北侧集合",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (12,"活动","校级",null,0,CURRENT_TIMESTAMP,20182369,"雏鹰计划志愿招募","去小学为学生教授基础课程",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
             'VALUES (13,"活动","校级",null,0,CURRENT_TIMESTAMP,20185656,"运动会观众排练","校运动会观众排练，5月12日早9：00五四体育场",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (14,"活动","校级",null,0,CURRENT_TIMESTAMP,20181111,"建党一百周年晚会","7月1日晚18：00，大活多功能厅，观众凭票入场",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (15,"活动","院级","文法学院",0,CURRENT_TIMESTAMP,20182333,"模拟法庭","欢迎报名，也欢迎参观",0)')
con.commit()

cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
            'VALUES (16,"活动","校级",null,0,CURRENT_TIMESTAMP,20185656,"玄机科技校园行","线下取票时间5月1日9：00食堂三楼活动室一",0)')
con.commit()
'''

cursor = cur.execute('SELECT * from user')
for i in cursor:
    print(i)

# cur.execute('INSERT INTO post(post_id,label1,label2,label3,count,time,uid, content,title,top)'
#             'VALUES (1,"交易",null,null,4,CURRENT_TIMESTAMP,20181111,"有人买吗","出洗发膏",0)')
# con.commit()
#
# cur.execute('INSERT INTO comment(post_id,rid,reply)'
#             'VALUES (1,20182499,"多少钱一瓶")')
# con.commit()

cursor = cur.execute('SELECT * from post')
for i in cursor:
    print(i)

for i in cursor:
    print(i)

# cursor = cur.execute('SELECT * from comment')
# for i in cursor:
#     print(i)

con.close()
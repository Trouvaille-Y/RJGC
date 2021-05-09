from PySide2.QtGui import QPixmap
from function import *
import win32con
from edition4 import *
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import win32api

class test:
    def __init__(self):
        self.flag=[]
        self.club_num=0
        self.notice_num=0
        self.news_num=0
        self.tiezinum=0
        window1 = QFile('./登录.ui')
        window2 = QFile('./注册.ui')
        window3 = QFile('./密保.ui')
        window4 = QFile('./ID.ui')
        window5 = QFile('./主页.ui')
        window6 = QFile('./组织.ui')
        window7 = QFile('./新闻.ui')
        window8 = QFile('./公告.ui')
        window9 = QFile('./论坛.ui')
        window10 = QFile('./退出询问.ui')
        window11 = QFile('./忘记.ui')
        window12 = QFile('./忘记密码.ui')
        window13 = QFile('./修改密码.ui')
        window14 = QFile('./新闻内容.ui')
        window15 = QFile('./公告内容.ui')
        window16 = QFile('./帖子内容.ui')
        window17 = QFile('./发布帖子.ui')
        window18 = QFile('./管理员.ui')
        window19 = QFile('./发布公告.ui')
        window20 = QFile('./管理用户.ui')
        window21 = QFile('./管理帖子.ui')

        window1.open(QFile.ReadOnly)
        window2.open(QFile.ReadOnly)
        window3.open(QFile.ReadOnly)
        window4.open(QFile.ReadOnly)
        window5.open(QFile.ReadOnly)
        window6.open(QFile.ReadOnly)
        window7.open(QFile.ReadOnly)
        window8.open(QFile.ReadOnly)
        window9.open(QFile.ReadOnly)
        window10.open(QFile.ReadOnly)
        window11.open(QFile.ReadOnly)
        window12.open(QFile.ReadOnly)
        window13.open(QFile.ReadOnly)
        window14.open(QFile.ReadOnly)
        window15.open(QFile.ReadOnly)
        window16.open(QFile.ReadOnly)
        window17.open(QFile.ReadOnly)
        window18.open(QFile.ReadOnly)
        window19.open(QFile.ReadOnly)
        window20.open(QFile.ReadOnly)
        window21.open(QFile.ReadOnly)

        self.window_1 = QUiLoader().load(window1)
        self.window_1.setWindowTitle('登录')
        self.window_2 = QUiLoader().load(window2)
        self.window_2.setWindowTitle('注册')
        self.window_3 = QUiLoader().load(window3)
        self.window_3.setWindowTitle('注册')
        self.window_4 = QUiLoader().load(window4)
        self.window_4.setWindowTitle('注册')
        self.window_5 = QUiLoader().load(window5)
        self.window_5.setWindowTitle('123456')
        self.window_6 = QUiLoader().load(window6)
        self.window_6.setWindowTitle('组织')
        self.window_7 = QUiLoader().load(window7)
        self.window_7.setWindowTitle('新闻')
        self.window_8 = QUiLoader().load(window8)
        self.window_8.setWindowTitle('公告')
        self.window_9 = QUiLoader().load(window9)
        self.window_9.setWindowTitle('论坛')
        self.window_10 = QUiLoader().load(window10)
        self.window_10.setWindowTitle('退出')
        self.window_11 = QUiLoader().load(window11)
        self.window_11.setWindowTitle('忘记密码')
        self.window_12 = QUiLoader().load(window12)
        self.window_12.setWindowTitle('忘记密码')
        self.window_13 = QUiLoader().load(window13)
        self.window_13.setWindowTitle('修改密码')
        self.window_14 = QUiLoader().load(window14)
        self.window_14.setWindowTitle('新闻')
        self.window_15 = QUiLoader().load(window15)
        self.window_15.setWindowTitle('公告')
        self.window_16 = QUiLoader().load(window16)
        self.window_16.setWindowTitle('帖子')
        self.window_17 = QUiLoader().load(window17)
        self.window_17.setWindowTitle('发布')
        self.window_18 = QUiLoader().load(window18)
        self.window_18.setWindowTitle('管理员')
        self.window_19 = QUiLoader().load(window19)
        self.window_19.setWindowTitle('发布公告')
        self.window_20 = QUiLoader().load(window20)
        self.window_20.setWindowTitle('发布用户')
        self.window_21 = QUiLoader().load(window21)
        self.window_21.setWindowTitle('发布帖子')


        self.window_1.check.clicked.connect(self.show_zhuye)
        self.window_1.new_2.clicked.connect(self.show_zhuce)
        self.window_1.forget.clicked.connect(self.show_forget)
        self.window_2.pb1.clicked.connect(self.show_mibao)
        self.window_2.pb2.clicked.connect(self.show_denglu)
        self.window_3.pb1.clicked.connect(self.show_id)
        self.window_3.pb2.clicked.connect(self.show_zhuce)
        self.window_4.pb1.clicked.connect(self.sertdb)
        self.window_4.pb2.clicked.connect(self.show_mibao)
        self.window_5.pb1.clicked.connect(self.show_zuzhi)
        self.window_5.pb2.clicked.connect(self.show_xinwen)
        self.window_5.pb3.clicked.connect(self.show_gonggao)
        self.window_5.pb4.clicked.connect(self.show_tiezi)
        self.window_5.pb5.clicked.connect(self.show_guanlijiemian)
        self.window_5.tui.clicked.connect(self.show_denglu)
        self.window_5.exit.clicked.connect(self.show_xunwen)

        self.window_6.back.clicked.connect(self.goback)
        self.window_6.pb2.clicked.connect(self.setclnum1)
        self.window_6.pb3.clicked.connect(self.setclnum2)
        self.window_6.pb4.clicked.connect(self.setclnum3)
        self.window_6.pb5.clicked.connect(self.setclnum4)
        self.window_6.pb6.clicked.connect(self.setclnum5)
        self.window_6.pb7.clicked.connect(self.setclnum6)
        self.window_6.pb8.clicked.connect(self.setclnum7)
        self.window_6.pb9.clicked.connect(self.setclnum8)
        self.window_6.pb10.clicked.connect(self.setclnum9)
        self.window_6.pb11.clicked.connect(self.setclnum10)

        self.window_7.back.clicked.connect(self.goback)
        self.window_7.b1.clicked.connect(self.setnewnum1)
        self.window_7.b2.clicked.connect(self.setnewnum2)
        self.window_7.b3.clicked.connect(self.setnewnum3)
        self.window_7.b4.clicked.connect(self.setnewnum4)
        self.window_7.b5.clicked.connect(self.setnewnum5)
        self.window_7.b6.clicked.connect(self.setnewnum6)
        self.window_7.b7.clicked.connect(self.setnewnum7)
        self.window_7.b8.clicked.connect(self.setnewnum8)
        self.window_7.b9.clicked.connect(self.setnewnum9)
        self.window_7.b10.clicked.connect(self.setnewnum10)

        self.window_8.back.clicked.connect(self.goback)
        self.window_8.b1.clicked.connect(self.setnonum1)
        self.window_8.b2.clicked.connect(self.setnonum2)
        self.window_8.b3.clicked.connect(self.setnonum3)
        self.window_8.b4.clicked.connect(self.setnonum4)
        self.window_8.b5.clicked.connect(self.setnonum5)
        self.window_8.b6.clicked.connect(self.setnonum6)
        self.window_8.b7.clicked.connect(self.setnonum7)
        self.window_8.b8.clicked.connect(self.setnonum8)
        self.window_8.b9.clicked.connect(self.setnonum9)
        self.window_8.b10.clicked.connect(self.setnonum10)

        self.window_9.back.clicked.connect(self.goback)
        self.window_9.phot.clicked.connect(self.show_hotresult)
        self.window_9.ptime.clicked.connect(self.show_timeresult)
        self.window_9.p1.clicked.connect(self.show_p1result)
        self.window_9.p2.clicked.connect(self.show_p2result)
        self.window_9.p3.clicked.connect(self.show_p3result)
        self.window_9.p4.clicked.connect(self.show_p4result)
        self.window_9.p5.clicked.connect(self.show_p5result)
        self.window_9.p6.clicked.connect(self.show_p6result)
        self.window_9.p7.clicked.connect(self.show_p7result)
        self.window_9.p8.clicked.connect(self.show_p8result)
        self.window_9.b1.clicked.connect(self.settiezinum1)
        self.window_9.b2.clicked.connect(self.settiezinum2)
        self.window_9.b3.clicked.connect(self.settiezinum3)
        self.window_9.b4.clicked.connect(self.settiezinum4)
        self.window_9.b5.clicked.connect(self.settiezinum5)
        self.window_9.b6.clicked.connect(self.settiezinum6)
        self.window_9.b7.clicked.connect(self.settiezinum7)
        self.window_9.b8.clicked.connect(self.settiezinum8)
        self.window_9.b9.clicked.connect(self.settiezinum9)
        self.window_9.b10.clicked.connect(self.settiezinum10)
        self.window_9.search.clicked.connect(self.show_keyresult)
        self.window_9.fabu.clicked.connect(self.show_fabutiezi)


        self.window_10.pb1.clicked.connect(self.tuichu)
        self.window_10.pb2.clicked.connect(self.nottuichu)

        self.window_11.pb1.clicked.connect(self.yanzhengid)
        self.window_11.pb2.clicked.connect(self.show_denglu)

        self.window_12.pb1.clicked.connect(self.yanzhengmibao)
        self.window_12.pb2.clicked.connect(self.show_denglu)

        self.window_13.pb1.clicked.connect(self.changecode)
        self.window_13.pb2.clicked.connect(self.show_denglu)

        self.window_14.back.clicked.connect(self.goback_news)
        self.window_15.back.clicked.connect(self.goback_notices)
        self.window_16.back.clicked.connect(self.goback_luntan)
        self.window_17.back.clicked.connect(self.goback_luntan1)
        self.window_18.back.clicked.connect(self.goback)
        self.window_19.back.clicked.connect(self.goback_guanli)
        self.window_20.back.clicked.connect(self.goback_guanli)
        self.window_21.back.clicked.connect(self.goback_guanli)

        self.window_16.content.clicked.connect(self.fabiaopinglun)
        self.window_17.ok.clicked.connect(self.fabiaotiezi)
        self.window_18.p1.clicked.connect(self.fagonggao)
        self.window_18.p2.clicked.connect(self.guanyonghu)
        self.window_18.p3.clicked.connect(self.guantiezi)
        self.window_19.ok.clicked.connect(self.announce)

        self.window_20.pb1.clicked.connect(self.lock)
        self.window_20.pb2.clicked.connect(self.unlock)

        self.window_21.pb1.clicked.connect(self.zhiding)
        self.window_21.pb2.clicked.connect(self.delete)
        self.window_21.pb3.clicked.connect(self.sousuo)

    def show_zhuce(self):   #点击注册按钮，进入注册界面
        self.window_1.close()
        self.window_3.close()
        self.window_2.show()

    def show_denglu(self):  #进入登录界面
        self.window_2.close()
        self.window_3.close()
        self.window_4.close()
        self.window_5.close()
        self.window_11.close()
        self.window_12.close()
        self.window_13.close()
        self.window_1.id.clear()
        self.window_1.code.clear()
        self.window_1.id.setFocus()
        self.window_1.show()

    def show_zhuye(self):  #进入主页
        id=self.window_1.id.text()
        password=self.window_1.code.text()
        assess_number=visitor.log_in(v,id,password)
        if assess_number==1:  #登陆成功
            self.window_1.close()
            self.window_2.close()
            self.window_5.show()
        elif assess_number==2:  #账号错误
            win32api.MessageBox(0, '账号不存在，请重新确认或注册新账户！', 'error', win32con.MB_OK)
            self.window_1.id.clear()
            self.window_1.code.clear()
            self.window_1.id.setFocus()
        else:  #密码错误
            win32api.MessageBox(0, '密码错误，请重新确认或点击忘记密码进行修改', 'error', win32con.MB_OK)
            self.window_1.code.clear()
            self.window_1.code.setFocus()
    def show_mibao(self):  #注册输入姓名和密码
        name = self.window_2.id.text()
        password = self.window_2.code.text()
        password2 = self.window_2.code1.text()
        if name != "" and password != "" and password2 != "":
            register_number = visitor.register(v, name, password, password2)
            if register_number == 1:
                win32api.MessageBox(0, '两次输入的密码不一致，请重新输入！', 'error', win32con.MB_OK)
                self.window_2.code.clear()
                self.window_2.code1.clear()
            else:  #注册成功，进入密保界面
                self.window_2.close()
                self.window_4.close()
                self.window_3.answer.clear()
                self.window_3.show()
        else:
            win32api.MessageBox(0, '请输入正确格式', 'error', win32con.MB_OK)
            return

    def sertdb(self):  #将id插入数据库，生成新用户
        visitor.insertdb(v)
        win32api.MessageBox(0, '注册成功！', '123456', win32con.MB_OK)
        self.window_4.close()
        self.window_1.id.clear()
        self.window_1.code.clear()
        self.window_1.show()


    def show_forget(self):  #进入忘记密码界面
        self.window_1.close()
        self.window_11.id.clear()
        self.window_11.show()
        win32api.MessageBox(0, '您将进入密码修改阶段！', '注意', win32con.MB_OK)

    def show_id(self):  #密保界面输入密保问题答案
        mibao_number = visitor.mibao(v,self.window_3.wenti.currentText(),self.window_3.answer.text())
        if mibao_number == 0:
            win32api.MessageBox(0, '密保答案不能为空，请重新输入', 'error', win32con.MB_OK)
            self.window_3.answer.setFocus()
        else:  #密保问题回答正确，生成id
            id = visitor.crearte_id(v)
            self.window_3.close()
            self.window_4.id.setText(id)
            self.window_4.show()

    def yanzhengid(self):  #修改密码前输入id，验证id是否存在
        self.flag = visitor.panduid(v,self.window_11.id.text())
        if self.flag :  #id存在，打开密保问题验证界面
            print(self.flag)
            self.window_11.close()
            self.window_12.wenti.setText(self.flag[5])
            self.window_12.show()
        else:
            win32api.MessageBox(0, '账号输入有误，请检查账号是否正确', 'error', win32con.MB_OK)
            self.window_11.id.clear()
            self.window_11.id.setFocus()

    def yanzhengmibao(self):  #验证密保问题
        answer = self.window_12.answer.text()
        if answer!=self.flag[6]:
            win32api.MessageBox(0, '密保答案错误', 'error', win32con.MB_OK)
            self.window_12.answer.clear()
            self.window_12.answer.setFocus()
        else:  #验证成功，打卡设置新密码界面
            self.window_12.close()
            self.window_13.show()

    def changecode(self):  #设置新密码
        password = self.window_13.code.text()
        password2 = self.window_13.code1.text()
        if password=="" or password2=="":
            win32api.MessageBox(0, '两次输入的密码不一致，请重新输入！', 'error', win32con.MB_OK)
            return
        if password!=password2:
            win32api.MessageBox(0, '两次输入的密码不一致，请重新输入！', 'error', win32con.MB_OK)
            self.window_13.code.clear()
            self.window_13.code1.clear()
        elif password==password2:  #设置成功，返回登录
            visitor.update_newcode(v,self.flag[0],password)
            win32api.MessageBox(0, '修改成功，请记住您的新密码', '', win32con.MB_OK)
            self.window_13.close()
            self.window_13.code.clear()
            self.window_13.code1.clear()
            self.window_1.id.clear()
            self.window_1.code.clear()
            self.window_1.show()
        else:
            win32api.MessageBox(0, '请重新输入！', 'error', win32con.MB_OK)
            return

    def show_zuzhi(self):  #学校各组织简介
        self.window_5.close()
        str='学生会'
        content = get_content(str,'Stu-org')
        self.window_6.words.setText(content)
        self.window_6.show()

    def show_xinwen(self):
        self.window_5.close()
        title = visitor.get_newstitle(v)
        self.window_7.b1.setText(title[0][1])
        self.window_7.b2.setText(title[1][1])
        self.window_7.b3.setText(title[2][1])
        self.window_7.b4.setText(title[3][1])
        self.window_7.b5.setText(title[4][1])
        self.window_7.b6.setText(title[5][1])
        self.window_7.b7.setText(title[6][1])
        self.window_7.b8.setText(title[7][1])
        self.window_7.b9.setText(title[8][1])
        self.window_7.b10.setText(title[9][1])
        self.window_7.show()

    def show_gonggao(self):
        self.window_5.close()
        title = visitor.get_noticetitle(v)
        self.window_8.b1.setText(title[0][1])
        self.window_8.b2.setText(title[1][1])
        self.window_8.b3.setText(title[2][1])
        self.window_8.b4.setText(title[3][1])
        self.window_8.b5.setText(title[4][1])
        self.window_8.b6.setText(title[5][1])
        self.window_8.b7.setText(title[6][1])
        self.window_8.b8.setText(title[7][1])
        self.window_8.b9.setText(title[8][1])
        self.window_8.b10.setText(title[9][1])
        self.window_8.show()

    def show_tiezi(self):
        self.window_5.close()
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        time_title = visitor.result_time(v)
        self.window_9.b1.setText(time_title[0])
        self.window_9.b2.setText(time_title[1])
        self.window_9.b3.setText(time_title[2])
        self.window_9.b4.setText(time_title[3])
        self.window_9.b5.setText(time_title[4])
        self.window_9.b6.setText(time_title[5])
        self.window_9.b7.setText(time_title[6])
        self.window_9.b8.setText(time_title[7])
        self.window_9.b9.setText(time_title[8])
        self.window_9.b10.setText(time_title[9])
        self.window_9.show()
    def show_hotresult(self):
        print("热度")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        hot_title = visitor.result_hot(v)
        self.window_9.b1.setText(hot_title[0])
        self.window_9.b2.setText(hot_title[1])
        self.window_9.b3.setText(hot_title[2])
        self.window_9.b4.setText(hot_title[3])
        self.window_9.b5.setText(hot_title[4])
        self.window_9.b6.setText(hot_title[5])
        self.window_9.b7.setText(hot_title[6])
        self.window_9.b8.setText(hot_title[7])
        self.window_9.b9.setText(hot_title[8])
        self.window_9.b10.setText(hot_title[9])
    def show_timeresult(self):
        print("时间")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        time_title = visitor.result_time(v)
        # print(time_title)
        self.window_9.b1.setText(time_title[0])
        self.window_9.b2.setText(time_title[1])
        self.window_9.b3.setText(time_title[2])
        self.window_9.b4.setText(time_title[3])
        self.window_9.b5.setText(time_title[4])
        self.window_9.b6.setText(time_title[5])
        self.window_9.b7.setText(time_title[6])
        self.window_9.b8.setText(time_title[7])
        self.window_9.b9.setText(time_title[8])
        self.window_9.b10.setText(time_title[9])
    def show_p1result(self):
        print("活动")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p1.text()
        title = visitor.result_p(v,str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p2result(self):
        print("闲聊")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p2.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p3result(self):
        print("交友")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p3.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p4result(self):
        print("自习")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p4.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p5result(self):
        print("拼单")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p5.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p6result(self):
        print("交易")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p6.text()
        title = visitor.result_p(v, str)
        print(title)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p7result(self):
        print("咨询")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p7.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_p8result(self):
        print("公告")
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.p8.text()
        title = visitor.result_p(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])
    def show_keyresult(self):
        self.window_9.b1.setText("空")
        self.window_9.b2.setText("空")
        self.window_9.b3.setText("空")
        self.window_9.b4.setText("空")
        self.window_9.b5.setText("空")
        self.window_9.b6.setText("空")
        self.window_9.b7.setText("空")
        self.window_9.b8.setText("空")
        self.window_9.b9.setText("空")
        self.window_9.b10.setText("空")
        str = self.window_9.words.text()
        title = visitor.result_key(v, str)
        self.window_9.b1.setText(title[0])
        self.window_9.b2.setText(title[1])
        self.window_9.b3.setText(title[2])
        self.window_9.b4.setText(title[3])
        self.window_9.b5.setText(title[4])
        self.window_9.b6.setText(title[5])
        self.window_9.b7.setText(title[6])
        self.window_9.b8.setText(title[7])
        self.window_9.b9.setText(title[8])
        self.window_9.b10.setText(title[9])

    def settiezinum1(self):
        self.tiezinum=1
        self.show_tiezicontent(self.tiezinum)
    def settiezinum2(self):
        self.tiezinum=2
        self.show_tiezicontent(self.tiezinum)
    def settiezinum3(self):
        self.tiezinum=3
        self.show_tiezicontent(self.tiezinum)
    def settiezinum4(self):
        self.tiezinum=4
        self.show_tiezicontent(self.tiezinum)
    def settiezinum5(self):
        self.tiezinum=5
        self.show_tiezicontent(self.tiezinum)
    def settiezinum6(self):
        self.tiezinum=6
        self.show_tiezicontent(self.tiezinum)
    def settiezinum7(self):
        self.tiezinum=7
        self.show_tiezicontent(self.tiezinum)
    def settiezinum8(self):
        self.tiezinum=8
        self.show_tiezicontent(self.tiezinum)
    def settiezinum9(self):
        self.tiezinum=9
        self.show_tiezicontent(self.tiezinum)
    def settiezinum10(self):
        self.tiezinum=10
        self.show_tiezicontent(self.tiezinum)
    def show_tiezicontent(self,titlenum):
        self.window_9.close()
        c0,c1,c2 = visitor.chakantiezi(v,titlenum)
        self.window_16.title.setText(c0)
        self.window_16.tiezi.setText(c1)
        string = ""
        for i in c2:
            string = string + i + "\n"
        self.window_16.huifu.setText(string)
        self.window_16.show()

    def fabiaopinglun(self):
        if not (v.attribute == 'user' and v.state == 0):
            win32api.MessageBox(0, '非用户或被锁定，请联系管理员', 'error', win32con.MB_OK)
            self.window_16.words.clear()
        else:
            rid = v.id
            reply =  self.window_16.words.text()
            post_id = v.pid[self.tiezinum-1]
            v.cur.execute(
                'UPDATE post set count = count + 1 where post_id = ?', (post_id,))
            v.con.commit()
            v.cur.execute(
                'INSERT INTO comment(post_id,rid,reply) VALUES (?,?,?)', (post_id, rid, reply))
            v.con.commit()
            win32api.MessageBox(0, '评论成功！', '', win32con.MB_OK)
            self.show_tiezicontent(self.tiezinum)

    def fabiaotiezi(self):
        if not (v.attribute == 'user' and v.state == 0):
            win32api.MessageBox(0, '非用户或被锁定，请联系管理员', 'error', win32con.MB_OK)
            self.window_16.words.clear()
        else:
            title = self.window_17.title.text()
            content = self.window_17.words.text()
            if title == "" or content =="":
                win32api.MessageBox(0, '标题或内容不能为空', 'error', win32con.MB_OK)
                return
            label1 = self.window_17.label.currentText()
            if label1 == "活动":
                label2 = self.window_17.label2.currentText()
            else:
                label2 =None
            if label2 =="院级":
                label3 = self.window_17.label3.currentText()
            else:
                label3 =None
            post_id = random.randint(1, 9999)
            while v.cur.execute(
                    'SELECT * from post where post_id = ?',
                    (post_id,
                     )).fetchone():
                post_id = random.randint(1, 9999)
            count = 0
            # time = CURRENT_TIMESTAMP
            uid = v.id
            top = 0
            v.cur.execute(
                'INSERT INTO post(post_id,label1,label2,label3,count,uid,content,title,top) VALUES '
                '(?,?,?,?,?,?,?,?,?)',
                (post_id,
                 label1,
                 label2,
                 label3,
                 count,
                 uid,
                 content,
                 title,
                 top))
            v.con.commit()
            win32api.MessageBox(0, '发帖成功!', '', win32con.MB_OK)
            self.window_17.close()
            self.window_9.show()

    def announce(self):
        title = self.window_19.title.text()
        content = self.window_19.words.text()
        if title == "" or content == "":
            win32api.MessageBox(0, '标题或内容不能为空', 'error', win32con.MB_OK)
            return
        post_id = random.randint(1, 9999)
        while v.cur.execute(
                'SELECT * from post where post_id = ?',
                (post_id,
                 )).fetchone():
            post_id = random.randint(1, 9999)
        count = 0
        uid = v.id
        top = 0
        v.cur.execute(
            'INSERT INTO post(post_id,label1,label2,label3,count,uid,content,title,top) VALUES '
            '(?,?,?,?,?,?,?,?,?)', (post_id, "公告", None, None, count, uid, content, title, top))
        v.con.commit()
        win32api.MessageBox(0, '公告发布成功！', '', win32con.MB_OK)
        self.window_19.close()
        self.window_18.show()

    def lock(self):
        userid = self.window_20.words.text()
        userid = int(userid)
        if not v.cur.execute('SELECT * FROM user WHERE id=?', (userid,)):
            win32api.MessageBox(0, '用户不存在，请重新输入', 'error', win32con.MB_OK)
            return
        m = v.cur.execute(
            'SELECT * FROM user WHERE id=?', (userid,)).fetchone()
        if m[4] == 1:
            win32api.MessageBox(0, '用户已经被锁定', 'error', win32con.MB_OK)
            return
        else:
            sql = 'update user set state=1 where id=?'
            v.cur.execute(sql, (userid,))
            v.con.commit()
            win32api.MessageBox(0, '锁定成功', '', win32con.MB_OK)
            sql = v.cur.execute(
                'SELECT id,name,state from user where attribute = ?', ("user",))
            res = sql.fetchall()
            id = [(res.index(i) + 1, i) for i in res]
            string = ""
            for i in id:
                string = string + str(i) + "\n"
            self.window_20.ids.setText(string)

    def unlock(self):
        userid = self.window_20.words.text()
        userid = int(userid)
        if not v.cur.execute('SELECT * FROM user WHERE id=?', (userid,)):
            win32api.MessageBox(0, '用户不存在，请重新输入', 'error', win32con.MB_OK)
            return
        m = v.cur.execute(
            'SELECT * FROM user WHERE id=?', (userid,)).fetchone()
        if m[4] == 0:
            win32api.MessageBox(0, '用户未锁定', 'error', win32con.MB_OK)
            return
        else:
            sql = 'update user set state=0 where id=?'
            v.cur.execute(sql, (userid,))
            v.con.commit()
            win32api.MessageBox(0, '解锁成功', '', win32con.MB_OK)
            sql = v.cur.execute(
                'SELECT id,name,state from user where attribute = ?', ("user",))
            res = sql.fetchall()
            id = [(res.index(i) + 1, i) for i in res]
            string = ""
            for i in id:
                string = string + str(i) + "\n"
            self.window_20.ids.setText(string)

    def zhiding(self):
        postid = self.window_21.ids.text()
        postid = int(postid)
        if not v.cur.execute('SELECT * FROM post WHERE post_id=?', (postid,)):
            win32api.MessageBox(0, '帖子不存在，请重新输入', 'error', win32con.MB_OK)
            return
        m = v.cur.execute(
            'SELECT * FROM post WHERE post_id=?', (postid,)).fetchone()
        if m[-1] == 1:
            win32api.MessageBox(0, '帖子已经被置顶', 'error', win32con.MB_OK)
            return
        else:
            sql = 'update post set top=1 where post_id=?'
            v.cur.execute(sql, (postid,))
            v.con.commit()
            win32api.MessageBox(0, '置顶成功', '', win32con.MB_OK)
            sql = v.cur.execute(
                'SELECT post_id,label1,title,top from post')
            res = sql.fetchall()
            id = [(res.index(i) + 1, i) for i in res]
            string = ""
            for i in id:
                string = string + str(i) + "\n"
            self.window_21.words.setText(string)

    def delete(self):
        postid = self.window_21.ids.text()
        postid = int(postid)
        if not v.cur.execute('SELECT * FROM post WHERE post_id=?', (postid,)):
            win32api.MessageBox(0, '帖子不存在，请重新输入', 'error', win32con.MB_OK)
            return
        v.cur.execute('DELETE from post WHERE post_id=?', (postid,))
        win32api.MessageBox(0, '删除成功', '', win32con.MB_OK)
        self.window_21.ids.clear()
        sql = v.cur.execute(
            'SELECT post_id,label1,title,top from post')
        res = sql.fetchall()
        id = [(res.index(i) + 1, i) for i in res]
        string = ""
        for i in id:
            string = string + str(i) + "\n"
        self.window_21.words.setText(string)

    def sousuo(self):
        content = self.window_21.key.text()
        if content == "":
            sql = v.cur.execute(
                'SELECT post_id,label1,title,top from post')
            res = sql.fetchall()
            id = [(res.index(i) + 1, i) for i in res]
            string = ""
            for i in id:
                string = string + str(i) + "\n"
            self.window_21.words.setText(string)
        else:
            res = v.cur.execute(
                'SELECT post_id,label1,title,top FROM post WHERE content like ? or title like ?',('%' + content + '%','%' + content + '%',)).fetchall()
            v.con.commit()
            id = [(res.index(i) + 1, i) for i in res]
            string = ""
            for i in id:
                string = string + str(i) + "\n"
            self.window_21.key.clear()
            self.window_21.words.setText(string)

    def show_fabutiezi(self):
        self.window_9.close()
        self.window_17.show()
    def show_guanlijiemian(self):
        if v.attribute == 'user':
            win32api.MessageBox(0, '身份限制，拒绝查看', 'error', win32con.MB_OK)
        else:
            self.window_5.close()
            self.window_18.show()
    def show_xunwen(self):
        self.window_10.show()
    def fagonggao(self):
        self.window_18.close()
        self.window_19.show()
    def guanyonghu(self):
        self.window_18.close()
        sql = v.cur.execute(
            'SELECT id,name,state from user where attribute = ?', ("user",))
        res = sql.fetchall()
        id = [(res.index(i) + 1, i) for i in res]
        string = ""
        for i in id:
            string = string + str(i) + "\n"
        self.window_20.ids.setText(string)
        self.window_20.show()

    def guantiezi(self):
        self.window_18.close()
        sql = v.cur.execute(
            'SELECT post_id,label1,title,top from post')
        res = sql.fetchall()
        id = [(res.index(i) + 1, i) for i in res]
        string = ""
        for i in id:
            string = string + str(i) + "\n"
        self.window_21.words.setText(string)
        self.window_21.show()

    def goback(self):
        self.window_6.close()
        self.window_7.close()
        self.window_8.close()
        self.window_9.close()
        self.window_18.close()
        self.window_5.show()
    def goback_news(self):
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        #image clear()
        self.window_14.close()
        self.window_7.show()
    def goback_notices(self):
        self.window_15.words.clear()
        self.window_15.close()
        self.window_8.show()
    def goback_luntan(self):
        self.window_16.close()
        self.window_9.show()
    def goback_luntan1(self):
        self.window_17.title.clear()
        self.window_17.words.clear()
        self.window_17.close()
        self.window_9.show()
    def goback_guanli(self):
        self.window_19.close()
        self.window_20.close()
        self.window_21.close()
        self.window_18.show()
    def tuichu(self):
        exit()
    def nottuichu(self):
        self.window_10.close()

    def setclnum1(self):
        self.window_6.words.clear()
        str=self.window_6.pb2.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum2(self):
        self.window_6.words.clear()
        str = self.window_6.pb3.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum3(self):
        self.window_6.words.clear()
        str = self.window_6.pb4.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum4(self):
        self.window_6.words.clear()
        str = self.window_6.pb5.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum5(self):
        self.window_6.words.clear()
        str = self.window_6.pb6.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum6(self):
        self.window_6.words.clear()
        str = self.window_6.pb7.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum7(self):
        self.window_6.words.clear()
        str = self.window_6.pb8.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum8(self):
        self.window_6.words.clear()
        str = self.window_6.pb9.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum9(self):
        self.window_6.words.clear()
        str = self.window_6.pb10.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)
    def setclnum10(self):
        self.window_6.words.clear()
        str = self.window_6.pb11.text()
        content = get_content(str, 'Stu-org')
        self.window_6.words.setText(content)

    def setnewnum1(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b1.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum2(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b2.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum3(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b3.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum4(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b4.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum5(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b5.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum6(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b6.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum7(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b7.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum8(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b8.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum9(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b9.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()
    def setnewnum10(self):
        self.window_7.close()
        self.window_14.upwords.clear()
        self.window_14.downwords.clear()
        str = self.window_7.b10.text()
        content = get_content(str, 'News')
        self.window_14.upwords.setText(content[0])
        self.window_14.label.setPixmap(QPixmap(content[1]))
        self.window_14.downwords.setText(content[2])
        self.window_14.show()

    def setnonum1(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b1.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum2(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b2.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum3(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b3.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum4(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b4.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum5(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b5.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum6(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b6.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum7(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b7.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum8(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b8.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum9(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b9.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()
    def setnonum10(self):
        self.window_8.close()
        self.window_15.words.clear()
        str=self.window_8.b10.text()
        content = get_content(str, 'Notice')
        self.window_15.words.setText(content)
        self.window_15.show()




if __name__ == '__main__':
    v = visitor()
    app = QApplication([])
    test = test()
    # test.drawn()
    test.window_1.show()
    app.exec_()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchat
itchat.auto_login(True)
itchat.send('autoreply', toUserName='filehelper')
from itchat.content import *
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg['Text']=="1":
        msg['Text']="2"
    else:
        msg['Text'] =msg['Text']
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
# 处理好友添加请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    # 加完好友后，给好友打个招呼
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
itchat.run()

#==========以下代码都没啥用，先不删，没准以后能用上。
#import itchat
#@itchat.msg_register(itchat.content.TEXT)
#def text_reply(msg):
#    return msg['Text']
#itchat.auto_login(True)
#itchat.run()

# 处理多媒体类消息,包括图片、录音、文件、视频
#@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
#def download_files(msg):
#     msg['Text']是一个文件下载函数
#     传入文件名，将文件下载下来
#    msg['Text'](msg['FileName'])
#     把下载好的文件再发回给发送者
#    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
#itchat.auto_login(True)
#itchat.run()

# 处理好友添加请求
#@itchat.msg_register(FRIENDS)
#def add_friend(msg):
#    该操作会自动将新好友的消息录入，不需要重载通讯录
#    itchat.add_friend(**msg['Text'])
#     加完好友后，给好友打个招呼
#    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
#itchat.auto_login(True)
#itchat.run()
import sys
import time
from danmu import DanMuClient

programstarttime = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(time.time()))

a = open("danmu%s.txt" % programstarttime, "a")
a.writelines(['start', '\n'])
a.close()

b = open("gift%s.txt" % programstarttime, "a")
b.writelines(['start', '\n'])
b.close()


def pp(msg):
    encodedmsg = msg.encode(sys.stdin.encoding, 'ignore').decode(sys.stdin.encoding)
    # print(encodedmsg)
    if encodedmsg[0:7] == 'chatmsg':
        print(encodedmsg)
        f = open("danmu%s.txt" % programstarttime, "a")
        f.writelines([encodedmsg, '\n'])
        f.close()
    elif encodedmsg[0:3] == 'dgb':
        f = open("gift%s.txt" % programstarttime, "a")
        f.writelines([encodedmsg, '\n'])
        f.close()
    else:
        pass


dmc = DanMuClient('http://www.douyu.com/916749')


@dmc.danmu
def danmu_fn(msg):
    pp('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
        msg['type'], time.time(), msg['uid'], msg['nn'], msg['txt'],
        msg['cid'], msg['level'], msg['bnn'], msg['bl'], msg['brid']))
    # 数据含义：消息类型 时间戳 发送者UID　发送者昵称　弹幕文本　弹幕ID　用户等级　徽章昵称　徽章等级　徽章房间ID


@dmc.gift
def gift_fn(msg):
    pp('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
        msg['type'], time.time(), msg['gfid'], msg['uid'], msg['nn'],
        msg['bnn'], msg['bl'], msg['brid']))
    # 数据含义：消息类型 时间戳 礼物ID 发送者UID　发送者昵称　徽章昵称　徽章等级　徽章房间ID


dmc.start(blockThread=True)

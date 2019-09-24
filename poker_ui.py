import threading
from tkinter import *
from tkinter import messagebox

import poker


def play_or_continue():
    '''
    开始/继续游戏按钮事件
    :return:
    '''
    if is_playing:
        play()
    else:
        go_on()


def finish():
    '''
    结束游戏按钮事件
    :return:
    '''
    global is_playing
    is_playing = True
    var_play_or_continue_btn.set('开始游戏')
    play_or_continue_btn.config(state=NORMAL)
    var_player_mine.set('')
    var_player_other.set('')
    var_score.set('')
    var_compare_result.set('')
    var_point_player_mine.set('')
    var_point_player_other.set('')


def play():
    '''
    开始游戏逻辑
    :return:
    '''
    global is_playing
    is_playing = False
    var_play_or_continue_btn.set('继续游戏')

    var_score.set(SCORE)
    global score
    score = SCORE
    go_on()


def go_on():
    '''
    继续游戏逻辑
    :return:
    '''
    play_or_continue_btn.config(state=DISABLED)
    finish_btn.config(state=DISABLED)
    var_player_mine.set('')
    var_player_other.set('')
    var_compare_result.set('')
    var_point_player_mine.set('')
    var_point_player_other.set('')

    global poker_mine
    poker_mine = poker.random_poker()
    global poker_other
    poker_other = poker.random_poker()
    global i
    i = 1

    threading.Timer(delay, print_poker).start()


def print_poker():
    '''
    输出牌数
    :return:
    '''
    global i
    if i <= 2 * len(poker_mine):
        f = (i + 1) // 2
        if i % 2 == 0:
            var_player_other.set('* ' * f)
        else:
            var_player_mine.set(poker_mine[:f])
        i = i + 1

        threading.Timer(delay, print_poker).start()
    else:
        threading.Timer(delay, print_my_point).start()


def print_my_point():
    '''
    输出我的牛数或最大数
    :return:
    '''
    global point_mine
    point_mine = poker.poker_point(poker_mine)
    if point_mine is None:
        var_point_player_mine.set('没牛，最大：%d' % max(poker_mine))
    else:
        var_point_player_mine.set('牛数：%d' % point_mine)

    threading.Timer(delay, print_other_point).start()


def print_other_point():
    '''
    输出对方的牛数或最大数
    :return:
    '''
    var_player_other.set(poker_other)
    global point_other
    point_other = poker.poker_point(poker_other)
    if point_other is None:
        var_point_player_other.set('没牛，最大：%d' % max(poker_other))
    else:
        var_point_player_other.set('牛数：%d' % point_other)

    threading.Timer(delay, compare).start()


def compare():
    '''
    比较大小
    :return:
    '''
    if point_mine is None:
        if point_other is None:
            compare_score = poker.compare(max(poker_mine), max(poker_other))
        else:
            compare_score = poker.compare(0, point_other)
    else:
        if point_other is None:
            compare_score = poker.compare(point_mine, 0)
        else:
            compare_score = poker.compare(point_mine, point_other)

    if compare_score > 0:
        var_compare_result.set('恭喜你！你赢了，加%d分！' % compare_score)
    elif compare_score < 0:
        var_compare_result.set('很遗憾，你输了，扣%d分' % abs(compare_score))
    else:
        var_compare_result.set('平局，分数不变')
    global score
    score += compare_score
    var_score.set(score)
    if score < 0:
        messagebox.showerror(title='错误', message='分数小于零，游戏结束！')
        finish()
    else:
        play_or_continue_btn.config(state=NORMAL)
        finish_btn.config(state=NORMAL)


if __name__ == '__main__':
    SCORE = 80

    # 是否开始游戏
    is_playing = True
    delay = 0.3

    window = Tk()
    # 窗口标题
    window.title('斗牛——很好玩的一款小游戏')

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    win_width = 1200
    win_height = 1000

    x = (screen_width - win_width) / 2
    y = (screen_height - win_height) / 2

    # 窗口居中显示到屏幕
    window.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))

    Label(window, text='你的牌：', font=(14)).place(x=100, y=100)
    var_player_mine = StringVar()
    Label(window, textvariable=var_player_mine, bg='green', fg='white', font=(14)).place(x=220, y=100)
    var_point_player_mine = StringVar()
    Label(window, textvariable=var_point_player_mine, fg='blue', font=(14)).place(x=400, y=100)

    Label(window, text='对方的牌：', font=(14)).place(x=100, y=200)
    var_player_other = StringVar()
    Label(window, textvariable=var_player_other, bg='green', fg='white', font=(14)).place(x=220, y=200)
    var_point_player_other = StringVar()
    Label(window, textvariable=var_point_player_other, fg='blue', font=(14)).place(x=400, y=200)

    Label(window, text='得分：', font=(14)).place(x=100, y=350)
    var_score = StringVar()
    Label(window, textvariable=var_score, fg='green', font=('Arial', 16)).place(x=220, y=345)

    var_compare_result = StringVar()
    Label(window, textvariable=var_compare_result, fg='red', font=('Arial', 18)).place(x=win_width / 2 - 180,
                                                                                       y=win_height / 2)

    # 开始/继续游戏按钮
    var_play_or_continue_btn = StringVar()
    var_play_or_continue_btn.set('开始游戏')
    play_or_continue_btn = Button(window, textvariable=var_play_or_continue_btn, command=play_or_continue)
    play_or_continue_btn.place(x=win_width / 2 - 150, y=win_height - 200)

    # 结束游戏按钮
    finish_btn = Button(window, text='结束游戏', command=finish)
    finish_btn.place(x=win_width / 2 + 50, y=win_height - 200)
    finish_btn.config(state=DISABLED)

    window.mainloop()

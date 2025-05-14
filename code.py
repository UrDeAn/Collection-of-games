import tkinter as tk

from pygame import mixer
from PIL import ImageTk
import random
import time
import json


global BACK,xx,data,volume,f,now,s,ss,solo_Time
solo_Time = True
BACK = False
now = 0
volume = True
xx = 4
t = False
s = False
ss = False

#цвета
abg = "#396c7c"
bagr = "#71a4bb"
tex = "#111114"
bbg = "#abc2d1"
red = "#900020"
green = "#00693E"

#настройка основного окна
window = tk.Tk()

window.geometry('1200x900+352+55')
window.title("Сборник игр")
window.minsize(1200, 900)
window.maxsize(1600, 900)
window.iconbitmap(r'pictures\gamepad.ico')
window["bg"] = bagr

def dfdf(g):
    return 'break'
window.bind('<Tab>', dfdf)
def closing():
    with open('game_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    window.destroy()
window.protocol('WM_DELETE_WINDOW', closing)
#загружаем картинки
imag = ImageTk.PhotoImage(file='pictures\\стрелка.png')
image1 = ImageTk.PhotoImage(file='pictures\\zzz.png')
image2 = ImageTk.PhotoImage(file='pictures\\zz.png')
image3 = ImageTk.PhotoImage(file='pictures\\info.png')
vic_image1 = ImageTk.PhotoImage(file='pictures\\виселица1.png')
vic_image2 = ImageTk.PhotoImage(file='pictures\\виселица2.png')
vic_image3 = ImageTk.PhotoImage(file='pictures\\виселица3.png')
vic_image4 = ImageTk.PhotoImage(file='pictures\\виселица4.png')
vic_image5 = ImageTk.PhotoImage(file='pictures\\виселица5.png')
vic_image6 = ImageTk.PhotoImage(file='pictures\\виселица6.png')
vic_image7 = ImageTk.PhotoImage(file='pictures\\виселица7.png')
vic_image8 = ImageTk.PhotoImage(file='pictures\\виселица8.png')
vic_image9 = ImageTk.PhotoImage(file='pictures\\виселица9.png')
vic_image10 = ImageTk.PhotoImage(file='pictures\\виселица10.png')
stone_image = ImageTk.PhotoImage(file='pictures\\камень.png')
scissors_image = ImageTk.PhotoImage(file='pictures\\ножницы.png')
paper_image = ImageTk.PhotoImage(file='pictures\\бумага.png')
inp = ImageTk.PhotoImage(file='pictures\\inpt.png')
del_png = ImageTk.PhotoImage(file='pictures\\удалить.png')
tri = ImageTk.PhotoImage(file='pictures\\треугольник.png')
qwad = ImageTk.PhotoImage(file='pictures\\квадрат.png')
cir = ImageTk.PhotoImage(file='pictures\\круг.png')
romb = ImageTk.PhotoImage(file='pictures\\ромб.png')
galk = ImageTk.PhotoImage(file='pictures\\ыыы.png')
az = ImageTk.PhotoImage(file='pictures\\az.png')
stp = ImageTk.PhotoImage(file='pictures\\стоп.png')
pla = ImageTk.PhotoImage(file='pictures\\играть.png')
lev = ImageTk.PhotoImage(file='pictures\\лево.png')
prav = ImageTk.PhotoImage(file='pictures\\право.png')
stat_im = ImageTk.PhotoImage(file='pictures\\Стат.png')
ach_im = ImageTk.PhotoImage(file='pictures\\Достижение.png')
ach_im_1 = ImageTk.PhotoImage(file='pictures\\Достижение_1.png')
pol = ImageTk.PhotoImage(file='pictures\\полоса.png')
mos = ImageTk.PhotoImage(file='pictures\\мышь.png')
klav = ImageTk.PhotoImage(file='pictures\\клава.png')
udl = ImageTk.PhotoImage(file='pictures\\удал.png')
triu = ImageTk.PhotoImage(file='pictures\\треугл.png')
triu1 = ImageTk.PhotoImage(file='pictures\\треугл1.png')
pal = ImageTk.PhotoImage(file='pictures\\пал.png')
dos = ImageTk.PhotoImage(file='pictures\\ДОС.png')
bac = ImageTk.PhotoImage(file='pictures\\бак.png')


mixer.init()
mixer.music.load('music\\Музыка.mp3')
mixer.music.play((-1))
mixer.music.set_volume(0.1)
sound_win = mixer.Sound('music\\win.mp3')
sound_win.set_volume(0.25)
sound_keyboard = mixer.Sound('music\\нажатие кнопки.wav')
sound_keyboard.set_volume(1)
sound_short_win = mixer.Sound('music\\Победакоротка.mp3')
sound_short_win.set_volume(0.1)
sound_back = mixer.Sound('music\\Назад.mp3')
sound_back.set_volume(0.2)
sound_play = mixer.Sound('music\\ИГРАТЬ.mp3')
sound_play.set_volume(0.4)
sound_menu = mixer.Sound('music\\МЕНЮ.mp3')
sound_menu.set_volume(0.15)
sound_mem = mixer.Sound('music\\Мемори.mp3')
sound_mem.set_volume(0.35)
sound_ach = mixer.Sound('music\\Достижение.mp3')
sound_ach.set_volume(0.2)
sound_mem1 = mixer.Sound('music\\mEm.mp3')
sound_mem1.set_volume(1)
sound_lose = mixer.Sound('music\\Проигрышь.mp3')
sound_lose.set_volume(0.35)

BACK = False
now = 0
with open('game_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
data['opens'] += 1

def autosave():
    with open('game_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    window.after(1000, autosave)
window.after(1000, autosave)

def time(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    parts = []
    parts.append(f'{days} д.') if days > 0 else None
    parts.append(f'{hours} ч.') if hours > 0 else None
    parts.append(f'{minutes} мин.') if minutes > 0 else None
    parts.append(f'{seconds} сек.') if seconds > 0 or not parts else parts.append(f'{seconds} сек.')
    return ' '.join(parts)
volume = True
class Achievement:
    global ach_f
    def __init__(self,main, text,x,y, text2 = ""):
        def ll12(char):
            im.focus_set()
        g = tk.Frame(ach_f, bg=abg, width=345, height=90, pady=2, padx=2)
        im = tk.Label(g, image=dos, bg=bbg)
        im.place(x=0, y=0)
        ll = tk.Frame(g, bg=bbg, height=86, width=276)
        thj = tk.Entry(ll, bg=bbg, width=21, relief="flat", justify="center", font=("Arial", 18, "bold"), cursor="arrow",fg=green)
        thj.insert(0, main)
        thj.bind("<FocusIn>",ll12)
        thj.place(x=0, y=-3)
        pp1 = tk.Entry(ll, bg=bbg, width=25, relief="flat", justify="center", font=("Arial", 15, "bold"),cursor="arrow")
        pp1.insert(0, text)
        pp1.bind("<FocusIn>",ll12)
        pp1.place(x=0, y=33)
        pp12 = tk.Entry(ll, bg=bbg, width=25, relief="flat", justify="center", font=("Arial", 15, "bold"),cursor="arrow")
        pp12.insert(0, text2)
        pp12.place(x=0, y=58)
        pp12.bind("<FocusIn>",ll12)
        tk.Frame(ll, bg=bbg, width=345, height=3).place(x=0, y=30)
        g.place(x=x, y=y)
        ll.place(x=65, y=0)
def chec():
    def achive(main, text, text2 = "",g123=True):
        sound_ach.play()
        def dell(ach):
            ach.destroy()
        def ll12(char):
            im.focus_set()
        g = tk.Frame(window,bg=abg, width=345, height=90,pady=2,padx=2)
        im = tk.Label(g,image=dos,bg=bbg)
        im.place(x=0,y=0)
        ll = tk.Frame(g,bg=bbg,height=86,width=276)
        thj = tk.Entry(ll,bg=bbg,width=21,relief="flat",justify="center",font=("Arial",18,"bold"),cursor="arrow",fg=green)
        thj.insert(0, main)
        thj.bind("<FocusIn>",ll12)
        thj.place(x=0, y=-3)
        pp1 = tk.Entry(ll,bg=bbg,width=25,relief="flat",justify="center",font=("Arial",15,"bold"),cursor="arrow")
        pp1.insert(0,text)
        pp1.bind("<FocusIn>",ll12)
        pp1.place(x=0,y=33)
        pp12 = tk.Entry(ll,bg=bbg,width=25,relief="flat",justify="center",font=("Arial",15,"bold"),cursor="arrow")
        pp12.insert(0,text2)
        pp12.bind("<FocusIn>",ll12)
        pp12.place(x=0,y=58)
        tk.Frame(ll,bg=bbg,width=345,height=3).place(x=0,y=30)
        ll.place(x=65,y=0)
        if g123:
            g.place(x=853,y=808)
        else:
            g.place(x=1253,y=808)
        def up(g, t=6000, n=10):
            try:
                g.lift()
            except:
                return
            t -= n
            if t > 0:
                window.after(n, up, g, t)
        up(g)
        window.after(6000, lambda x=g: dell(g))
        
    if data['opens'] >= 100:
        if data["100opens"] != "True":
            achive('100 ЗАПУСКОВ', 'Откройте игру 100 раз')
            data['100opens'] = 'True'

    if data['time'] >= 3600:
        if data["3600times"] != "True":
            achive('ВРЕМЯ 1', 'ПРОВЕСТИ В ИГРЕ',"ПЕРВЫЙ ЧАС")
            data["3600times"] = "True"
            data["timeCount"] = "ВРЕМЯ 1"
            data["time_in_game"] = "ПЕРВЫЙ ЧАС"
            data["new"] = "False"
    if data['time'] >= 18000:
        if data["18000times"] != "True":
            achive('ВРЕМЯ 2', 'ПРОВЕСТИ В ИГРЕ',"5 ЧАСОВ")
            data["18000times"] = "True"
            data["timeCount"] = "ВРЕМЯ 2"
            data["time_in_game"] = "5 ЧАСОВ"
            data["new"] = "False"
    if data['time'] >= 36000:
        if data["36000times"] != "True":
            achive('ВРЕМЯ 3', 'ПРОВЕСТИ В ИГРЕ',"10 ЧАСОВ")
            data["36000times"] = "True"
            data["timeCount"] = "ВРЕМЯ 3"
            data["time_in_game"] = "10 ЧАСОВ"
            data["new"] = "False"
    if data['time'] >= 180000:
        if data["180000times"] != "True":
            achive('ВРЕМЯ max', 'ПРОВЕСТИ В ИГРЕ',"50 ЧАСОВ")
            data["180000times"] = "True"
            data["timeCount"] = "ВРЕМЯ max"
            data["time_in_game"] = "50 ЧАСОВ"
            data["new"] = "False"
    if data['time'] >= 90000:
        if data["360000times"] != "True":
            achive('ВРЕМЯ 4', 'ПРОВЕСТИ В ИГРЕ',"25 ЧАСОВ")
            data["360000times"] = "True"
            data["timeCount"] = "ВРЕМЯ 4"
            data["time_in_game"] = "100 ЧАСОВ"
            data["new"] = "False"


    if data['opens'] >= 10:
        if data["100opens"] != "True":
            achive('ЗАХОДЫ 1', 'ЗАЙТИ В ИГРУ',"10 РАЗ")
            data["100opens"] = "True"
            data["openCount"] = "ЗАХОДЫ 1"
            data["open_in_game"] = "10 РАЗ"
            data["new"] = "False"
    if data['opens'] >= 50:
        if data["500opens"] != "True":
            achive('ЗАХОДЫ 2', 'ЗАЙТИ В ИГРУ',"50 РАЗ")
            data["500opens"] = "True"
            data["openCount"] = "ЗАХОДЫ 2"
            data["open_in_game"] = "50 РАЗ"
            data["new"] = "False"
    if data['opens'] >= 100:
        if data["1000opens"] != "True":
            achive('ЗАХОДЫ 3', 'ЗАЙТИ В ИГРУ',"100 РАЗ")
            data["1000opens"] = "True"
            data["openCount"] = "ЗАХОДЫ 3"
            data["open_in_game"] = "100 РАЗ"
            data["new"] = "False"
    if data['opens'] >= 250:
        if data["5000opens"] != "True":
            achive('ЗАХОДЫ 4', 'ЗАЙТИ В ИГРУ',"250 РАЗ")
            data["5000opens"] = "True"
            data["openCount"] = "ЗАХОДЫ 4"
            data["open_in_game"] = "250 РАЗ"
            data["new"] = "False"
    if data['opens'] >= 500:
        if data["10000opens"] != "True":
            achive('ЗАХОДЫ max', 'ЗАЙТИ В ИГРУ',"500 РАЗ")
            data["10000opens"] = "True"
            data["openCount"] = "ЗАХОДЫ max"
            data["open_in_game"] = "500 РАЗ"
            data["new"] = "False"


    if data['games'] >= 10:
        if data["100games"] != "True":
            achive('СЫГРАНО 1', 'ЗАЙТИ В ЛЮБУЮ ИГРУ',"10 РАЗ")
            data["100games"] = "True"
            data["gamesCount"] = "СЫГРАНО 1"
            data["games_in_game"] = "10 РАЗ"
            data["new"] = "False"
    if data['games'] >= 50:
        if data["500games"] != "True":
            achive('СЫГРАНО 2', 'ЗАЙТИ В ЛЮБУЮ ИГРУ',"50 РАЗ")
            data["500games"] = "True"
            data["gamesCount"] = "СЫГРАНО 2"
            data["games_in_game"] = "50 РАЗ"
            data["new"] = "False"
    if data['games'] >= 100:
        if data["1000games"] != "True":
            achive('СЫГРАНО 3', 'ЗАЙТИ В ЛЮБУЮ ИГРУ',"100 РАЗ")
            data["1000games"] = "True"
            data["gamesCount"] = "СЫГРАНО 3"
            data["games_in_game"] = "100 РАЗ"
            data["new"] = "False"
    if data['games'] >= 250:
        if data["5000games"] != "True":
            achive('СЫГРАНО 4', 'ЗАЙТИ В ЛЮБУЮ ИГРУ',"250 РАЗ")
            data["5000games"] = "True"
            data["gamesCount"] = "СЫГРАНО 4"
            data["games_in_game"] = "250 РАЗ"
            data["new"] = "False"
    if data['games'] >= 500:
        if data["10000games"] != "True":
            achive('СЫГРАНО max', 'СЫГРАТЬ В ЛЮБУЮ ИГРУ',"500 РАЗ")
            data["10000games"] = "True"
            data["gamesCount"] = "СЫГРАНО max"
            data["games_in_game"] = "500 РАЗ"
            data["new"] = "False"

    if data['vis_wins'] >= 5:
        if data["10vis_wins"] != "True":
            achive('ВИСЕЛИЦА 1', 'ОДЕРЖАТЬ 5 ПОБЕД', "В ВИСИЛИЦЕ")
            data["10vis_wins"] = "True"
            data["visCount"] = "ВИСИЛИЦА 1"
            data["vis_wins_с"] = "5"
            data["new"] = "False"
    if data['vis_wins'] >= 10:
        if data["50vis_wins"] != "True":
            achive('ВИСЕЛИЦА 2', 'ОДЕРЖАТЬ 10 ПОБЕД', "В ВИСИЛИЦЕ")
            data["50vis_wins"] = "True"
            data["visCount"] = "ВИСИЛИЦА 2"
            data["vis_wins_с"] = "10"
            data["new"] = "False"
    if data['vis_wins'] >= 25:
        if data["100vis_wins"] != "True":
            achive('ВИСЕЛИЦА 3', 'ОДЕРЖАТЬ 25 ПОБЕД', "В ВИСИЛИЦЕ")
            data["100vis_wins"] = "True"
            data["visCount"] = "ВИСИЛИЦА 3"
            data["vis_wins_с"] = "25"
            data["new"] = "False"
    if data['vis_wins'] >= 50:
        if data["500vis_wins"] != "True":
            achive('ВИСЕЛИЦА 4', 'ОДЕРЖАТЬ 50 ПОБЕД', "В ВИСИЛИЦЕ")
            data["500vis_wins"] = "True"
            data["visCount"] = "ВИСИЛИЦА 4"
            data["vis_wins_с"] = "50"
            data["new"] = "False"
    if data['vis_wins'] >= 100:
        if data["1000vis_wins"] != "True":
            achive('ВИСЕЛИЦА max', 'ОДЕРЖАТЬ 100 ПОБЕД', "В ВИСИЛИЦЕ")
            data["1000vis_wins"] = "True"
            data["visCount"] = "ВИСИЛИЦА max"
            data["vis_wins_с"] = "100"
            data["new"] = "False"


    if data['rps_wins'] >= 10:
        if data["100rps_wins"] != "True":
            achive('К, Н, Б 1', 'ОДЕРЖАТЬ 10 ПОБЕД', "В К, Н, Б")
            data["100rps_wins"] = "True"
            data["rpsCount"] = "К, Н, Б 1"
            data["rps_wins_с"] = "10"
            data["new"] = "False"
    if data['rps_wins'] >= 50:
        if data["500rps_wins"] != "True":
            achive('К, Н, Б 2', 'ОДЕРЖАТЬ 50 ПОБЕД', "В К, Н, Б")
            data["500rps_wins"] = "True"
            data["rpsCount"] = "К, Н, Б 2"
            data["rps_wins_с"] = "50"
            data["new"] = "False"
    if data['rps_wins'] >= 100:
        if data["1000rps_wins"] != "True":
            achive('К, Н, Б 3', 'ОДЕРЖАТЬ 100 ПОБЕД', "В К, Н, Б")
            data["1000rps_wins"] = "True"
            data["rpsCount"] = "К, Н, Б 3"
            data["rps_wins_с"] = "100"
            data["new"] = "False"
    if data['rps_wins'] >= 250:
        if data["5000rps_wins"] != "True":
            achive('К, Н, Б 4', 'ОДЕРЖАТЬ 250 ПОБЕД', "В К, Н, Б")
            data["5000rps_wins"] = "True"
            data["rpsCount"] = "К, Н, Б 4"
            data["rps_wins_с"] = "250"
            data["new"] = "False"
    if data['rps_wins'] >= 500:
        if data["10000rps_wins"] != "True":
            achive('К, Н, Б max', 'ОДЕРЖАТЬ 500 ПОБЕД', "В К, Н, Б")
            data["10000rps_wins"] = "True"
            data["rpsCount"] = "К, Н, Б max"
            data["rps_wins_с"] = "500"
            data["new"] = "False"


    if data['gn_wins'] >= 5:
        if data["10gn_wins"] != "True":
            achive('УГАДАЙ ЧИСЛО 1', 'ОДЕРЖАТЬ 5 ПОБЕД', "В УГАДАЙ ЧИСЛО")
            data["10gn_wins"] = "True"
            data["gnCount"] = "УГАДАЙ ЧИСЛО 1"
            data["gn_wins_c"] = "5"
            data["new"] = "False"
    if data['gn_wins'] >= 10:
        if data["50gn_wins"] != "True":
            achive('УГАДАЙ ЧИСЛО 2', 'ОДЕРЖАТЬ 10 ПОБЕД', "В УГАДАЙ ЧИСЛО")
            data["50gn_wins"] = "True"
            data["gnCount"] = "УГАДАЙ ЧИСЛО 2"
            data["gn_wins_c"] = "10"
            data["new"] = "False"
    if data['gn_wins'] >= 25:
        if data["100gn_wins"] != "True":
            achive('УГАДАЙ ЧИСЛО 3', 'ОДЕРЖАТЬ 25 ПОБЕД', "В УГАДАЙ ЧИСЛО")
            data["100gn_wins"] = "True"
            data["gnCount"] = "УГАДАЙ ЧИСЛО 3"
            data["gn_wins_c"] = "25"
            data["new"] = "False"
    if data['gn_wins'] >= 50:
        if data["500gn_wins"] != "True":
            achive('УГАДАЙ ЧИСЛО 4', 'ОДЕРЖАТЬ 50 ПОБЕД', "В УГАДАЙ ЧИСЛО")
            data["500gn_wins"] = "True"
            data["gnCount"] = "УГАДАЙ ЧИСЛО 4"
            data["gn_wins_c"] = "50"
            data["new"] = "False"
    if data['gn_wins'] >= 100:
        if data["1000gn_wins"] != "True":
            achive('УГАДАЙ ЧИСЛО max', 'ОДЕРЖАТЬ 100 ПОБЕД', "В УГАДАЙ ЧИСЛО")
            data["1000gn_wins"] = "True"
            data["gnCount"] = "УГАДАЙ ЧИСЛО max"
            data["gn_wins_c"] = "100"
            data["new"] = "False"


    if data['mem_max'] >= 5:
        if data["5mem_max"] != "True":
            achive('ПОВТОРИ ЗА МНОЙ 1', 'ДОСТИГНУТЬ КОМБО 6', "В ПОВТОРИ ЗА МНОЙ")
            data["5mem_max"] = "True"
            data["memCount"] = "ПОВТОРИ ЗА МНОЙ 1"
            data["mem_wins_c"] = "5"
            data["new"] = "False"
    if data['mem_max'] >= 7:
        if data["7mem_max"] != "True":
            achive('ПОВТОРИ ЗА МНОЙ 2', 'ДОСТИГНУТЬ КОМБО 8', "В ПОВТОРИ ЗА МНОЙ")
            data["7mem_max"] = "True"
            data["memCount"] = "ПОВТОРИ ЗА МНОЙ 2"
            data["mem_wins_c"] = "7"
            data["new"] = "False"
    if data['mem_max'] >= 9:
        if data["9mem_max"] != "True":
            achive('ПОВТОРИ ЗА МНОЙ 3', 'ДОСТИГНУТЬ КОМБО 10', "В ПОВТОРИ ЗА МНОЙ")
            data["9mem_max"] = "True"
            data["memCount"] = "ПОВТОРИ ЗА МНОЙ 3"
            data["mem_wins_c"] = "9"
            data["new"] = "False"
    if data['mem_max'] >= 11:
        if data["11mem_max"] != "True":
            achive('ПОВТОРИ ЗА МНОЙ 4', 'ДОСТИГНУТЬ КОМБО 12', "В ПОВТОРИ ЗА МНОЙ")
            data["11mem_max"] = "True"
            data["memCount"] = "ПОВТОРИ ЗА МНОЙ 4"
            data["mem_wins_c"] = "11"
            data["new"] = "False"
    if data['mem_max'] >= 13:
        if data["13mem_max"] != "True":
            achive('ПОВТОРИ max', 'ДОСТИГНУТЬ КОМБО 14', "В ПОВТОРИ ЗА МНОЙ")
            data["13mem_max"] = "True"
            data["memCount"] = "ПОВТОРИ ЗА МНОЙ max"
            data["mem_wins_c"] = "13"
            data["new"] = "False"


    if data["bing_count"] >= 5000:
        if data["5000bing_max"] != "True":
            achive('БИНГО 1', 'ДОСТИГНУТЬ СЧЕТА 5000', "В БИНГО")
            data["5000bing_max"] = "True"
            data["bingCount"] = "БИНГО 1"
            data["bing_wins_c"] = "5000"
            data["new"] = "False"
    if data["bing_count"] >= 10000:
        if data["10000bing_max"] != "True":
            achive('БИНГО 2', 'ДОСТИГНУТЬ СЧЕТА 10000', "В БИНГО")
            data["10000bing_max"] = "True"
            data["bingCount"] = "БИНГО"
            data["bing_wins_c"] = "10000"
            data["new"] = "False"
    if data["bing_count"] >= 25000:
        if data["25000bing_max"] != "True":
            achive('БИНГО 3', 'ДОСТИГНУТЬ СЧЕТА 25000', "В БИНГО")
            data["25000bing_max"] = "True"
            data["bingCount"] = "БИНГО 3"
            data["bing_wins_c"] = "25000"
            data["new"] = "False"
    if data["bing_count"] >= 50000:
        if data["50000bing_max"] != "True":
            achive('БИНГО 4', 'ДОСТИГНУТЬ СЧЕТА 50000', "В БИНГО")
            data["50000bing_max"] = "True"
            data["bingCount"] = "БИНГО 4"
            data["bing_wins_c"] = "50000"
            data["new"] = "False"
    if data["bing_count"] >= 100000:
        if data["100000bing_max"] != "True":
            achive('БИНГО max', 'ДОСТИГНУТЬ СЧЕТА 100K', "В БИНГО")
            data["100000bing_max"] = "True"
            data["bingCount"] = "БИНГО max"
            data["bing_wins_c"] = "100000"
            data["new"] = "False"

    if data['vis2_wins'] >= 5:
        if data["5vis2_wins"] != "True":
                achive('ВИСЕЛИЦА ДЛЯ 2 1', 'ОДЕРЖАТЬ 5 ПОБЕД', "В ВИСИЛИЦЕ ДЛЯ 2")
                data["5vis2_wins"] = "True"
                data["vis2Count"] = "ВИСИЛИЦА ДЛЯ 2 1"
                data["vis2_wins_с"] = "5 ПОБЕД"
                data["new"] = "False"
    if data['vis2_wins'] >= 10:
        if data["10vis2_wins"] != "True":
                achive('ВИСЕЛИЦА ДЛЯ 2 2', 'ОДЕРЖАТЬ 10 ПОБЕД', "В ВИСИЛИЦЕ ДЛЯ 2")
                data["10vis2_wins"] = "True"
                data["vis2Count"] = "ВИСИЛИЦА ДЛЯ 2 2"
                data["vis2_wins_с"] = "10 ПОБЕД"
                data["new"] = "False"
    if data['vis2_wins'] >= 25:
        if data["25vis2_wins"] != "True":
                achive('ВИСЕЛИЦА ДЛЯ 2 3', 'ОДЕРЖАТЬ 25 ПОБЕД', "В ВИСИЛИЦЕ ДЛЯ 2")
                data["25vis2_wins"] = "True"
                data["vis2Count"] = "ВИСИЛИЦА ДЛЯ 2 3"
                data["vis2_wins_с"] = "25 ПОБЕД"
                data["new"] = "False"
    if data['vis2_wins'] >= 50:
        if data["50vis2_wins"] != "True":
                achive('ВИСЕЛИЦА ДЛЯ 2 4', 'ОДЕРЖАТЬ 50 ПОБЕД', "В ВИСИЛИЦЕ ДЛЯ 2")
                data["50vis2_wins"] = "True"
                data["vis2Count"] = "ВИСИЛИЦА ДЛЯ 2 4"
                data["vis2_wins_с"] = "50 ПОБЕД"
                data["new"] = "False"
    if data['vis2_wins'] >= 100:
        if data["100vis2_wins"] != "True":
                achive('ВИСЕЛИЦА ДЛЯ 2 max', 'ОДЕРЖАТЬ 100 ПОБЕД', "В ВИСИЛИЦЕ ДЛЯ 2")
                data["100vis2_wins"] = "True"
                data["vis2Count"] = "ВИСИЛИЦА ДЛЯ 2 max"
                data["vis2_wins_с"] = "100 ПОБЕД"
                data["new"] = "False"



    if (data['sl_count1']+data['sl_count2']) >= 10:
        if data["10sl_wins"] != "True":
                achive('СЛОВА 1', 'ДОСТИГНУТЬ СЧЕТА 10', "В СЛОВАХ",False)
                data["10sl_wins"] = "True"
                data["slCount"] = "СЛОВА 1"
                data["sl_wins_c"] = "10"
                data["new"] = "False"
    if (data['sl_count1']+data['sl_count2']) >= 20:
        if data["20sl_wins"] != "True":
                achive('СЛОВА 2', 'ДОСТИГНУТЬ СЧЕТА 20', "В СЛОВАХ",False)
                data["20sl_wins"] = "True"
                data["slCount"] = "СЛОВА 2"
                data["sl_wins_c"] = "20"
                data["new"] = "False"
    if (data['sl_count1']+data['sl_count2']) >= 50:
        if data["50sl_wins"] != "True":
                achive('СЛОВА 3', 'ДОСТИГНУТЬ СЧЕТА 50', "В СЛОВАХ",False)
                data["50sl_wins"] = "True"
                data["slCount"] = "СЛОВА 3"
                data["sl_wins_c"] = "50"
                data["new"] = "False"
    if (data['sl_count1']+data['sl_count2']) >= 100:
        if data["100sl_wins"] != "True":
                achive('СЛОВА 4', 'ДОСТИГНУТЬ СЧЕТА 100', "В СЛОВАХ",False)
                data["100sl_wins"] = "True"
                data["slCount"] = "СЛОВА 4"
                data["sl_wins_c"] = "100"
                data["new"] = "False"
    if (data['sl_count1']+data['sl_count2']) >= 200:
        if data["200sl_wins"] != "True":
                achive('СЛОВА max', 'ДОСТИГНУТЬ СЧЕТА 200', "В СЛОВАХ",False)
                data["200sl_wins"] = "True"
                data["slCount"] = "СЛОВА max"
                data["sl_wins_c"] = "200"
                data["new"] = "False"


        if (data["bing_count"] >= 100000 and data['mem_max'] >= 13 and data['gn_wins'] >= 100 and data['rps_wins'] >= 500 and
            data['vis_wins'] >= 100 and data['games'] >= 500 and data['opens'] >= 500 and data['time'] >= 180000 and
        data['vis2_wins'] >= 100 and (data['sl_count1']+data['sl_count2']) >= 200):
            if data["max_max"] != "True":
                achive('MAX max MAX', 'ДОСТИГНУТЬ max', " ВО ВСЕХ ДОСТИЖЕНИЯ")
                data["max_max"] = "True"
                data["maxt1"] = "ДОСТИГНУТЬ РАНГА max"
                data["maxt2"] = "ВО ВСЕХ ДОСТИЖЕНИЯ"
    window.after(500, chec)
window.after(500, chec)


def track_time():
    global now
    now += 1
    if now > data['longtime']:
        data['longtime'] = now
    data['time'] += 1
    if now > data['longtime']:
        data['longtime'] = now
    window.after(1000, track_time)
window.after(1000, track_time)


def menu_1():   #основная функция
    global BACK, solo_Time,multy_time
    solo_Time = True
    multy_time = True
    if BACK:
        sound_back.play()
        BACK = False
    def exit(): #функция выхода из игры
        window.destroy()

    def solo():
        global s
        s = True
        def solo_track_time():
            if s:
                data['solotime'] += 1
            else: return
            window.after(1000, solo_track_time)
        if solo_Time:
            solo_track_time()
        global BACK,t
        t = True
        if BACK:
            sound_back.play()
            BACK = False
        else:sound_menu.play()
        #функция выбора одиночной игры
        def back(g="g"):#функция возврата в меню
            global s
            s = False
            global BACK
            BACK = True
            solo_menu.destroy()
            menu_1()

        def visilica():
            sound_menu.play()# игра виселица
            sdf = []
            words_4_5 = ["ДЕЛО", "ДЕНЬ", "РУКА", "ЛИЦО", "ДРУГ", "ГЛАЗ", "СИЛА", "ВОДА", "ОТЕЦ", "НОГА", "НОЧЬ", "СТОЛ",
                         "ЖЕНА", "СВЕТ", "ПОРА", "ПУТЬ", "ДУША", "МАТЬ", "ЯЗЫК", "МАМА", "ЦЕЛЬ", "УТРО", "РОЛЬ", "ТЕЛО",
                         "ТРУД", "МЕРА", "ОКНО", "ИДЕЯ", "СЧЕТ", "ВЕЩЬ", "ЦЕНА", "ПЛАН", "РЕЧЬ", "СРОК", "ОПЫТ", "ЧЛЕН",
                         "БРАТ", "ИГРА", "РОСТ", "ТЕМА", "КРАЙ", "НЕБО", "ПОЛЕ", "БАНК", "СОЮЗ", "ВРАЧ", "ФАКТ", "УГОЛ",
                         "ДВОР", "ВЕРА", "ЦВЕТ", "МОРЕ", "КРУГ", "ПОЭТ", "ПАРА", "УДАР", "БАЗА", "ПАПА", "ГУБА", "ДОЧЬ",
                         "ЛЕТО", "КУРС", "РЕКА", "ФОНД", "ЛИСТ", "ВОЛЯ", "СНЕГ", "ИТОГ", "ЗОНА", "ГОРА", "МЕТР", "БОЛЬ",
                         "ЗВУК", "ДОЛЯ", "ВРАГ", "ЭТАП", "ЧЕРТ", "КОЖА", "ЗНАК", "ДЯДЯ", "УЧЕТ", "ХЛЕБ", "ЗИМА", "СЕТЬ",
                         "СУТЬ", "КЛУБ", "ЭТАЖ", "КИНО", "ДОЛГ", "ТЕНЬ", "ХРАМ", "УЖАС", "МАРТ", "ДАМА", "СТУЛ", "СЛЕД",
                         "РЫБА", "ДУМА", "ЧУДО", "МОЗГ", "ПОСТ", "ИЮНЬ", "ДАЧА", "БАБА", "ВИНО", "СПОР", "ВКУС", "КЛЮЧ",
                         "СЛОЙ", "ИЮЛЬ", "СЛУХ", "ЯЩИК", "ЦАРЬ", "СМЕХ", "БЕДА", "БЛОК", "УРОК", "ЧАСЫ", "КРИК", "МЯСО",
                         "аллея", "маска", "автор", "агент", "актер", "акула", "спорт", "алмаз", "ангар", "ангел", "анонс",
                     "бидон", "бетон", "берег", "белок", "белка", "бекон", "бедро", "бегун", "башня", "батон", "батут",
                     "басня", "барин", "баржа", "баран", "барак", "банка", "банан", "балка", "балет", "багет", "багаж",
                     "бабка", "афиша", "атлет", "атлас", "атака", "буран", "булка", "букет", "буква", "будни", "бугор",
                     "брюхо", "брошь", "броня", "бровь", "гонка", "шорты", "голос", "голод", "глушь", "культ", "табак",
                     "гамак", "линза", "ветер", "огонь", "шишка", "малыш", "ветка", "финал", "дрель", "трель", "свист",
                     "ворон", "пульс", "дятел", "дуэль", "изгой", "игрок", "колея", "колба", "кокон", "козел", "морда",
                     "хорда", "ковер", "кобра", "книга", "клоун", "класс", "макет", "мазут", "магма", "магия", "лямка",
                     "лыжня", "лопух", "ложка", "монах", "моляр", "молот", "мозги", "мишка", "мираж", "минус", "мидия",
                     "мечта", "метод", "опрос", "опора", "опера", "опека", "сырье", "сыщик", "сцена", "сфера", "схема",]

            words_5_6 = ["авария", "азбука", "азимут", "аккорд", "акцент", "алтарь", "альбом", "амулет", "аналог", "ангина",
                     "бензин", "белуга", "бездна", "беглец", "барьер", "баобаб", "банкир", "банкет", "бампер", "балкон",
                     "ведьма", "вахтер", "варвар", "ванная", "ваниль", "вампир", "валюта", "вакуум", "бюджет", "власть",
                     "глагол", "гитара", "гигант", "гвоздь", "гарпун", "гамбит", "галлон", "газета", "гадюка", "двойка",
                     "датчик", "данный", "журнал", "житель", "жертва", "жемчуг", "желудь", "желтый", "жасмин", "каблук",
                     "йогурт", "истина", "ирония", "индекс", "клевер", "кирпич", "кинжал", "кетчуп", "каштан", "каучук",
                     "колоша", "колпак", "логово", "ловкач", "лифтер", "листок", "медуза", "медаль", "мебель", "машина",
                     "матрас", "матрос", "мнение", "обивка", "остров", "основа", "ошибка", "пекарь", "пейзаж", "певица",
                     "пробка", "пробел", "пробег", "причал", "прицеп", "прицел", "резина", "резерв", "реестр", "регион",
                     "седина", "сговор", "сделка", "уговор", "футбол", "шантаж", "штанга", "штатив", "штекер", "штопор",
                     "анкета", "береза", "вектор", "паштет", "письмо", "поддон", "подвох", "подвиг", "подвал","аллея",
                     "маска", "автор", "агент", "актер", "акула", "спорт", "алмаз", "ангар", "ангел", "анонс",
                     "бидон", "бетон", "берег", "белок", "белка", "бекон", "бедро", "бегун", "башня", "батон", "батут",
                     "басня", "барин", "баржа", "баран", "барак", "банка", "банан", "балка", "балет", "багет", "багаж",
                     "бабка", "афиша", "атлет", "атлас", "атака", "буран", "булка", "букет", "буква", "будни", "бугор",
                     "брюхо", "брошь", "броня", "бровь", "гонка", "шорты", "голос", "голод", "глушь", "культ", "табак",
                     "гамак", "линза", "ветер", "огонь", "шишка", "малыш", "ветка", "финал", "дрель", "трель", "свист",
                     "ворон", "пульс", "дятел", "дуэль", "изгой", "игрок", "колея", "колба", "кокон", "козел", "морда",
                     "хорда", "ковер", "кобра", "книга", "клоун", "класс", "макет", "мазут", "магма", "магия", "лямка",
                     "лыжня", "лопух", "ложка", "монах", "моляр", "молот", "мозги", "мишка", "мираж", "минус", "мидия",
                     "мечта", "метод", "опрос", "опора", "опера", "опека", "сырье", "сыщик", "сцена", "сфера", "схема",
                     "подача"]
            words_7_8 = ["ЧЕЛОВЕК", "СТОРОНА", "РЕБЕНОК", "СИСТЕМА", "ЖЕНЩИНА", "РЕШЕНИЕ", "ИСТОРИЯ", "ОБЛАСТЬ",
                         "ПРОЦЕСС", "УСЛОВИЕ", "УРОВЕНЬ", "КОМНАТА", "ПОРЯДОК", "ИНТЕРЕС", "ПРАВИЛО", "МУЖЧИНА",
                         "ЧУВСТВО", "ПРИЧИНА", "ТОВАРИЩ", "ВСТРЕЧА", "ДЕВУШКА", "ОЧЕРЕДЬ", "СОБЫТИЕ", "ПРИНЦИП",
                         "МАЛЬЧИК", "УЧАСТИЕ", "ДЕВОЧКА", "КАРТИНА", "РИСУНОК", "ТЕЧЕНИЕ", "ЦЕРКОВЬ", "СВОБОДА",
                         "КОМАНДА", "ДОГОВОР", "ПРИРОДА", "ТЕЛЕФОН", "ПОЗИЦИЯ", "САМОЛЕТ", "ПРОЦЕНТ", "СТЕПЕНЬ",
                         "НАДЕЖДА", "ПРЕДМЕТ", "ВАРИАНТ", "МИНИСТР", "ГРАНИЦА", "МИЛЛИОН", "СЧАСТЬЕ", "КАБИНЕТ",
                         "МАГАЗИН", "ПЛОЩАДЬ", "ВОЗРАСТ", "УЧАСТОК", "ЖЕЛАНИЕ", "ГЕНЕРАЛ", "ПОНЯТИЕ", "РАДОСТЬ",
                         "ПРОДУКТ", "РЕФОРМА", "БУДУЩЕЕ", "РАССКАЗ", "ТЕХНИКА", "ДЕРЕВНЯ", "ЭЛЕМЕНТ", "ФУНКЦИЯ",
                         "КАПИТАН", "ФАМИЛИЯ", "БУТЫЛКА", "ВЛИЯНИЕ", "УЧИТЕЛЬ", "КОРАБЛЬ", "ДЕТСТВО", "ПРОШЛОЕ",
                         "КОРИДОР", "БОЛЕЗНЬ", "ПОПЫТКА", "ДЕПУТАТ", "КОМИТЕТ", "ДЕСЯТОК", "ГЛУБИНА", "СТУДЕНТ",
                         "СЕКУНДА", "СТАНЦИЯ", "БАБУШКА", "СТОЛИЦА", "ЭНЕРГИЯ", "СУБЪЕКТ", "РЕАКЦИЯ", "ОТЛИЧИЕ",
                         "КРАСОТА", "ЯВЛЕНИЕ", "НАЛИЧИЕ", "БОЛЬНОЙ", "ДЕКАБРЬ", "ОКТЯБРЬ", "ЗАНЯТИЕ", "ЗРИТЕЛЬ",
                         "КОНЦЕРТ", "МИЛИЦИЯ", "ПЕРЕХОД", "КРОВАТЬ", "АППАРАТ", "ОТРАСЛЬ", "ПРОДАЖА", "ОБРАЗЕЦ",
                         "ГЛАВНОЕ", "ТАБЛИЦА", "КОЛЛЕГА", "ОБОРОНА", "ПОДРУГА", "ПРИЗНАК", "ПЕРЕВОД", "РУССКИЙ",
                         "ПОДАРОК", "КОНКУРС", "ПРОСЬБА", "ПУБЛИКА", "РЕКЛАМА", "ПОРТРЕТ", "ЗЕРКАЛО", "ПОЕЗДКА",
                         "ПРОБЛЕМА", "КОМПАНИЯ", "РАЗВИТИЕ", "СРЕДСТВО", "КАЧЕСТВО", "ДЕЙСТВИЕ", "ОБЩЕСТВО", "СИТУАЦИЯ",
                         "КВАРТИРА", "ВНИМАНИЕ", "РАЗГОВОР", "ДВИЖЕНИЕ", "МАТЕРИАЛ", "КУЛЬТУРА", "ДОКУМЕНТ", "ИНСТИТУТ",
                         "ДИРЕКТОР", "СОЗДАНИЕ", "ЗНАЧЕНИЕ", "ХАРАКТЕР", "ПОЛИТИКА", "ПИСАТЕЛЬ", "РОДИТЕЛЬ", "ПОЛОВИНА",
                         "ГОСПОДИН", "ОПЕРАЦИЯ", "НАЗВАНИЕ", "СОЗНАНИЕ", "УЧАСТНИК", "ХУДОЖНИК", "КОМПЛЕКС", "КОНТРОЛЬ",
                         "ИСТОЧНИК", "ПРАКТИКА", "КОМИССИЯ", "РАБОТНИК", "ЛИЧНОСТЬ", "ПРАЗДНИК", "ЧИТАТЕЛЬ", "КОМАНДИР",
                         "СОБРАНИЕ", "ЗДОРОВЬЕ", "СКОРОСТЬ", "РЕЖИССЕР", "ОЩУЩЕНИЕ", "МЕХАНИЗМ", "ПЕРЕДАЧА", "РОЖДЕНИЕ",
                         "БОЛЬНИЦА", "СУЩЕСТВО", "СВОЙСТВО", "ЖИВОТНОЕ", "СТРАНИЦА", "РАСТЕНИЕ", "ТРАДИЦИЯ", "СВЕДЕНИЕ",
                         "СЕНТЯБРЬ", "РЕДАКЦИЯ", "ИЗВЕСТИЕ", "ВЫСТАВКА", "СЕРЕДИНА", "СОМНЕНИЕ", "ЛЕСТНИЦА", "ЦЕННОСТЬ",
                         "ОРГАНИЗМ", "ОТКРЫТИЕ", "РЕСТОРАН", "КИЛОМЕТР", "ЧИНОВНИК", "ЗАРПЛАТА", "ИЗУЧЕНИЕ", "ЗНАКОМЫЙ",
                         "КОНФЛИКТ", "ПЛОЩАДКА", "АКАДЕМИЯ", "ПРИНЯТИЕ", "ВЕЩЕСТВО", "КАНДИДАТ", "ДАВЛЕНИЕ", "ВОДИТЕЛЬ",
                         "СНИЖЕНИЕ", "УБИЙСТВО", "ПРОВЕРКА", "ОБУЧЕНИЕ", "ОЖИДАНИЕ", "ПАМЯТНИК", "ВЛАДЕЛЕЦ", "ТОРГОВЛЯ",
                         "МОЛОДЕЖЬ", "СУЩНОСТЬ", "ОСНОВНОЕ", "ОПИСАНИЕ", "РЕДАКТОР", "ПИСТОЛЕТ", "ВЕЛИЧИНА", "ПОМОЩНИК",
                         "ПРОКУРОР", "СИГАРЕТА", "ПАРАМЕТР", "ПРИЯТЕЛЬ", "МОЩНОСТЬ", "УКАЗАНИЕ", "ПРЕПАРАТ", "ВВЕДЕНИЕ",
                         "СОГЛАСИЕ", "СЦЕНАРИЙ", "УВАЖЕНИЕ", "ПОСТУПОК", "КОНТРАКТ", "АКАДЕМИК", "КАМПАНИЯ", "ПЕРЕМЕНА",
                         "ПРОТОКОЛ", "ПРИВЫЧКА", "ПАССАЖИР", "СТАНДАРТ", "КРИТЕРИЙ", "КАРАНДАШ", "РАЗВЕДКА", "ТРАГЕДИЯ"]
            def set_diff_visilica(): # выбор сложности
                def back_1(g="g"):
                    global BACK, solo_Time
                    solo_Time = False
                    BACK = True
                    diff_menu.destroy()
                    solo()

                def diff(difficul):
                    global game_vis,vis_t,diff_menu
                    game_vis = tk.Frame(window, width=1200, height=1100)
                    game_vis["bg"] = bagr
                    global count
                    if difficul == 1:
                        count = 10
                        wrd = words_4_5
                    elif difficul == 2:
                        count = 8
                        vic2 = tk.Label(game_vis,image=vic_image2, bg=bagr)
                        vic2.place(x=400, y=100)
                        wrd = words_5_6
                    elif difficul == 3:
                        count = 7
                        vic2 = tk.Label(game_vis,image=vic_image3, bg=bagr)
                        vic2.place(x=400, y=100)
                        wrd = words_7_8
                    data['sologames'] += 1
                    data['games'] += 1
                    data['vis_games'] += 1
                    vis_t = True
                    sound_play.play()
                    play(wrd)
                solo_menu.destroy()
                diff_menu = tk.Frame(window, width=1200, height=900)
                diff_menu["bg"] = bagr
                diffpick = tk.Label(diff_menu, text="ВЫБЕРИТЕ СЛОЖНОСТЬ", bg=bagr, fg=tex, font=("arial", 65, "bold"),
                                    anchor="n", ).pack(pady=5)
                diff1 = tk.Button(diff_menu, text="ЛЕГКАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, command=lambda difficult=1: diff(difficult), padx=55)
                diff1.pack(pady=15)
                diff2 = tk.Button(diff_menu, text="СРЕДНЯЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, padx=27, command=lambda difficult=2: diff(difficult))
                diff2.pack(pady=15)
                diff3 = tk.Button(diff_menu, text="СЛОЖНАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, padx=19, command=lambda difficult=3: diff(difficult))
                diff3.pack(pady=15)
                diff_menu.focus_set()
                diff_menu.bind('<Escape>',back_1)
                def guide_vis_m():
                    sound_keyboard.play()
                    global gh3
                    how_play.configure(text="СКРЫТЬ",command=cl)
                    gh3 = tk.Label(diff_menu, bg=bbg, text="КАК ИГРАТЬ В ВИСИЛИЦУ?\nСНАЧАЛА ВЫБЕРИТЕ СЛОЖНОСТЬ:\n1. ЛЕГКАЯ(СЛОВА ОТ 4 ДО 5 БУКВ И 10 ПОПЫТОК),\n2. СРЕДНЯЯ(СЛОВА ОТ 5 ДО 6 БУКВ И 8 ПОПЫТОК),\n3. СЛОЖНАЯ(СЛОВА ОТ 7 ДО 8 БУКВ И 7 ПОПЫТОК),\nЗАТЕМ ВВОДИТЕ БУКВЫ С КЛАВИАТУРЫ(РЕАЛЬНОЙ ИЛИ ВИРТУАЛЬНОЙ),\nЕСЛИ БУКВА ЕСТЬ В СЛОВЕ, ТО ОНА ВСТАНЕТ НА СВОЕ МЕСТО И ЗАГОРИТСЯ ЗЕЛЕНЫМ,\nА ЕСЛИ БУКВЫ НЕТ, ТО ОНА ЗАГОРИТСЯ КРАСНЫМ И КОЛ-ВО ПОПЫТОК УМЕНЬШИТСЯ.\nИГРА ИДЕТ ДО ТЕХ ПОР,\nПОКА СЛОВО НЕ БУДЕТ ОТГАДАНО\nИЛИ КОЛ-ВО ПОПЫТОК НЕ СТАНЕТ РАВНЫМ 0.\n(НА КЛАВИАТУРЕ ИСПОЛЬЗУЙТЕ РУССКУЮ РАСКЛАДКУ)"
                             ,justify="center", font=("arial", 17, "bold"))
                    gh3.place(x=22,y=257)
                def cl():
                    sound_keyboard.play()
                    global gh3
                    gh3.destroy()
                    how_play.configure(text="КАК ИГРАТЬ?",command = guide_vis_m)
                how_play = tk.Button(diff_menu, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 18, "bold"),
                                     relief="flat", activebackground=abg, padx=27, command=guide_vis_m)
                how_play.pack(pady=20)

                ex = tk.Button(diff_menu, text="НАЗАД", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                               activebackground=abg, padx=27, command=back_1)
                ex.pack(pady=70)
                diff_menu.pack()
                def play(wrd):
                    global vis_t,p
                    p = 0
                    def vis_track_time():
                        if vis_t:
                            data['vis_time'] += 1
                        else:
                            return
                        window.after(1000, vis_track_time)
                    vis_track_time()
                    diff_menu.destroy()
                    global game_vis
                    def back_vic(g="g"):
                        global vis_t
                        vis_t = False
                        global BACK, solo_Time
                        solo_Time = False
                        BACK = True
                        game_vis.destroy()
                        solo()

                    back_vic_button_1 = tk.Button(game_vis, image=imag, command=back_vic, relief="flat",
                                                  activebackground=bagr,width=60,height=50, bg=bagr,
                                                  ).place(x=20, y=20)
                    global guessed, correct, word,attempts
                    guessed = []
                    correct = []
                    word = random.choice(wrd).upper()
                    attempts = (tk.Label(game_vis, text=f"Осталось попыток: {count}!", bg=bagr, fg=tex,
                                         font=("arial", 30, "bold")))
                    attempts.place(x=372, y=10)

                    def check(letter):
                        sound_keyboard.play()
                        global count,p
                        letter = letter.upper()
                        if letter in sdf:
                            return
                        sdf.append(letter)
                        data['alphs'] += 1
                        def end():
                            def again():
                                game_vis.destroy()
                                visilica()
                            again_button_2 = tk.Button(game_vis, text="ЗАНОВО", command=again, relief="flat",
                                                     activebackground=abg, font=("arial", 45, "bold"), bg=bbg)
                            again_button_2.place(x=192,y=690)
                            back_vic_button_2 = tk.Button(game_vis, text="НАЗАД", command=back_vic, relief="flat",
                                                        activebackground=abg, font=("arial", 45, "bold"), bg=bbg,
                                                        padx=29).place(x=692, y=690)
                            game_vis.bind("<Key>", "")
                            for i in range(32):
                                globals()[chr(1040 + i)].destroy()
                        guessed.append(letter)
                        if letter in word:
                            globals()[letter].config(bg="#00693E",state="disabled")
                            for num, alpha in enumerate(word):
                                if alpha == letter:
                                    correct.append(letter)
                                    globals()["lab" + str(num)].configure(text=letter)
                        else:
                            global count,p
                            count -= 1
                            p += 1
                            globals()[letter].config(bg="#900020",state="disabled")
                            attempts.configure(text=f"Осталось попыток: {count}!")
                            if count == 9:
                                vic_print = tk.Label(game_vis,image=vic_image1,bg=bagr).place(x=400,y=100)
                            elif count == 8:
                                vic_print = tk.Label(game_vis, image=vic_image2, bg=bagr).place(x=400, y=100)
                            elif count == 7:
                                vic_print = tk.Label(game_vis, image=vic_image3, bg=bagr).place(x=400, y=100)
                            elif count == 6:
                                vic_print = tk.Label(game_vis, image=vic_image4, bg=bagr).place(x=400, y=100)
                            elif count == 5:
                                vic_print = tk.Label(game_vis, image=vic_image5, bg=bagr).place(x=400, y=100)
                            elif count == 4:
                                vic_print = tk.Label(game_vis,image=vic_image6,bg=bagr).place(x=400,y=100)
                            elif count == 3:
                                vic_print = tk.Label(game_vis,image=vic_image7,bg=bagr).place(x=400,y=100)
                            elif count == 2:
                                vic_print = tk.Label(game_vis,image=vic_image8,bg=bagr).place(x=400,y=100)
                            elif count == 1:
                                vic_print = tk.Label(game_vis,image=vic_image9,bg=bagr).place(x=400,y=100)
                            elif count == 0:
                                vic_print = tk.Label(game_vis,image=vic_image10,bg=bagr).place(x=400,y=100)

                        if set(correct) == set(word):
                            sound_win.play()
                            data['wins'] += 1
                            data['solowins'] += 1
                            data['vis_wins'] += 1
                            attempts.configure(text=f"Вы отгадали слово {word}!")
                            try:
                                if  p < data['vis_min']:
                                    data['vis_min'] = p
                            except:
                                if data['vis_min'] == "--":
                                    data['vis_min'] = p
                            if len(word) == 3:
                                attempts.place(x=330, y=10)
                            if len(word) == 4:
                                attempts.place(x=320, y=10)
                            if len(word) == 5:
                                attempts.place(x=310, y=10)
                            if len(word) == 6:
                                attempts.place(x=300, y=10)
                            if len(word) == 7:
                                attempts.place(x=290, y=10)
                            if len(word) == 8:
                                attempts.place(x=280, y=10)
                            end()
                        elif count == 0:
                            sound_lose.play()
                            data['loses'] += 1
                            data['sololoses'] += 1
                            data['vis_lose'] += 1
                            attempts.configure(text=f"Вы не отгадали слово {word}!")
                            try:
                                if  p < data['vis_min']:
                                    data['vis_min'] = p
                            except:
                                if data['vis_min'] == "--":
                                    data['vis_min'] = p
                            if len(word) == 3:
                                attempts.place(x=313, y=10)
                            if len(word) == 4:
                                attempts.place(x=304, y=10)
                            if len(word) == 5:
                                attempts.place(x=295, y=10)
                            if len(word) == 6:
                                attempts.place(x=286, y=10)
                            if len(word) == 7:
                                attempts.place(x=277, y=10)
                            if len(word) == 8:
                                attempts.place(x=268, y=10)
                            for i in range(len(word)):
                                if word[i] not in correct:
                                    globals()["lab" + str(i)].configure(text=word[i], fg="#900020")
                            end()
                    for i in range(11):
                        globals()[chr(1040 + i)] = tk.Button(game_vis, text=chr(1040 + i), bg=bbg, fg=tex,
                                                             font=("arial", 35, "bold"),
                                                             relief="flat", activebackground=abg,
                                                             command=lambda letter=f"{chr(1040 + i)}",: check(letter, ))
                        globals()[chr(1040 + i)].place(x=141 + i * 85, y=620, width=70, height=70)
                    for i in range(11):
                        globals()[chr(1051 + i)] = (tk.Button(game_vis, text=chr(1051 + i), bg=bbg, fg=tex,
                                                              font=("arial", 35, "bold"), relief="flat",
                                                              activebackground=abg,
                                                              command=lambda letter=f"{chr(1051 + i)}": check(letter)))
                        globals()[chr(1051 + i)].place(x=141 + i * 85, y=700, width=70, height=70, )
                    for i in range(10):
                        globals()[chr(1062 + i)] = tk.Button(game_vis, text=chr(1062 + i), bg=bbg, fg=tex,
                                                             font=("arial", 35, "bold"),
                                                             relief="flat", activebackground=abg,
                                                             command=lambda letter=f"{chr(1062 + i)}": check(letter))
                        globals()[chr(1062 + i)].place(x=184 + i * 85, y=780, width=70, height=70)
                    for i in range(len(word)):
                        for i in range(len(word)):
                            if len(word) == 8:
                                d = 123
                            if len(word) == 7:
                                d = 183
                            if len(word) == 6:
                                d = 243
                            if len(word) == 5:
                                d = 303
                            if len(word) == 4:
                                d = 363
                            if len(word) == 3:
                                d = 423
                            globals()["lab" + str(i)] = (
                                tk.Label(game_vis, text="  ", bg=bbg, fg=tex, font=("arial", 70, "bold"), padx=29, ))
                            globals()["lab" + str(i)].place(x=d + i * 120, y=455, width=110, height=110)
                    game_vis.focus_set()
                    def ggg(event):
                        char = event.char
                        if char in "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" and char != "":
                            check(char)
                    game_vis.bind("<Key>",ggg)
                    game_vis.bind('<Escape>', back_vic)
                    def stat_vis():
                        sound_keyboard.play()
                        def ba():
                            sound_keyboard.play()
                            ab.destroy()
                            stat.configure(command=stat_vis)
                        def upd():
                            try:
                                h.configure(text=f"МИН. ПОПЫТОК: {data['vis_min']}")
                                t.configure(text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis_time'])}")
                                g.configure(text=f"СЫГРАНО: {data['vis_games']}")
                                l.configure(text=f"ПОРАЖЕНИЙ: {data['vis_lose']}")
                                w.configure(text=f"ПОБЕД: {data['vis_wins']}")
                                a.configure(text=f"ПОПЫТОК: {data['alphs']}")
                                window.after(10, upd)
                            except:return
                        ab = tk.Frame(game_vis,bg=bbg,height=350,width=335)
                        ab.place(x=860,y=96)
                        tk.Label(ab,bg=bbg,text="СТАТИСТИКА",font=("arial", 35, "bold")).place(x=5,y=2)
                        a = tk.Label(ab, bg=bbg, text=f"ПОПЫТОК: {data['alphs']}", font=("arial", 25, "bold"))
                        a.place(x=-1, y=55)
                        w = tk.Label(ab, bg=bbg, text=f"ПОБЕД: {data['vis_wins']}", font=("arial", 25, "bold"))
                        w.place(x=-1, y=135)
                        l = tk.Label(ab, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['vis_lose']}", font=("arial", 25, "bold"))
                        l.place(x=-1, y=175)
                        g = tk.Label(ab, bg=bbg, text=f"СЫГРАНО: {data['vis_games']}", font=("arial", 25, "bold"))
                        g.place(x=-1, y=95)
                        t = tk.Label(ab, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis_time'])}", font=("arial", 25, "bold"))
                        h = tk.Label(ab, bg=bbg, text=f"МИН. ПОПЫТОК: {data['vis_min']}", font=("arial", 25, "bold"))
                        h.place(x=-1, y=295)
                        t.place(x=-1, y=215)
                        window.after(10,upd)
                        stat.configure(command=ba)
                    def guide_vis_m():
                        sound_keyboard.play()
                        global gh3
                        how_play.configure(text="СКРЫТЬ", command=cl)
                        how_play.place(x=512, y=854)
                        gh3 = tk.Label(game_vis, bg=bbg,
                                       text="КАК ИГРАТЬ В ВИСИЛИЦУ?\nСНАЧАЛА ВЫБЕРИТЕ СЛОЖНОСТЬ:\n1. ЛЕГКАЯ(СЛОВА ОТ 4 ДО 5 БУКВ И 10 ПОПЫТОК),\n2. СРЕДНЯЯ(СЛОВА ОТ 5 ДО 6 БУКВ И 8 ПОПЫТОК),\n3. СЛОЖНАЯ(СЛОВА ОТ 7 ДО 8 БУКВ И 7 ПОПЫТОК),\nЗАТЕМ ВВОДИТЕ БУКВЫ С КЛАВИАТУРЫ(РЕАЛЬНОЙ ИЛИ ВИРТУАЛЬНОЙ),\nЕСЛИ БУКВА ЕСТЬ В СЛОВЕ, ТО ОНА ВСТАНЕТ НА СВОЕ МЕСТО И ЗАГОРИТСЯ ЗЕЛЕНЫМ,\nА ЕСЛИ БУКВЫ НЕТ, ТО ОНА ЗАГОРИТСЯ КРАСНЫМ И КОЛ-ВО ПОПЫТОК УМЕНЬШИТСЯ.\nИГРА ИДЕТ ДО ТЕХ ПОР,\nПОКА СЛОВО НЕ БУДЕТ ОТГАДАНО\nИЛИ КОЛ-ВО ПОПЫТОК НЕ СТАНЕТ РАВНЫМ 0.\n(НА КЛАВИАТУРЕ ИСПОЛЬЗУЙТЕ РУССКУЮ РАСКЛАДКУ)"
                                       , justify="center", font=("arial", 17, "bold"))
                        gh3.place(x=68, y=100)

                    def cl():
                        sound_keyboard.play()
                        global gh3
                        gh3.destroy()
                        how_play.configure(text="КАК ИГРАТЬ?", command=guide_vis_m)
                        how_play.place(x=480, y=854)
                    how_play = tk.Button(game_vis, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 18, "bold"),
                                             relief="flat", activebackground=abg, padx=27, command=guide_vis_m)
                    how_play.place(x=480,y=854)
                    stat = tk.Button(game_vis, image=stat_im, relief='flat', activebackground=bagr, width=85,
                                          height=80, bg=bagr, command=stat_vis, compound='top', text='СТАТИСТИКА',
                                          font=('arial', 10, 'bold'))
                    stat.place(x=1100, y=5)
                    game_vis.pack()
            set_diff_visilica()

        def RockPaperScissors():
            global rps_t
            rps_t = True
            def rps_track_time():
                if rps_t:
                    data['rps_time'] += 1
                else:
                    return
                window.after(1000, rps_track_time)
            rps_track_time()
            data['sologames'] += 1
            data['games'] += 1
            sound_play.play()
            global loses, draws
            solo_menu.destroy()
            def back_RPS(g="g"):
                global rps_t
                rps_t = False
                global BACK, solo_Time
                solo_Time = False
                BACK = True
                rps.destroy()
                solo()
            def play_2(player_move):
                sound_keyboard.play()
                global wins, loses, draws
                data["rps_games"] += 1
                count_rps_lbl.configure(text=f"СЫГРАНО: {data["rps_games"]}")
                bot_move = random.randint(1,3)
                if bot_move == 1:
                    random_move.configure(image=stone_image,bg=bbg)
                elif bot_move == 2:
                    random_move.configure(image=scissors_image,bg=bbg)
                elif bot_move == 3:
                    random_move.configure(image=paper_image,bg=bbg)
                if player_move == 1:
                    your_move.configure(image=stone_image,bg=bbg)
                elif player_move == 2:
                    your_move.configure(image=scissors_image,bg=bbg)
                elif player_move == 3:
                    your_move.configure(image=paper_image,bg=bbg)
                if bot_move == 1 and player_move == 3 or bot_move == 2 and player_move == 1 or bot_move == 3 and player_move == 2:
                    sound_short_win.play()
                    data['rps_wins'] += 1
                    data['solowins'] += 1
                    lose_or_win.configure(fg="#00693E",text="ПОБЕДА")
                    lose_or_win.place(x=405, y=12)
                    win_lbl.configure(text=f"ПОБЕД: {data["rps_wins"]}")
                elif bot_move == 3 and player_move == 1 or bot_move == 1 and player_move == 2 or bot_move == 2 and player_move == 3:
                    sound_lose.play()
                    data['loses'] += 1
                    data['sololoses'] += 1
                    data["rps_loses"] += 1
                    lose_or_win.configure(fg="#900020", text="ПОРАЖЕНИЕ")
                    lose_or_win.place(x=315, y=12)
                    lose_lbl.configure(text=f"ПОРАЖЕНИЙ: {data["rps_loses"]}")
                elif bot_move == 3 and player_move == 3 or bot_move == 1 and player_move == 1 or bot_move == 2 and player_move == 2:
                    data["rps_draws"] += 1
                    lose_or_win.configure(fg="#B5B8B1", text="НИЧЬЯ")
                    lose_or_win.place(x=440, y=12)
                    draw_lbl.configure(text=f"НИЧЬИХ: {data["rps_draws"]}")
                win_rate_lbl.configure(text=f"ПРОЦЕНТ ПОБЕД: {data["rps_wins"]*100//data["rps_games"]}%")

            rps = tk.Frame(window, width=1200, height=900)
            rps["bg"] = bagr
            draw_lbl = tk.Label(rps,text=f"НИЧЬИХ: {data["rps_draws"]}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            draw_lbl.place(x=528,y=475)
            lose_or_win = tk.Label(rps,bg=bagr,font=("arial", 65, "bold"))
            your_move = tk.Label(rps,width=200,height=250,image=az)
            random_move = tk.Label(rps, width=200, height=250, image=az)
            your_move.place(x=210,y=150)
            random_move.place(x=790,y=150)
            win_or_lose = tk.Label(rps,text="VS",font=("arial", 140, "bold"),bg=bagr,fg=tex)
            win_or_lose.place(x=478,y=170)
            stone_move = tk.Button(rps,width=210,height=255,image=stone_image,bg=bbg,relief="flat",
                                   activebackground=bbg,command= lambda player_move=1:play_2(player_move))
            stone_move.place(x=194,y=600)
            scissors_move = tk.Button(rps,width=210,height=255,image=scissors_image,bg=bbg,relief="flat",
                                   activebackground=bbg,command= lambda player_move=2:play_2(player_move))
            scissors_move.place(x=494,y=600)
            paper_move = tk.Button(rps,width=210,height=255, image=paper_image, bg=bbg, relief="flat",
                                      activebackground=bbg,command= lambda player_move=3:play_2(player_move))
            paper_move.place(x=794, y=600)
            count_rps_lbl = tk.Label(rps,text=f"СЫГРАНО: {data["rps_games"]}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            count_rps_lbl.place(x=513,y=370)
            win_lbl = tk.Label(rps,text=f"ПОБЕД: {data["rps_wins"]}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            win_lbl.place(x=405,y=405)
            lose_lbl = tk.Label(rps,text=f"ПОРАЖЕНИЙ: {data["rps_loses"]}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            lose_lbl.place(x=585,y=405)
            win_rate_lbl = tk.Label(rps,text=f"ПРОЦЕНТ ПОБЕД: {data["rps_wins"]*100//(data["rps_games"]+1)}%",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            win_rate_lbl.place(x=465,y=440)
            rock_lbl = tk.Label(rps,text="КАМЕНЬ",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            rock_lbl.place(x=242,y=560)
            scissors_lbl = tk.Label(rps,text="НОЖНИЦЫ",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            scissors_lbl.place(x=522,y=560)
            paper_lbl = tk.Label(rps,text="БУМАГА",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            paper_lbl.place(x=842,y=560)
            you_lbl = tk.Label(rps,text="ВАШ ХОД",font=("arial", 25, "bold"),bg=bagr,fg=tex)
            you_lbl.place(x=230,y=105)
            rival_lbl = tk.Label(rps,text="СОПЕРНИК",font=("arial", 25, "bold"),bg=bagr,fg=tex)
            rival_lbl.place(x=796,y=105)
            back_rps_btn = tk.Button(rps,bg=bagr,image = imag,command= back_RPS,width=60,height=50,
                                     relief="flat",activebackground=bagr).place(x=20,y=20)
            rps.focus_set()
            def guide_rps():
                sound_keyboard.play()
                global gh3
                how_play.configure(text="СКРЫТЬ", command=cl_rps)
                how_play.place(x=523,y=865)
                gh3 = tk.Label(rps, bg=bbg,
                               text="КАК ИГРАТЬ В КАМЕНЬ, НОЖНИЦЫ, БУМАГА?\nСНАЧАЛА ВЫБЕРИТЕ ОДИН ИЗ ВАРИАНТОВ СВОЕГО ХОДА:\n1. КАМЕНЬ(ПОБЕЖДАЕТ НОЖНИЦЫ, НО ПРОИГРЫВАЕТ БУМАГЕ),\n2. НОЖНИЦЫ(ПОБЕЖДАЮТ БУМАГУ, НО ПРОИГРЫВАЮТ КАМНЮ),\n3. БУМАГА(ПОБЕЖДАЕТ КАМЕНЬ, НО ПРОИГРЫВАЕТ НОЖНИЦАМ),\nЗАТЕМ ВАШ ХОД СРАВНЯТ С ХОДОМ СОПЕРНИКА(КОМПЬЮТЕРОМ)\nИ БУДЕТ ОПРЕДЕЛЕН РЕЗУЛЬТАТ ИГРЫ."
                               , justify="center", font=("arial", 16, "bold"),pady=6)
                gh3.place(x=242, y=410)
            def cl_rps():
                sound_keyboard.play()
                global gh3
                gh3.destroy()
                how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                how_play.place(x=494, y=865)
            how_play = tk.Button(rps, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"),relief="flat", activebackground=abg, padx=20, command=guide_rps)
            how_play.place(x=494, y=865)
            rps.bind('<Escape>', back_RPS)
            def upd():
                try:
                    t.configure(text=f"ВРЕМЯ В ИГРЕ: {time(data["rps_time"])}")
                    window.after(10,upd)
                except: return
            t = tk.Label(rps,text=f"ВРЕМЯ В ИГРЕ: {time(data["rps_time"])}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            t.place(x=430,y=510)
            upd()
            rps.pack()

        def guess_number():
            sound_menu.play()
            def again_gn():
                gn.destroy()
                guess_number()
            def back_1(g="g"):
                global BACK, solo_Time
                solo_Time = False
                BACK = True
                diff_menu.destroy()
                solo()

            def diff(difficul):
                global gn,max_num,ioi
                gn = tk.Frame(window, width=1200, height=900)
                gn["bg"] = bagr
                diff_menu.destroy()
                if difficul == 1:
                    max_num = 100
                elif difficul == 2:
                    max_num = 1000
                elif difficul == 3:
                    max_num = 10000
                data['sologames'] += 1
                data['games'] += 1
                sound_play.play()
                ioi = 0
                play_2(max_num)

            solo_menu.destroy()
            diff_menu = tk.Frame(window, width=1200, height=900)
            diff_menu["bg"] = bagr
            diffpick = tk.Label(diff_menu, text="ВЫБЕРИТЕ СЛОЖНОСТЬ", bg=bagr, fg=tex, font=("arial", 65, "bold"),
                                anchor="n", ).pack(pady=5)
            diff1 = tk.Button(diff_menu, text="ЛЕГКАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, command=lambda difficult=1: diff(difficult), padx=55)
            diff1.pack(pady=15)
            diff2 = tk.Button(diff_menu, text="СРЕДНЯЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, padx=27, command=lambda difficult=2: diff(difficult))
            diff2.pack(pady=15)
            diff3 = tk.Button(diff_menu, text="СЛОЖНАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, padx=19, command=lambda difficult=3: diff(difficult))
            diff3.pack(pady=15)
            diff_menu.focus_set()
            diff_menu.bind('<Escape>', back_1)
            def guide_vis_m():
                sound_keyboard.play()
                global gh3
                how_play.configure(text="СКРЫТЬ", command=cl)
                gh3 = tk.Label(diff_menu, bg=bbg,
                               text="КАК ИГРАТЬ В УГАДАЙ ЧИСЛО?\nСНАЧАЛА ВЫБЕРИТЕ СЛОЖНОСТЬ:\n1. ЛЕГКАЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 100),\n2. СРЕДНЯЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 1000),\n3. СЛОЖНАЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 10000),\nЗАТЕМ ВВОДИТЕ ЧИСЛА С КЛАВИАТУРЫ(РЕАЛЬНОЙ ИЛИ ВИРТУАЛЬНОЙ),\nВВЕДЕННОЕ ЧИСЛО ВСТАНЕТ НА СВОЁ МЕСТО В ДВОЙНОМ НЕРАВЕНСТВЕ,\n ЕСЛИ ОНО СУЖАЕТ ОБЛАСТЬ ЗНАЧЕНИЯ Х,\nИГРА ИДЕТ ДО ТЕХ ПОР, ПОКА ЧИСЛО НЕ БУДЕТ ОТГАДАННО"
                               , justify="center", font=("arial", 21, "bold"))
                gh3.place(x=11, y=257)
            def cl():
                sound_keyboard.play()
                global gh3
                gh3.destroy()
                how_play.configure(text="КАК ИГРАТЬ?", command=guide_vis_m)
            how_play = tk.Button(diff_menu, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 18, "bold"),
                                 relief="flat", activebackground=abg, padx=27, command=guide_vis_m)
            how_play.pack(pady=20)
            ex = tk.Button(diff_menu, text="НАЗАД", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                           activebackground=abg, padx=27, command=back_1)
            ex.pack(pady=70)
            diff_menu.pack()
            def play_2(max_num):
                global gn_t
                gn_t = True
                def gn_track_time():
                    if gn_t:
                        data['gn_time'] += 1
                    else:
                        return
                    window.after(1000, gn_track_time)
                gn_track_time()
                data['gn_games'] += 1

                def back_gn(g="g"):
                    global gn_t
                    gn_t = False
                    global BACK, solo_Time
                    solo_Time = False
                    BACK = True
                    gn.destroy()
                    solo()
                global one, count, numbr, numb, min_numb,guess_num,min_num,first
                guess_num = random.randint(1, max_num-1)
                if max_num == 10000:
                    guess_num = random.randint(1000, max_num - 1)
                one = True
                first = True
                count = 0
                numbr = " "
                numb = 0
                min_num = 0
                diff_menu.destroy()

                def inpt(number):
                    sound_keyboard.play()
                    global one,numb,input_menu_2,numbr,count
                    if number == " ":
                        return
                    if number == "del" and count != 0:
                        input_menu_2.destroy()
                        error_lbl.configure(text="")
                        count -= 1
                        numbr = numbr[0:-1]
                        input_menu_2 = tk.Label(gn,text=numbr, font=("arial", 100, "bold"), bg=bbg, fg=tex)
                        if len(numbr) == 1:
                            input_menu_2.place(x=565, y=520)
                        elif len(numbr) == 2:
                            input_menu_2.place(x=515, y=520)
                        elif len(numbr) == 3:
                            input_menu_2.place(x=480, y=520)
                        elif len(numbr) == 4:
                            input_menu_2.place(x=445, y=520)
                        elif len(numbr) == 5:
                            input_menu_2.place(x=410, y=520)
                        elif len(numbr) == 6:
                            input_menu_2.place(x=375, y=520)
                        elif len(numbr) == 7:
                            input_menu_2.place(x=340, y=520)
                        elif len(numbr) == 8:
                            input_menu_2.place(x=305, y=520)
                        numb = numbr
                    elif number != "del":
                        if count == 8:
                            error_lbl.configure(text="ЧИСЛО СЛИШКОМ БОЛЬШОЕ")
                            return
                        if count != 0:
                            input_menu_2.destroy()
                        if count == 0 and number == 0:
                            return
                        if count != 0:
                            numbr = f"{numb}{number}"
                        else: numbr = str(number)
                        input_menu_2 = tk.Label(gn,text=numbr, font=("arial", 100, "bold"), bg=bbg, fg=tex)
                        if len(numbr) == 1:
                            input_menu_2.place(x=560, y=520)
                        elif len(numbr) == 2:
                            input_menu_2.place(x=523, y=520)
                        elif len(numbr) == 3:
                            input_menu_2.place(x=486, y=520)
                        elif len(numbr) == 4:
                            input_menu_2.place(x=449, y=520)
                        elif len(numbr) == 5:
                            input_menu_2.place(x=412, y=520)
                        elif len(numbr) == 6:
                            input_menu_2.place(x=375, y=520)
                        elif len(numbr) == 7:
                            input_menu_2.place(x=338, y=520)
                        elif len(numbr) == 8:
                            input_menu_2.place(x=301, y=520)
                        numb = numbr
                        count += 1

                def print_numb():
                    sound_keyboard.play()
                    global ioi
                    data['gn_try'] += 1
                    ioi += 1
                    global max_num,min_num,count,numbr,max_num,guess_num,first,X_lbl,bigger_or_lower,numbr_lbl
                    if numbr == " ":
                        return
                    if not first:
                        X_lbl.destroy()
                        bigger_or_lower.destroy()
                        numbr_lbl.destroy()

                    input_menu_2.destroy()
                    X_lbl = tk.Label(gn,fg=tex,bg=bagr,font=("arial", 100, "bold"),text = "X")
                    bigger_or_lower = tk.Label(gn,fg=green,bg=bagr,font=("arial", 100, "bold"))
                    numbr_lbl = tk.Label(gn,fg=green,bg=bagr,font=("arial", 100, "bold"),text = numbr)
                    first = False


                    if (not int(numbr) < max_num) and int(numbr) > min_num:
                        if len(numbr) == 1:
                            X_lbl.place(x=412, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=562, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=712, y=350)

                        elif len(numbr) == 2:
                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 3:
                            X_lbl.place(x=338, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=488, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=638, y=350)

                        elif len(numbr) == 4:
                            X_lbl.place(x=301, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=451, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=601, y=350)

                        elif len(numbr) == 5:
                            X_lbl.place(x=264, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=414, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=564, y=350)

                        elif len(numbr) == 6:
                            X_lbl.place(x=227, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=377, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=527, y=350)

                        elif len(numbr) == 7:
                            X_lbl.place(x=190, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=340, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=490, y=350)

                        elif len(numbr) == 8:
                            X_lbl.place(x=153, y=350)
                            bigger_or_lower.config(text="<",fg=red)
                            bigger_or_lower.place(x=303, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=453, y=350)


                    if (not int(numbr) > min_num) and int(numbr) < guess_num:

                        if len(numbr) == 1:
                            X_lbl.place(x=412, y=350)
                            bigger_or_lower.config(text=">", fg=red)
                            bigger_or_lower.place(x=562, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=712, y=350)

                        elif len(numbr) == 2:
                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text=">", fg=red)
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 3:
                            X_lbl.place(x=338, y=350)
                            bigger_or_lower.config(text=">", fg=red)
                            bigger_or_lower.place(x=488, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=638, y=350)

                        elif len(numbr) == 4:
                            X_lbl.place(x=301, y=350)
                            bigger_or_lower.config(text=">", fg=red)
                            bigger_or_lower.place(x=451, y=350)
                            numbr_lbl.configure(fg=red)
                            numbr_lbl.place(x=601, y=350)


                    if int(numbr) < max_num and int(numbr) > guess_num:
                        max_num = int(numbr)

                        if len(numbr) == 1:
                            max_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            max_num_lbl_1.place(x=1019, y=212)

                            X_lbl.place(x=412, y=350)
                            bigger_or_lower.config(text="<")
                            bigger_or_lower.place(x=562, y=350)
                            numbr_lbl.place(x=712, y=350)

                        elif len(numbr) == 2:
                            max_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            max_num_lbl_1.place(x=994, y=212)

                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text="<")
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 3:
                            max_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            max_num_lbl_1.place(x=969, y=212)

                            X_lbl.place(x=338, y=350)
                            bigger_or_lower.config(text="<")
                            bigger_or_lower.place(x=488, y=350)
                            numbr_lbl.place(x=638, y=350)

                        elif len(numbr) == 4:
                            max_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            max_num_lbl_1.place(x=944, y=212)

                            X_lbl.place(x=301, y=350)
                            bigger_or_lower.config(text="<")
                            bigger_or_lower.place(x=451, y=350)
                            numbr_lbl.place(x=601, y=350)


                    if int(numbr) > min_num and int(numbr) < guess_num:
                        min_num = int(numbr)
                        if len(numbr) == 1:
                            min_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            min_num_lbl_1.place(x=123, y=212)

                            X_lbl.place(x=412, y=350)
                            bigger_or_lower.config(text=">")
                            bigger_or_lower.place(x=562, y=350)
                            numbr_lbl.place(x=712, y=350)

                        elif len(numbr) == 2:
                            min_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            min_num_lbl_1.place(x=96, y=212)

                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text=">")
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 3:
                            min_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            min_num_lbl_1.place(x=71, y=212)

                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text=">")
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 4:
                            min_num_lbl_1.configure(text=numbr, font=("arial", 70, "bold"))
                            min_num_lbl_1.place(x=45, y=212)

                            X_lbl.place(x=301, y=350)
                            bigger_or_lower.config(text=">")
                            bigger_or_lower.place(x=451, y=350)
                            numbr_lbl.place(x=601, y=350)

                    if int(numbr) == guess_num:
                        global ajk
                        try: ajk.destroy()
                        except:None
                        sound_win.play()
                        try:
                            if ioi < data["gn_min"]:
                                data["gn_min"] = ioi
                        except:
                            if data["gn_min"] == "--":
                                data["gn_min"] = ioi
                        data['wins'] += 1
                        data['solowins'] += 1
                        data['gn_wins'] += 1
                        win_lbl = tk.Label(gn,text="ПОБЕДА",fg=green,bg=bagr,font=("arial", 100, "bold")).place(x=300,y=15)
                        number_lbl.configure(text = guess_num)
                        number_lbl.place(x=378,y=200)
                        if len(numbr) == 1:
                            X_lbl.place(x=412, y=350)
                            bigger_or_lower.config(text="=")
                            bigger_or_lower.place(x=562, y=350)
                            numbr_lbl.place(x=712, y=350)

                        elif len(numbr) == 2:
                            X_lbl.place(x=375, y=350)
                            bigger_or_lower.config(text="=")
                            bigger_or_lower.place(x=525, y=350)
                            numbr_lbl.place(x=675, y=350)

                        elif len(numbr) == 3:
                            X_lbl.place(x=338, y=350)
                            bigger_or_lower.config(text="=")
                            bigger_or_lower.place(x=488, y=350)
                            numbr_lbl.place(x=638, y=350)

                        elif len(numbr) == 4:
                            X_lbl.place(x=338, y=350)
                            bigger_or_lower.config(text="=")
                            bigger_or_lower.place(x=488, y=350)
                            numbr_lbl.place(x=638, y=350)
                        for i in range (10):
                            globals()["numbr" + str(i)].destroy()
                        inp_btn.configure(state="disabled")
                        del_alf.configure(state="disabled")
                        again = tk.Button(gn, text="ЗАНОВО", command=again_gn, relief="flat",
                                                     activebackground=abg, font=("arial", 45, "bold"), bg=bbg).place(x=192,y=720)

                        def back_gn():
                            global BACK, solo_Time
                            solo_Time = False
                            BACK = True
                            gn.destroy()
                            solo()
                        back_gn = tk.Button(gn, text="НАЗАД", command=back_gn, relief="flat",
                                                      activebackground=abg, font=("arial", 45, "bold"), bg=bbg,
                                                      padx=29).place(x=692, y=720)

                    count = 0
                    numbr = " "
                    error_lbl.configure(text="")

                back_gn_btn = tk.Button(gn,image=imag,bg=bagr,command = back_gn,activebackground=bagr,
                                            relief="flat",width=60,height=50).place(x=20,y=20)
                for i in range(10):
                    globals()["numbr" + str(i)] = tk.Button(gn,text = i,relief="flat",activebackground=abg,bg=bbg,
                                                font= ("arial", 45, "bold"),padx=10,command=lambda number = i:inpt(number))

                    globals()["numbr" + str(i)].place(x=20+i*117,y=730)
                input_menu = tk.Label(gn,bg=bbg, fg=tex,pady=70,padx=350)
                input_menu.place(x=248,y=520)
                min_num_lbl = tk.Label(gn,bg = bbg,pady=60,padx=130).place(x=20,y=200)
                number_lbl = tk.Label(gn, bg=bbg,text = "X",fg = tex,font =("arial", 86, "bold"),padx = 95)
                number_lbl.place(x=467, y=200)
                max_num_lbl = tk.Label(gn,bg = bbg,pady=60,padx=131).place(x=915,y=200)
                max_num_lbl_1 = (tk.Label(gn, bg=bbg))
                max_num_lbl_1.place(x=915, y=212)
                min_num_lbl_1 = (tk.Label(gn, bg=bbg,text = "0",font=("arial", 70, "bold")))
                min_num_lbl_1.place(x=123, y=212)
                number_lbl_1 = tk.Label(gn, bg=bbg,).place(x=467, y=200)
                bigger_lbl = tk.Label(gn, bg=bagr,text = "<",fg=tex,font=("arial", 170, "bold")).place(x=307,y=135)
                lower_lbl = tk.Label(gn, bg=bagr,text = "<",fg=tex,font=("arial", 170, "bold")).place(x=757,y=135)
                inp_btn = (tk.Button(gn,bg=bagr,activebackground=bagr,relief="flat",image = inp,height=160,
                                    command = print_numb))
                inp_btn.place(x=50,y=510)
                del_alf = tk.Button(gn,text = "FF",image = del_png,bg =bagr,activebackground=bagr,
                                    relief = "flat",command=lambda number = "del":inpt(number))

                def guide_rps():
                    sound_keyboard.play()
                    global gh3
                    how_play.configure(text="СКРЫТЬ", command=cl_rps)
                    how_play.place(x=520, y=865)
                    gh3 = tk.Label(gn, bg=bbg,
                                   text="КАК ИГРАТЬ В УГАДАЙ ЧИСЛО?\nСНАЧАЛА ВЫБЕРИТЕ СЛОЖНОСТЬ:\n1. ЛЕГКАЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 100),\n2. СРЕДНЯЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 1000),\n3. СЛОЖНАЯ(НУЖНО УГДАТЬ ЧИСЛО ОТ 0 ДО 10000),\nЗАТЕМ ВВОДИТЕ ЧИСЛА С КЛАВИАТУРЫ(РЕАЛЬНОЙ ИЛИ ВИРТУАЛЬНОЙ),\nВВЕДЕННОЕ ЧИСЛО ВСТАНЕТ НА НУЖНОЕ МЕСТО В ДВОЙНОМ НЕРАВЕНСТВЕ,\n ЕСЛИ ОНО СУЖАЕТ ОБЛАСТЬ ЗНАЧЕНИЯ Х,\nИГРА ИДЕТ ДО ТЕХ ПОР, ПОКА ЧИСЛО НЕ БУДЕТ ОТГАДАННО"
                                   , justify="center", font=("arial", 17, "bold"), pady=6)
                    gh3.place(x=130, y=420)

                def cl_rps():
                    sound_keyboard.play()
                    global gh3
                    gh3.destroy()
                    how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                    how_play.place(x=494, y=865)

                how_play = tk.Button(gn, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"), relief="flat",
                                     activebackground=abg, padx=20, command=guide_rps)
                how_play.place(x=494, y=865)
                del_alf.place(x=980,y=535)
                error_lbl = (tk.Label(gn,bg=bagr,font=("arial", 25, "bold"),fg=red,))
                error_lbl.place(x=351,y=686)
                if max_num == 10000:
                    max_num_lbl_1.configure(text = "10000",font = ("arial", 70, "bold"))
                elif max_num == 1000:
                    max_num_lbl_1.configure(text="1000", font=("arial", 70, "bold"))
                    max_num_lbl_1.place(x=939,y=212)
                else:
                    max_num_lbl_1.configure(text = "100",font = ("arial", 70, "bold"))
                    max_num_lbl_1.place(x=963, y=212)
                gn.focus_set()
                def hgf(event):
                    char = event.char
                    inpt(char)
                for i in range(10):
                    gn.bind(f"<KeyPress-{i}>",hgf)
                def ghj(event):
                    inpt("del")
                def ghjj(event):
                    print_numb()
                gn.bind(f"<KeyPress-BackSpace>", ghj)
                gn.bind(f"<KeyPress-Return>", ghjj)
                gn.bind('<Escape>', back_gn)

                def stat_gn():
                    sound_keyboard.play()
                    global ajk

                    def ba():
                        sound_keyboard.play()
                        ajk.destroy()
                        stat.configure(command=stat_gn)

                    def upd():
                        try:
                            gh.configure(text=f"ПОБЕД: {data['gn_wins']}")
                            ass.configure(text=f"МИН. ПОПЫТОК: {data['gn_min']}")
                            t.configure(text=f"В ИГРЕ: {time(data['gn_time'])}")
                            tr.configure(text=f"ПОПЫТОК: {data['gn_try']}")
                            window.after(10, upd)
                        except:
                            return
                    ajk = tk.Frame(gn,bg=bbg,height=190,width=620)
                    ajk.place(x=480,y=5)
                    tk.Label(ajk, bg=bbg, text="СТАТИСТИКА", font=("arial", 35, "bold")).place(x=112, y=2)
                    gh = tk.Label(ajk, bg=bbg, text=f"ПОБЕД: {data['gn_wins']}", font=("arial", 25, "bold"))
                    gh.place(x=-2, y=55)
                    tk.Label(ajk, bg=bbg, text=f"СЫГРАНО: {data['gn_games']}", font=("arial", 25, "bold")).place(x=-2, y=95)
                    tr = tk.Label(ajk, bg=bbg, text=f"ПОПЫТОК: {data['gn_try']}", font=("arial", 25, "bold"))
                    tr.place(x=-2,y=135)
                    t = tk.Label(ajk, bg=bbg, text=f"В ИГРЕ: {time(data['gn_time'])}", font=("arial", 25, "bold"))
                    ass = tk.Label(ajk, bg=bbg, text=f"МИН. ПОПЫТОК: {data['gn_min']}", font=("arial", 25, "bold"))
                    ass.place(x=250,y=95)
                    t.place(x=250,y=55)
                    upd()
                    stat.configure(command=ba)
                stat = tk.Button(gn, image=stat_im, relief='flat', activebackground=bagr, width=85,
                                 height=80, bg=bagr, command=stat_gn, compound='top', text='СТАТИСТИКА',
                                 font=('arial', 10, 'bold'))
                stat.place(x=1100, y=5)
                gn.pack()


        def memory():
            global fi
            fi = True
            sound_menu.play()
            data['mem_games'] += 1
            data['sologames'] += 1
            data['games'] += 1

            def menu_mem():
                global h,f
                h = True

                def mem_track_time():
                    if h:
                        data['mem_time'] += 1
                    else:
                        return
                    window.after(1000, mem_track_time)
                if fi:
                    mem_track_time()
                if BACK:
                    sound_back.play()
                global truecombo, ccc
                truecombo = ""
                ccc = 0
                for i in range(3):
                    a = random.randint(1, 9)
                    truecombo = truecombo + str(a)

                def play_3(first = True):
                    sound_play.play()
                    global combo, cnt,truecombo,ccc,vvv,pl3,combo_lbl,f

                    def again_mem():
                        play_3()
                    if first:
                        mem.destroy()
                        pl3 = tk.Frame(window, width=1200, height=900)
                        pl3["bg"] = bagr
                        pl3.pack()

                    def show_combo(www=0):
                        global ccc, a,f
                        a = tk.Label(pl3, text="ЗАПОМНИТЕ КОМБИНАЦИЮ", font=("arial", 50, "bold"), bg=bagr)
                        a.place(x=125, y=120)
                        for i in range(9):
                            globals()["ll" + str(i + 1)].configure(command="")
                        if www < len(truecombo):
                            sound_mem.play()
                            globals()["ll" + str(truecombo[www])].config(bg="yellow")
                            if int(truecombo[www]) > 4:
                                window.after(400, lambda: globals()["ll" + str(truecombo[www])].config(bg=bbg))
                            else:
                                window.after(400, lambda: globals()["ll" + str(truecombo[www])].config(bg=bagr))
                            window.after(700-ccc*10, lambda: show_combo(www + 1))
                        else:
                            a.configure(text="ПОВТОРИТЕ КОМБИНАЦИЮ")
                            for i in range (9):
                                globals()[f"ll{(i + 1)}"].configure(command=lambda x = i+1: check_mem(x))
                    ccc += 1
                    combo = ""
                    cnt = 0

                    def check_mem(x):
                        global combo, cnt, truecombo, ccc, a
                        combo = combo + str(x)
                        if combo[cnt] != truecombo[cnt]:
                            sound_lose.play()
                            data['loses'] += 1
                            data['sololoses'] += 1
                            c = tk.Label(pl3, bg=bagr, pady=30, padx=1200).place(x=0, y=120)
                            ag = tk.Label(pl3, bg=bagr,text="ПРОИГРЫШЬ",font=("arial", 50, "bold"))
                            ag.place(x=368,y=120)
                            globals()[f'll{x}'].configure(bg="red")
                            globals()[f'll{truecombo[cnt]}'].configure(bg="green")
                            close = tk.Label(pl3, bg=bagr, pady=200, padx=1200)

                            clos = tk.Button(pl3,bg=bbg,activebackground=abg,relief="flat",text="НАЗАД",font=("arial", 65, "bold")
                                             ,command=back_play_3,padx=29)
                            window.after(800,lambda: [globals()[f'll{i}'].configure(bg=bagr if i <= 4 else bbg) for i in
                                                  range(1, 10)])
                            window.after(800, lambda: clos.place(x=384, y=700))
                            window.after(800,lambda: close.place(x=0, y=650))
                            window.after(800, lambda: [globals()[f'll{i}'].config(command="") for i in range(1, 5)])
                        else:
                            sound_mem1.play()
                            cnt += 1
                            if combo == truecombo:
                                truecombo += str(random.randint(1, 9))
                                play_3(False)
                                sound_short_win.play()
                                data['wins'] += 1
                                data['solowins'] += 1

                    def back_play_3(g="g"):
                        global fi
                        fi = False
                        global BACK, solo_Time
                        solo_Time = False
                        BACK = True
                        pl3.destroy()
                        menu_mem()
                    pl3.focus_set()
                    pl3.bind("<Escape>",back_play_3)
                    f = (tk.Button(pl3, image=imag, bg=bagr, command=back_play_3, activebackground=bagr,
                              relief="flat", width=60, height=50, ))
                    f.place(x=20, y=20)
                    globals()["ll" + str(1)] = tk.Button(pl3, image=tri, bg=bagr,relief="flat",activebackground="green",padx=10,pady=10,
                                                         command=lambda x = 1: check_mem(x))
                    globals()["ll" + str(2)] = tk.Button(pl3, image=qwad, bg=bagr,relief="flat",activebackground="green",padx=10,pady=10,
                                                         command=lambda x = 2: check_mem(x))
                    globals()["ll" + str(3)] = tk.Button(pl3, image=cir, bg=bagr,relief="flat",activebackground="green",padx=10,pady=10,
                                                         command=lambda x = 3: check_mem(x))
                    globals()["ll" + str(4)] = tk.Button(pl3, image=romb, bg=bagr,relief="flat",activebackground="green",padx=10,pady=10,
                                                         command=lambda x = 4: check_mem(x))
                    globals()["ll" + str(1)].place(x=32, y=350)
                    globals()["ll" + str(2)].place(x=314, y=350)
                    globals()["ll" + str(3)].place(x=614, y=350)
                    globals()["ll" + str(4)].place(x=914, y=350)
                    for i in range(5):
                        globals()["ll" + str(i+5)] = tk.Button(pl3, text=i + 1, font=("Arial", 70, "bold"),relief="flat", fg=tex,
                                                             bg=bbg,padx=35,activebackground="green",command=lambda x = i+5: check_mem(x))
                        globals()["ll" + str(i+5)].place(x=58 + i * 220, y=680)
                    if first:
                        vvv = tk.Label(pl3,text = f"ХОД №{ccc}",font=("Arial", 70, "bold"),bg=bagr)
                        vvv.place(x=412,y=10)
                        combo_lbl = tk.Label(pl3,text = f"ДЛИННА КОМБИНАЦИИ:{ccc+2}",font=("Arial", 30, "bold"),bg=bagr)
                        combo_lbl.place(x=344,y=200)
                    if not first:
                        vvv.configure(text = f"ХОД №{ccc}")
                        combo_lbl.configure(text = f"ДЛИННА КОМБИНАЦИИ:{ccc+2}")
                        if data['mem_max'] < ccc+1:
                            data['mem_max'] = ccc+1
                    show_combo()


                solo_menu.destroy()
                mem = tk.Frame(window, width=1200, height=900)
                mem["bg"] = bagr

                def back_memory(g="g"):
                    global h
                    h = False
                    global BACK, solo_Time
                    solo_Time = False
                    BACK = True
                    mem.destroy()
                    solo()
                tk.Label(mem,text="ПОВТОРИ ЗА МНОЙ",bg=bagr,font=("Arial", 60, "bold")).place(x=200,y=10)
                tk.Button(mem, image=imag, bg=bagr, command=back_memory, activebackground=bagr,
                                        relief="flat", width=60, height=50,).place(x=20,y=20)
                tk.Button(mem,text="ИГРАТЬ",font=("Arial",60,"bold"),bg=bbg,activebackground=abg,command=play_3,relief="flat").place(x=404,y=690)

                def guide_rps():
                    sound_keyboard.play()
                    global gh3
                    how_play.configure(text="СКРЫТЬ", command=cl_rps)
                    how_play.place(x=520, y=860)
                    gh3 = tk.Label(mem, bg=bbg,
                                   text="КАК ИГРАТЬ В ПОВТОРИ ЗА МНОЙ?\nПОСЛЕ ТОГО, КАК ВЫ НАЖМЕТЕ КНОПКУ 'ИГРАТЬ',\nВАМ НУЖНО БУДЕТ ЗАПОМНИТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ ЦИФР И ФИГУР,\nКОТОРЫЕ БУДУТ ПОДСВЕЧИВАТЬСЯ ЖЕЛТЫМ,\nА ПОСЛЕ ЭТОГО НАЖАТЬ В ТОЙ ЖЕ ПОСЛЕДОВАТЕЛЬНОСТИ НА ЦИФРЫ И ФИГУРЫ,\nЗАТЕМ К ДАННОЙ КОМБИНАЦИИ ДОБАВИТСЯ ЕЩЕ 1 ЭЛЕМЕНТ\nИ ИГРА ПОВТОРИТСЯ С БОЛЕЕ ДЛИННОЙ КОМБИНАЦИЕЙ.\nИГРА ИДЕТ ДО ТЕХ ПОР, ПОКА ВЫ НЕ ОШИБЕТЕСЬ."
                                   , justify="center", font=("arial", 17, "bold"), pady=6,padx=43)
                    gh3.place(x=58, y=417)

                def cl_rps():
                    sound_keyboard.play()
                    global gh3
                    gh3.destroy()
                    how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                    how_play.place(x=492, y=860)

                how_play = tk.Button(mem, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"), relief="flat",
                                     activebackground=abg, padx=20, command=guide_rps)
                how_play.place(x=492, y=865)
                t = tk.Label(mem,image = tri,bg=bagr).place(x=32,y=130)
                q = tk.Label(mem, image=qwad, bg=bagr).place(x=314, y=130)
                c = tk.Label(mem, image=cir, bg=bagr).place(x=614, y=130)
                r = tk.Label(mem, image=romb, bg=bagr).place(x=914, y=130)
                for i in range (5):
                    globals()["lbl" + str(i)] = tk.Label(mem,fg=tex,bg=bbg,padx=101,pady=90)
                    globals()["lbl" + str(i)].place(x=58+i*220,y=450)
                    globals()["lblal" + str(i)] = tk.Label(mem, fg=tex, bg=bbg,text = i + 1,font=("arial", 70, "bold"))
                    globals()["lblal" + str(i)].place(x=132 + i * 220, y=492)
                mem.focus_set()
                mem.bind("<Escape>", back_memory)


                def stat_mem():

                    sound_keyboard.play()
                    global ajk

                    def ba():
                        sound_keyboard.play()
                        ajk.destroy()
                        stat.configure(command=stat_mem)

                    def upd():
                        try:
                            t.configure(text=f"ВРЕМЯ В ИГРЕ:\n{time(data['mem_time'])}")
                            window.after(10, upd)
                        except:
                            return
                    ajk = tk.Frame(mem,bg=bbg,height=250,width=300)
                    ajk.place(x=802,y=655)
                    tk.Label(ajk, bg=bbg, text="СТАТИСТИКА", font=("arial", 32, "bold")).place(x=0, y=2)
                    tk.Label(ajk, bg=bbg, text=f"СЫГРАНО: {data['mem_games']}", font=("arial", 25, "bold")).place(x=-2, y=55)
                    t = tk.Label(ajk, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['mem_time'])}", font=("arial", 25, "bold"))
                    t.place(x=-2, y=135)
                    tr = tk.Label(ajk, bg=bbg, text=f"МАКС. : {data['mem_max']}", font=("arial", 25, "bold"))
                    tr.place(x=-2,y=95)
                    upd()
                    stat.configure(command=ba)
                stat = tk.Button(mem, image=stat_im, relief='flat', activebackground=bagr, width=85, height=80,
                                      bg=bagr, command=stat_mem, compound='top', text='СТАТИСТИКА',
                                      font=('arial', 10, 'bold'))
                stat.place(x=1100, y=807)
                mem.pack()
            menu_mem()

        def bingo(j=False):
            global b_t
            b_t = True

            def bingo_track_time():
                if b_t:
                    data['b_time'] += 1
                else:
                    return
                window.after(1000, bingo_track_time)
            if j:
                bingo_track_time()
            data["b_games"] += 1
            data['sologames'] += 1
            data['games'] += 1
            sound_menu.play()
            if BACK:
                sound_back.play()

            def play_5():
                sound_play.play()
                if BACK:
                    sound_back.play()
                from random import sample,shuffle
                global end, ij, afg, stop, lbl, gs, count,zx,zxc,flf,gh,chet
                gs = []
                zxc = []
                zx = []
                afg = [i for i in range(1,76)]
                shuffle(afg)
                stop = False
                ij = 0
                count= 0
                gh = 1000
                end = False
                kl = tk.Frame(window, width=1200, height=900, bg=bagr,)
                chet = tk.Label(kl,bg=bagr,text=f"СЧЕТ: {gh}",font=("Arial", 60, "bold"))
                chet.place(x=750,y=0)
                tr = []
                lbl = tk.Label(kl,font=("Arial", 80, "bold"),bg=bagr)
                lbl.place(x=525,y=10)

                def plaz():
                    global stop
                    stop = False
                    flf.configure(image=stp, command=step)
                    update_label()

                def step():
                    global stop, ds, gh
                    gh -= 25
                    if gh < 0:
                        gh = 0
                    chet.configure(text=f"СЧЕТ: {gh}")
                    if ds:
                        window.after_cancel(ds)
                    stop = True
                    flf.configure(image=pla,command=plaz)
                flf = tk.Button(kl,bg=bbg,image=stp,relief="flat",command=step,activebackground=bbg)
                flf.place(x=1050,y=772)

                def back_play_76(g="g"):
                    global BACK, solo_Time
                    solo_Time = False
                    BACK = True
                    global stop
                    stop = True
                    kl.destroy()
                    bingo()
                kl.focus_set()
                kl.bind("<Escape>",back_play_76)
                f = tk.Button(kl, image=imag, bg=bagr, command=back_play_76, activebackground=bagr,
                               relief="flat", width=60, height=50,)
                f.place(x=20, y=20)
                def ennd():

                    def start():
                        global stop
                        labl.destroy()
                        bttn.destroy()
                        bttn2.destroy()
                        k.destroy()
                        stop = False
                        update_label()

                    def ent():
                        global stop,lbl,gs,zx,count,flf,gh
                        lbl.destroy()
                        flf.configure(state="disabled")
                        stop = True
                        dd = tk.Label(text=f"ПРОИГРЫШЬ({gh})",font=("Arial", 70, "bold"),bg=bagr,fg=red)
                        labl.destroy()
                        bttn.destroy()
                        bttn2.destroy()
                        k.destroy()
                        for i in range(5):
                            for j in range(5):
                                globals()[f"btn{i}{j}"].configure(command="")
                        for i in zxc:
                            if i in tr and not i in gs:
                                gh -= 150
                                if gh < 0:
                                    gh = 0
                                if count != 12:
                                    globals()[f"btn{zx[count]}"].configure(bg="yellow")
                            if i not in tr:
                                gh -= 100
                                if gh < 0:
                                    gh = 0
                                if count != 12:
                                    globals()[f"btn{zx[count]}"].configure(bg=red)
                            if i in tr and i in gs:
                                gh += 100
                            count += 1
                        if set(zxc).issubset(tr):
                            sound_win.play()
                            data['wins'] += 1
                            data['solowins'] += 1
                            dd.configure(text=f"ПОБЕДА({gh})",fg=green)
                            dd.place(x=280,y=10)
                        else:
                            sound_lose.play()
                            data['loses'] += 1
                            data['sololoses'] += 1
                            dd.configure(text=f"ПРОИГРЫШЬ({gh})")
                            dd.place(x=220,y=10)
                        data['bing_count'] += gh
                        chet.destroy()

                    global stop, ds
                    stop=True
                    if ds:
                        window.after_cancel(ds)
                    k = tk.Label(bg=bagr,pady=150,padx=363)
                    k.place(x=236,y=200)
                    labl = tk.Label(k,text="ВЫ УВЕРЕНЫ?",font=("Arial", 70, "bold"),bg=bagr)
                    labl.place(x=10,y=20)
                    bttn = tk.Button(k,text="ДА",font=("Arial", 40, "bold"),bg=green,relief="flat",
                                     command = ent,activebackground=green,padx=15)
                    bttn.place(x=10,y=200)
                    bttn2 = tk.Button(k,text="НЕТ", font=("Arial", 40, "bold"), bg=red, relief="flat",
                                      command = start,activebackground=red)
                    bttn2.place(x=564, y=200)

                def update_label():
                    global ij, stop, lbl, ds, gh
                    if stop:
                        return
                    if ij < len(afg):
                        value = afg[ij]
                        tr.append(value)
                        lbl.config(text=value)
                        if len(str(value)) == 1:
                            lbl.place(x=560,y=15)
                        else:lbl.place(x=540,y=15)
                        ij += 1
                        ds = window.after(2300, update_label)
                    else:
                        lbl.config(text="ВСЕ ЦИФРЫ ПОКАЗАНЫ!",font=("Arial", 70, "bold"))
                        gh = gh - 2200
                        flf.configure(image=pla, command="")
                        lbl.place(x=10,y=15)
                        f.place(x=20,y=120)
                update_label()

                def get_green(x,y):
                    global gs
                    gs.append(zxc[x*5+y])
                    globals()[f"btn{x}{y}"].configure(bg=green,command=lambda x=x,y=y: get_red(x,y))
                    if x == 2 and y==2:
                        globals()[f"btn{x}{y}"].configure(bg=bbg)

                def get_red(x,y):
                    global gs
                    gs.remove(zxc[x*5+y])
                    globals()[f"btn{x}{y}"].configure(bg=bbg, command=lambda x=x, y=y: get_green(x, y))
                bing.destroy()
                b = sample([i for i in range(1, 16)],k=5)
                ing = sample([i for i in range(16, 31)],k=5)
                n = sample([i for i in range(31, 46)],k=5)
                g = sample([i for i in range(46, 61)],k=5)
                o = sample([i for i in range(61, 76)],k=5)
                for i in range(5):
                    for j in range(5):
                        if i == 0:
                            zxc.append(b[j])
                            zx.append(f"{i}{j}")
                            globals()[f"btn{i}{j}"] = tk.Button(kl, text=zxc[-1], bg=bbg, font=("Arial", 52, "bold"),relief="flat",
                                                                  activebackground=abg,padx=9,command = lambda x = i,y=j: get_green(x,y))
                            if len(str(b[j])) == 1:
                                globals()[f"btn{i}{j}"].configure(padx=28)
                        if i == 1:
                            zxc.append(ing[j])
                            zx.append(f"{i}{j}")
                            globals()[f"btn{i}{j}"] = tk.Button(kl, text=zxc[-1], bg=bbg, font=("Arial", 52, "bold"),relief="flat",
                                                                  activebackground=abg,padx=9,command = lambda x = i,y=j: get_green(x,y))
                        if i == 2:
                            zxc.append(n[j])
                            zx.append(f"{i}{j}")
                            globals()[f"btn{i}{j}"] = tk.Button(kl, text=zxc[-1], bg=bbg, font=("Arial", 52, "bold"),relief="flat",
                                                                  activebackground=abg,padx=9,command = lambda x = i,y=j: get_green(x,y))
                        if i == 3:
                            zxc.append(g[j])
                            zx.append(f"{i}{j}")
                            globals()[f"btn{i}{j}"] = tk.Button(kl, text=zxc[-1], bg=bbg, font=("Arial", 52, "bold"),relief="flat",
                                                                  activebackground=abg,padx=9,command = lambda x = i,y=j: get_green(x,y))
                        if i == 4:
                            zxc.append(o[j])
                            zx.append(f"{i}{j}")
                            globals()[f"btn{i}{j}"] = tk.Button(kl, text=zxc[-1], bg=bbg, font=("Arial", 52, "bold"),relief="flat",
                                                                  activebackground=abg,padx=9,command =lambda x = i,y=j: get_green(x,y))
                        if i == 2 and j == 2:
                            globals()[f"btn{i}{j}"].configure(image = galk,height=134,width=148,activebackground=bbg,command=ennd)
                        globals()[f"btn{i}{j}"].place(x=193+i*165,y=150+j*150)
                kl.pack()
            solo_menu.destroy()

            def back_play_5(g="g"):
                global b_t
                b_t = False
                global BACK, solo_Time
                solo_Time = False
                BACK = True
                bing.destroy()
                solo()
            bing = tk.Frame(window, width=1200, height=900, bg=bagr)
            tk.Button(bing,text="ИГРАТЬ",bg=bbg,activebackground=abg,relief="flat",font=("Arial", 45, "bold"),
                      command=play_5).place(x=455,y=770)
            tk.Label(bing,text="БИНГО",bg=bbg,font=("Arial", 60, "bold"),padx=280).place(x=178,y=10)
            for i in range (5):
                b1 = tk.Label(bing, text="Б", bg=bbg, font=("Arial", 70, "bold"),padx=40,pady=5)
                i2 = tk.Label(bing, text="И", bg=bbg, font=("Arial", 70, "bold"),padx=40,pady=5)
                n3 = tk.Label(bing, text="Н", bg=bbg, font=("Arial", 70, "bold"),padx=40,pady=5)
                g4 = tk.Label(bing, text="Г", bg=bbg, font=("Arial", 70, "bold"),padx=47,pady=5)
                o5 = tk.Label(bing, text="О", bg=bbg, font=("Arial", 70, "bold"),padx=37,pady=5)
                if i == 2:
                    n3.configure(image=galk,height=118,width=147)
                b1.place(x=178,y=115+i*131)
                i2.place(x=351.75,y=115+i*131)
                n3.place(x=525.5,y=115+i*131)
                g4.place(x=699.25,y=115+i*131)
                o5.place(x=873,y=115+i*131)
            f = tk.Button(bing, image=imag, bg=bagr, command=back_play_5, activebackground=bagr,
                           relief="flat", width=60, height=50, ).place(x=20,y=20)
            bing.focus_set()
            bing.bind("<Escape>", back_play_5)

            def guide_rps():
                sound_keyboard.play()
                global gh3
                how_play.configure(text="СКРЫТЬ", command=cl_rps)
                how_play.place(x=10, y=846)
                gh3 = tk.Label(bing, bg=bbg,
                               text="КАК ИГРАТЬ В БИНГО?\nПОСЛЕ ТОГО, КАК ВЫ НАЖМЕТЕ КНОПКУ 'ИГРАТЬ',\nВАМ НУЖНО БУДЕТ СЛЕДИТЬ ЗА ЦИФРАМИ СВЕРХУ,\nКОТОРЫЕ БУДУТ ПОЯВЛЯТЬСЯ 1 РАЗ,\nЕСЛИ ЧИСЛО СВЕРХУ СОВПАДАЕТ С ЧИСЛОМ НА ПОЛЕ ИГРЫ,\nНАЖМИТЕ НА ЭТО ЧИСЛО НА ПОЛЕ\nИ ОНО СТАНЕТ ЗЕЛЕНЫМ.\nИГРА ИДЕТ ДО ТЕХ ПОР, ПОКА ВЫ НЕ НААЖМЕТЕ НА ГАЛОЧКУ,\n ПОСЛЕ ЭТОГО ПОДСЧИТАЮТСЯ ОЧКИ(ПРОПУЩЕННОЕ ЧИСЛО -150, ПАУЗА -25, ВЕРНОЕ ЧИСЛО +100)\nЕСЛИ ВСЕ ЧИСЛА БЫЛИ ПОКАЗАНЫ, ТО СЧЕТ ДЕЛИТСЯ НА 2"
                               , justify="center", font=("arial", 16, "bold"),pady=5)
                gh3.place(x=58, y=246)

            def cl_rps():
                sound_keyboard.play()
                global gh3
                gh3.destroy()
                how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                how_play.place(x=10, y=846)

            how_play = tk.Button(bing, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"), relief="flat",
                                 activebackground=abg, padx=20, command=guide_rps)
            how_play.place(x=10, y=846)

            def stat_b():
                sound_keyboard.play()

                def ba():
                    sound_keyboard.play()
                    ab.destroy()
                    stat.configure(command=stat_b)

                def upd11():
                    try:
                        yt.configure(text=f"ОБЩИЙ СЧЕТ: {data['bing_count']}")
                        t.configure(text=f"В ИГРЕ: {time(data['b_time'])}")
                        window.after(100, upd11)
                    except:
                        return

                ab = tk.Frame(bing, bg=bbg, height=253, width=400)
                ab.place(x=699, y=508)
                tk.Label(ab, bg=bbg, text="СТАТИСТИКА", font=("arial", 35, "bold")).place(x=38, y=-2)
                tk.Label(ab, bg=bbg, text=f"СЫГРАНО: {data["b_games"]}", font=("arial", 25, "bold")).place(x=0, y=55)
                yt = tk.Label(ab, bg=bbg, text=f"ОБЩИЙ СЧЕТ: {data['bing_count']}",
                              font=("arial", 25, "bold"))
                yt.place(x=0, y=95)
                t = tk.Label(ab, bg=bbg, text=f"В ИГРЕ: {time(data['b_time'])}", font=("arial", 25, "bold"))
                t.place(x=0, y=135)
                window.after(10, upd11)
                stat.configure(command=ba)
            stat = tk.Button(bing, image=stat_im, relief='flat', activebackground=bagr, width=85,
                             height=80, bg=bagr, command=stat_b, compound='top', text='СТАТИСТИКА',
                             font=('arial', 10, 'bold'))
            stat.place(x=1100, y=807)
            bing.pack()


        menu.destroy()
        solo_menu = tk.Frame(window, bg=bagr,)
        tk.Label(solo_menu,text = "ВЫБЕРИТЕ ИГРУ", bg=bagr, fg=tex,font=("arial", 75, "bold"), anchor="n",padx = 200).pack()
        tk.Button(solo_menu, text="ВИСЕЛИЦА", bg=bbg, fg=tex, font=("arial", 40, "bold"),padx = 235,
                         activebackground=abg, pady=7,relief = "flat",command= visilica).pack(pady = 15)
        tk.Button(solo_menu, text="КАМЕНЬ,НОЖНИЦЫ,БУМАГА", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",
                         activebackground=abg, pady=7,command= RockPaperScissors).pack(pady = 15)
        tk.Button(solo_menu, text="УГАДАЙ ЧИСЛО", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 175,
                         activebackground=abg, pady=7, command = guess_number ).pack(pady=15)
        tk.Button(solo_menu, text="ПОВТОРИ ЗА МНОЙ", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 122,
                         activebackground=abg, pady=7, command = memory).pack(pady=15)
        tk.Button(solo_menu, text="БИНГО", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 292,
                         activebackground=abg, pady=7, command=lambda x=True:bingo(x)).pack(pady=15)
        tk.Button(solo_menu,width=60,height=50,image = imag,relief = "flat",command=back,activebackground=bagr).place(x=20, y=20)

        solo_menu.focus_set()
        solo_menu.bind('<Escape>',back)
        solo_menu.pack()


    def multy_menu():
        global BACK, multy_time,ss
        ss = True
        def mu_track_time():
            if ss:
                data['multytime'] += 1
            else: return
            window.after(1000, mu_track_time)
        if multy_time:
            mu_track_time()
        global BACK
        if BACK:
            sound_back.play()
            BACK = False
        else:sound_menu.play()
        #функция выбора совместной игры
        window.geometry('1200x900+352+55')

        def back(g="f"):
            global ss
            global multy_time
            multy_time = False
            ss = False
            #фунця возврата в меню
            global BACK
            BACK = True
            multy.destroy()
            menu_1()

        def vis2():
            global vis2_t,ght1
            vis2_t = True
            ght1 = []
            def vis2_track_time():
                if vis2_t:
                    data['vis2_time'] += 1
                else:
                    return
                window.after(1000, vis2_track_time)
            vis2_track_time()
            data['games'] += 1
            data['multygames'] += 1
            sound_play.play()
            global word,w,fi,te,coun,gh,er,fgh,vi,count,fd
            coun = 0
            vi = tk.Frame(window, bg=bagr, height=900, width=1200)
            word = ""
            fi = True
            count = 10
            gh =  False
            fgh = False

            def plus():
                sound_keyboard.play()
                global count,fd
                if count != 15:
                    count += 1
                    fd.configure(text=f"ПОПЫТОК:     {count}")
                    if count >= 10:
                        pl.place(x=736)

            def min():
                sound_keyboard.play()
                global count,fd
                if count != 1:
                    count -= 1
                    fd.configure(text = f"ПОПЫТОК:     {count}")
                    if count < 10:
                        pl.place(x=712)

            def yy():
                sound_play.play()
                data['vis2_games'] += 1
                global vi,word,count
                def df():
                    if count == 9:
                        vic_print = tk.Label(game_vis, image=vic_image1, bg=bagr)
                    elif count == 8:
                        vic_print = tk.Label(game_vis, image=vic_image2, bg=bagr)
                    elif count == 7:
                        vic_print = tk.Label(game_vis, image=vic_image3, bg=bagr)
                    elif count == 6:
                        vic_print = tk.Label(game_vis, image=vic_image4, bg=bagr)
                    elif count == 5:
                        vic_print = tk.Label(game_vis, image=vic_image5, bg=bagr)
                    elif count == 4:
                        vic_print = tk.Label(game_vis, image=vic_image6, bg=bagr)
                    elif count == 3:
                        vic_print = tk.Label(game_vis, image=vic_image7, bg=bagr)
                    elif count == 2:
                        vic_print = tk.Label(game_vis, image=vic_image8, bg=bagr)
                    elif count == 1:
                        vic_print = tk.Label(game_vis, image=vic_image9, bg=bagr)
                    elif count == 0:
                        vic_print = tk.Label(game_vis, image=vic_image10, bg=bagr)
                    if count < 10:
                        vic_print.place(x=400, y=100)
                vi.destroy()
                game_vis = tk.Frame(window, bg=bagr, height=900, width=1200)

                def back_vic2(g="g"):
                    global vis2_t
                    vis2_t = False
                    global multy_time
                    multy_time = False
                    global BACK
                    BACK = True
                    game_vis.destroy()
                    multy_menu()
                back_vic2_button_1 = tk.Button(game_vis, image=imag, command=back_vic2, relief="flat",
                                                  activebackground=bagr,width=60,height=50, bg=bagr,
                                                  ).place(x=20, y=20)
                global guessed, correct, word,attempts
                guessed = []
                correct = []
                attempts = (tk.Label(game_vis, text=f"Осталось попыток: {count}!", bg=bagr, fg=tex,
                                         font=("arial", 30, "bold")))
                attempts.place(x=372, y=10)
                df()

                def check(letter):
                    global ght1
                    if letter in ght1:
                        return
                    ght1.append(letter)
                    data['vis2_try'] += 1
                    sound_keyboard.play()
                    global count

                    def end():
                        def again():
                            game_vis.destroy()
                            vis2()
                        again_button_2 = tk.Button(game_vis, text="ЗАНОВО", command=again, relief="flat",
                                                     activebackground=abg, font=("arial", 45, "bold"), bg=bbg).place(x=192,y=690)
                        back_vic_button_2 = tk.Button(game_vis, text="НАЗАД", command=back_vic2, relief="flat",
                                                        activebackground=abg, font=("arial", 45, "bold"), bg=bbg,
                                                        padx=29).place(x=692, y=690)
                        for i in range(32):
                            globals()[chr(1040 + i)].destroy()
                        game_vis.bind("<Key>", "")
                    guessed.append(letter)
                    if letter in word:
                        globals()[letter].config(bg="#00693E",state="disabled")
                        for num, alpha in enumerate(word):
                            if alpha == letter:
                                correct.append(letter)
                                globals()["lab" + str(num)].configure(text=letter)
                    else:
                        global count
                        count -= 1
                        globals()[letter].config(bg="#900020",state="disabled")
                        attempts.configure(text=f"Осталось попыток: {count}!")
                        df()
                    if set(correct) == set(word):
                        sound_win.play()
                        data['vis2_wins'] += 1
                        data['wins'] += 1
                        data['multywins'] += 1
                        attempts.configure(text=f"Вы отгадали слово {word}!",)
                        if len(word) == 3:
                            attempts.place(x=330, y=10)
                        if len(word) == 4:
                            attempts.place(x=320, y=10)
                        if len(word) == 5:
                            attempts.place(x=310, y=10)
                        if len(word) == 6:
                            attempts.place(x=300, y=10)
                        if len(word) == 7:
                            attempts.place(x=290, y=10)
                        if len(word) == 8:
                            attempts.place(x=280, y=10)
                        end()
                    elif count == 0:
                        sound_lose.play()
                        data['loses'] += 1
                        data['multyloses'] += 1
                        data['vis2_lose'] += 1
                        attempts.configure(text=f"Вы не отгадали слово {word}!")
                        if len(word) == 3:
                            attempts.place(x=313, y=10)
                        if len(word) == 4:
                            attempts.place(x=304, y=10)
                        if len(word) == 5:
                            attempts.place(x=295, y=10)
                        if len(word) == 6:
                            attempts.place(x=286, y=10)
                        if len(word) == 7:
                            attempts.place(x=277, y=10)
                        if len(word) == 8:
                            attempts.place(x=268, y=10)
                        for i in range (len(word)):
                            if word[i] not in correct:
                                globals()["lab" + str(i)].configure(text=word[i],fg="#900020")
                        end()
                for i in range(11):
                    globals()[chr(1040 + i)] = tk.Button(game_vis, text=chr(1040 + i), bg=bbg, fg=tex,
                                                             font=("arial", 35, "bold"),
                                                             relief="flat", activebackground=abg,
                                                             command=lambda letter=f"{chr(1040 + i)}",: check(letter, ))
                    globals()[chr(1040 + i)].place(x=141 + i * 85, y=620, width=70, height=70)
                for i in range(11):
                    globals()[chr(1051 + i)] = (tk.Button(game_vis, text=chr(1051 + i), bg=bbg, fg=tex,
                                                              font=("arial", 35, "bold"), relief="flat",
                                                              activebackground=abg,
                                                              command=lambda letter=f"{chr(1051 + i)}": check(letter)))
                    globals()[chr(1051 + i)].place(x=141 + i * 85, y=700, width=70, height=70, )
                for i in range(10):
                    globals()[chr(1062 + i)] = tk.Button(game_vis, text=chr(1062 + i), bg=bbg, fg=tex,
                                                             font=("arial", 35, "bold"),
                                                             relief="flat", activebackground=abg,
                                                             command=lambda letter=f"{chr(1062 + i)}": check(letter))
                    globals()[chr(1062 + i)].place(x=184 + i * 85, y=780, width=70, height=70)
                for i in range(len(word)):
                    if len(word) == 8:
                        d=123
                    if len(word) == 7:
                        d=183
                    if len(word) == 6:
                        d=243
                    if len(word) == 5:
                        d=303
                    if len(word) == 4:
                        d=363
                    if len(word) == 3:
                        d=423
                    globals()["lab" + str(i)] = (
                        tk.Label(game_vis, text="  ", bg=bbg, fg=tex, font=("arial", 70, "bold"), padx=29, ))
                    globals()["lab" + str(i)].place(x=d + i * 120, y=455, width=110, height=110)

                    def ggg(event):
                        char = event.char
                        if char in "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" and char != "":
                            char = char.upper()
                            check(char)
                    game_vis.bind("<Key>", ggg)
                    game_vis.bind('<Escape>',back_vic2)
                    game_vis.focus_set()

                    def stat_vis():

                        def ba():
                            ab.destroy()
                            stat.configure(command=stat_vis)

                        def upd():
                            try:
                                tr.configure(text=f"ПОПЫТОК: {data['vis2_try']}")
                                t.configure(text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis2_time'])}")
                                window.after(10, upd)
                            except:
                                return

                        ab = tk.Frame(game_vis, bg=bbg, height=330, width=335)
                        ab.place(x=860, y=120)
                        tk.Label(ab, bg=bbg, text="СТАТИСТИКА", font=("arial", 35, "bold")).place(x=5, y=-2)
                        a = tk.Label(ab, bg=bbg, text=f"ЗАГАДАНО: {data['vis2_games']}", font=("arial", 25, "bold"))
                        a.place(x=-1, y=51)
                        w = tk.Label(ab, bg=bbg, text=f"ПОБЕД: {data['vis2_wins']}", font=("arial", 25, "bold"))
                        w.place(x=-1, y=91)
                        l = tk.Label(ab, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['vis2_lose']}", font=("arial", 25, "bold"))
                        l.place(x=-1, y=131)
                        t = tk.Label(ab, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis2_time'])}",
                                     font=("arial", 25, "bold"))
                        t.place(x=-1, y=171)
                        tr = tk.Label(ab, bg=bbg, text=f"ПОПЫТОК: {data['vis2_try']}",
                                     font=("arial", 25, "bold"))
                        tr.place(x=-1,y=251)
                        window.after(10, upd)
                        stat.configure(command=ba)

                    stat = tk.Button(game_vis, image=stat_im, relief='flat', activebackground=bagr, width=85,
                                     height=80, bg=bagr, command=stat_vis, compound='top', text='СТАТИСТИКА',
                                     font=('arial', 10, 'bold'))
                    stat.place(x=1100, y=5)
                game_vis.pack()

            def slo():
                global ba12
                try:ba12()
                except:None
                def d():
                    dsa.destroy()
                    y.destroy()
                    n.destroy()
                    dd.configure(command=slo)
                    for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЬЫЪЭЮЧШЩЯ":
                        globals()[i].configure(state="normal")
                dd.configure(command="")
                dsa = tk.Label(vi,bg=bagr,text=f"ЗАГАДАТЬ СЛОВО: '{word}'?",font=("Arial", 50, "bold"))
                y = tk.Button(vi,text="ДА",font=("Arial", 50, "bold"),bg=green,relief="flat",padx=22,activebackground=green,command = yy)
                n = tk.Button(vi,text="НЕТ",font=("Arial", 50, "bold"),bg=red, command = d,relief="flat",activebackground=red)
                dsa.place(x=250-25*len(word),y=170)
                y.place(x=250-25*len(word),y=270)
                n.place(x=730+25*len(word),y=270)
                for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЬЫЪЭЮЧШЩЯ":
                    globals()[i].configure(state="disabled")
            def wrd(x):
                global ght1
                sound_keyboard.play()
                global word,fi,te,coun,gh,er,fgh,dd,fd
                if x != "del":
                    x = x.upper()
                if fi and x != "del":
                    fi = False
                    word = x
                    coun += 1
                else:
                    if x == "del" and coun != 0:
                        word = word[0:-1]
                        coun -= 1
                        if gh:
                            er.destroy()
                            mi.place(x=640, y=405)
                            if count >= 10:
                                pl.place(x=736, y=405)
                            else: pl.place(x=712, y=405)
                            fd.place(x=412, y=405)
                            coun -= 1
                            gh = False
                    if coun <= 8 and x != "del":
                        if coun <= 7:
                            word = word+x
                        coun += 1
                if coun >= 3:
                    if not fgh:
                        dd = tk.Button(vi,bg=bbg,image=galk,width=120,height=120,relief="flat",command=slo)
                        dd.place(x=855, y=459)
                        fgh = True
                if coun < 3 and fgh:
                    dd.destroy()
                    fgh = False
                if coun <= 8:
                    te.config(text=word)
                    if len(word) == 1:
                        te.place(x=466,y=459)
                    if len(word) == 2:
                        te.place(x=428,y=459)
                    if len(word) == 3:
                        te.place(x=390,y=459)
                    if len(word) == 4:
                        te.place(x=352,y=459)
                    if len(word) == 5:
                        te.place(x=314,y=459)
                    if len(word) == 6:
                        te.place(x=276,y=459)
                    if len(word) == 7:
                        te.place(x=238,y=459)
                    if len(word) == 8:
                        te.place(x=200,y=459)
                else:
                    if not gh:
                        er = tk.Label(vi, bg=bagr, fg=red, font=("Arial", 15, "bold"),
                                      text="СЛОВО ДОЖНО СОДЕРЖАТЬ ОТ 3 ДО 8 БУКВ")
                        mi.place(x=640, y=380)
                        if count >= 10:
                            pl.place(x=736, y=380)
                        else:
                            pl.place(x=712, y=380)
                        fd.place(x=412, y=380)
                        er.place(x=300,y=425)
                        gh = True
            la = tk.Label(vi,bg=bbg,padx=475,pady=55).place(x=30,y=458)
            te = tk.Label(vi,bg=bbg,font=("Arial",79,"bold"),)
            te.place(x=463,y=459)
            g = tk.Label(vi,bg=bagr,font=("Arial",75,"bold"),text="ЗАГАДАЙТЕ СЛОВО").place(x=100,y=10)
            er = tk.Label(vi,bg=bagr,fg=red,font=("Arial",15,"bold"),text="СЛОВО ДОЖНО СОДЕРЖАТЬ ОТ 3 ДО 8 БУКВ")
            fd = tk.Label(vi,bg=bagr,text=f"ПОПЫТОК:     {count}",font=("Arial",30,"bold"))
            pl = tk.Button(vi,text="+",command=plus,bg=bagr,relief="flat",font=("Arial",19,"bold"),activebackground=green,padx=8)
            mi = tk.Button(vi,text="-",command=min,bg=bagr,relief="flat",font=("Arial",19,"bold"),activebackground=red,padx=11)
            mi.place(x=640,y=405)
            pl.place(x=736,y=405)
            fd.place(x=412,y=405)

            def back_vis2(g="g"):
                global vis2_t
                global multy_time
                multy_time = False
                vis2_t = False
                global BACK
                BACK = True
                vi.destroy()
                multy_menu()
            f = tk.Button(vi, image=imag, bg=bagr, command=back_vis2, activebackground=bagr,
                          relief="flat", width=60, height=50, ).place(x=20, y=20)
            del_b = tk.Button(vi,image=del_png, bg=bagr, activebackground=bagr,
                                relief="flat", command=lambda number="del": wrd(number))
            del_b.place(x=1000, y=460)
            multy.destroy()
            for i in range(11):
                globals()[chr(1040 + i)] = tk.Button(vi, text=chr(1040 + i), bg=bbg, fg=tex,
                                                     font=("arial", 35, "bold"),
                                                     relief="flat", activebackground=abg,
                                                     command=lambda letter=f"{chr(1040 + i)}": wrd(letter))
                globals()[chr(1040 + i)].place(x=141 + i * 85, y=640, width=70, height=70)
            for i in range(11):
                globals()[chr(1051 + i)] = (tk.Button(vi, text=chr(1051 + i), bg=bbg, fg=tex,
                                                      font=("arial", 35, "bold"), relief="flat",
                                                      activebackground=abg,
                                                      command=lambda letter=f"{chr(1051 + i)}": wrd(letter)))
                globals()[chr(1051 + i)].place(x=141 + i * 85, y=720, width=70, height=70,)
            for i in range(10):
                globals()[chr(1062 + i)] = tk.Button(vi, text=chr(1062 + i), bg=bbg, fg=tex,
                                                     font=("arial", 35, "bold"),
                                                     relief="flat", activebackground=abg,
                                                     command=lambda letter=f"{chr(1062 + i)}": wrd(letter))
                globals()[chr(1062 + i)].place(x=184 + i * 85, y=800, width=70, height=70)

            def kj(event):
                char = event.char
                if char in "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" and char != "":
                    wrd(char)

            def kjj(event):
                wrd("del")
            vi.focus_set()
            vi.bind("<KeyPress-BackSpace>",kjj)
            vi.bind("<KeyPress>", kj)

            def entrr(g="g"):
                global coun
                if coun >= 3:
                    slo()
            vi.bind("<Return>", entrr)
            vi.bind('<Escape>',back_vis2)

            def guide_rps():
                sound_keyboard.play()
                global gh3
                how_play.configure(text="СКРЫТЬ", command=cl_rps)
                how_play.place(x=520, y=590)
                gh3 = tk.Label(vi, bg=bbg,
                               text="КАК ИГРАТЬ В ВИСЕЛИЦУ ДЛЯ 2?\nСНАЧАЛА ИГРОК 1 ДОЛЖЕН ЗАГАДАТЬ СЛОВО И УСТАНОВИТЬ КОЛ-ВО ПОПЫТОК ДЛЯ ИГРОКА 2,\nЗАТЕМ ИГРОК 2 СЫГРАЕТ В ОБЫЧНУЮ ВИСЕЛИЦУ, НО СО СЛОВОМ, ЗАГАДАННЫМ ИГРОКОМ 1."
                               , justify="center", font=("arial", 18, "bold"),pady=5)
                gh3.place(x=5, y=246)

            def cl_rps():
                sound_keyboard.play()
                global gh3
                gh3.destroy()
                how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                how_play.place(x=492, y=590)

            how_play = tk.Button(vi, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"), relief="flat",
                                 activebackground=abg, padx=20, command=guide_rps)
            how_play.place(x=492, y=590)


            def stat_vis2():
                global ba12
                sound_keyboard.play()

                def ba12():
                    sound_keyboard.play()
                    ab3.destroy()
                    stat.configure(command=stat_vis2)

                def upd():
                    try:
                        t.configure(text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis2_time'])}")
                        window.after(10, upd)
                    except:
                        return

                ab3 = tk.Frame(vi, bg=bbg, height=330, width=335)
                ab3.place(x=860, y=120)
                tk.Label(ab3, bg=bbg, text="СТАТИСТИКА", font=("arial", 35, "bold")).place(x=5, y=-2)
                a = tk.Label(ab3, bg=bbg, text=f"ЗАГАДАНО: {data['vis2_games']}", font=("arial", 25, "bold"))
                a.place(x=-1, y=51)
                w = tk.Label(ab3, bg=bbg, text=f"ПОБЕД: {data['vis2_wins']}", font=("arial", 25, "bold"))
                w.place(x=-1, y=91)
                l = tk.Label(ab3, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['vis2_lose']}", font=("arial", 25, "bold"))
                l.place(x=-1, y=131)
                t = tk.Label(ab3, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis2_time'])}", font=("arial", 25, "bold"))
                t.place(x=-1, y=171)
                window.after(10, upd)
                stat.configure(command=ba12)

            stat = tk.Button(vi, image=stat_im, relief='flat', activebackground=bagr, width=85,
                             height=80, bg=bagr, command=stat_vis2, compound='top', text='СТАТИСТИКА',
                             font=('arial', 10, 'bold'))
            stat.place(x=1100, y=5)
            vi.pack()


        def slova():
            data["sl_games"] += 1
            global sl_t
            sl_t = True
            def sl_track_time():
                if sl_t:
                    data['sl_time'] += 1
                else:
                    return
                window.after(1000, sl_track_time)
            sl_track_time()
            data['games'] += 1
            data['multygames'] += 1
            sound_play.play()
            global word,first,cont,err1,err_lbl_1,err_lbl,count,tr,inpt_btn,inpt,cnt1,cnt2,fir
            sl = tk.Frame(window,bg=bagr,width=1600,height=900)
            fir = False
            cnt1 = 0
            cnt2 = 0
            first = True
            err1 = True
            err_lbl_1 = False
            words = []
            count = 0
            cont = 0
            word = ""
            multy.destroy()
            window.geometry('1600x900+152+55')
            polosa_p = tk.Label(sl,image=pol,bg=bagr).place(x=793,y=-2)
            mouse_lbl = tk.Label(sl,image=mos,bg=bagr).place(x=1161,y=10)
            keybord_lbl = tk.Label(sl,image=klav,bg=bagr).place(x=277,y=10)
            tr = tk.Label(sl,bd=0,image=triu)
            tr.place(x=807,y=75)
            pods1 = tk.Label(sl,text="ДЛЯ ОТПРАВКИ ИСПОЛЬЗУЙТЕ\n'ENTER'",bg=bbg,activebackground=abg,relief="flat",font=("arial", 35, "bold")).place(x=22,y=778)
            cnt1_lbl = tk.Label(sl,text=f"СЧЕТ: {cnt1}",bg=bbg,font=("arial", 35, "bold"))
            cnt1_lbl.place(x=810,y=0)
            cnt2_lbl = tk.Label(sl,text=f"СЧЕТ: {cnt2}",bg=bbg,font=("arial", 35, "bold"))
            cnt2_lbl.place(x=605,y=0)

            def zan():
                sl.destroy()
                slova()

            def player1(g="g"):
                global inpt,letter,tr,slovo,cont,word,cnt2
                word = inpt.get()
                if len(word) < 2:
                    return
                cont = 0
                inpt.delete(0, tk.END)
                inpt.insert(0, "")
                slovo.destroy()
                if word[0] != letter or word in words:
                    sound_lose.play()
                    data['loses'] += 1
                    data['multyloses'] += 1
                    if word[0] != letter:
                        d = "ПЕРВАЯ БУКВА НЕ СОВПАДАЕТ\nС ПОСЛЕДНЕЙ БУКВОЙ ПРЕДЫДУЩЕГО СЛОВА"
                    else:
                        d = "СЛОВО УЖЕ БЫЛО ИСПОЛЬЗОВАНО РАНЕЕ"
                    tk.Label(sl, bg=bbg, text=f"ПОБЕДА", font=("arial", 43, "bold"), fg=green).place(x=1080, y=300)
                    if d == "ПЕРВАЯ БУКВА НЕ СОВПАДАЕТ\nС ПОСЛЕДНЕЙ БУКВОЙ ПРЕДЫДУЩЕГО СЛОВА":
                        tk.Label(sl, bg=bbg, text=f"ПРОИГРЫШЬ,\n {d}", font=("arial", 23, "bold"), fg=red,justify="center").place(x=26, y=260)
                    if d == "СЛОВО УЖЕ БЫЛО ИСПОЛЬЗОВАНО РАНЕЕ":
                        tk.Label(sl, bg=bbg, text=f"ПРОИГРЫШЬ,\n {d}", font=("arial", 23, "bold"), fg=red,justify="center").place(x=51, y=295)
                    zano = tk.Button(sl, command=zan, bg=bbg, activebackground=abg, relief="flat",font=("arial", 40, "bold"), text="ЗАНОВО").place(x=115, y=520)
                    ba = tk.Button(sl, command=back_slova, bg=bbg, activebackground=abg, relief="flat",font=("arial", 40, "bold"), text="НАЗАД",padx=24).place(x=405, y=520)
                    fake = tk.Label(sl, pady=56, padx=390, bg=bbg).place(x=5, y=379)
                    global sl_t
                    sl_t = False
                    sl.focus_set()
                    inpt_btn.configure(command="")
                    for i in range(11):
                        globals()[chr(1040 + i)].configure(state="disabled")
                    for i in range(11):
                        globals()[chr(1051 + i)].configure(state="disabled")
                    for i in range(10):
                        globals()[chr(1062 + i)].configure(state="disabled")
                    globals()["del"].configure(state="disabled")
                    inpt.configure(state="disabled", bg=bbg)
                    sl.focus_set()
                    sl.bind('<Escape>', back_slova)
                    return
                letter = word[-1]
                if letter in "ьЬъыЪЫ":
                    letter = word[-2]
                    if letter in "ьЬъыЪЫ":
                        letter = word[-3]
                        if letter in "ьЬъыЪЫ":
                            letter = word[-4]
                            if letter in "ьЬъыЪЫ":
                                letter = word[-5]
                sound_short_win.play()
                data['wins'] += 1
                data['multywins'] += 1
                data['sl_count2'] += 1
                cnt2 += 1
                cnt2_lbl.configure(text=f"СЧЕТ: {cnt2}")
                words.append(word)
                tr.destroy()
                tr = tk.Label(sl, bd=0, image=triu)
                tr.place(x=807, y=75)
                inpt.bind("<Return>","")
                slovo = tk.Label(sl,bg=bbg,text=f"({word})\nСЛОВО НА БУКВУ {letter}",font=("arial", 55, "bold"),justify="center")
                inpt_btn.configure(command=player2)
                slovo.place(x=838,y=198)
                word = letter
                wrd.configure(text=word)
                wrd.place(x=1200-38,y=378)

            def player2():
                global word,tr,wrd,inpt,letter,slovo,cont,cnt1,fir
                try:slovo.destroy()
                except:None
                if len(word) < 2:
                    return
                sound_short_win.play()
                cont = 0
                inpt_btn.configure(command="")
                try:
                    if (word[0] != letter or word in words) and fir:
                        data['loses'] += 1
                        data['multyloses'] += 1
                        sound_lose.play()
                        if word[0] != letter:
                            d = "ПЕРВАЯ БУКВА НЕ СОВПАДАЕТ\nС ПОСЛЕДНЕЙ БУКВОЙ ПРЕДЫДУЩЕГО СЛОВА"
                        else:
                            d = "СЛОВО УЖЕ БЫЛО ИСПОЛЬЗОВАНО РАНЕЕ"
                        tk.Label(sl, bg=bbg, text=f"ПОБЕДА", font=("arial", 43, "bold"), fg=green).place(x=272, y=303)
                        if d == "ПЕРВАЯ БУКВА НЕ СОВПАДАЕТ\nС ПОСЛЕДНЕЙ БУКВОЙ ПРЕДЫДУЩЕГО СЛОВА":
                            tk.Label(sl, bg=bbg, text=f"ПРОИГРЫШЬ,\n {d}", font=("arial", 23, "bold"), fg=red,
                                     justify="center").place(x=832, y=259)
                        if d == "СЛОВО УЖЕ БЫЛО ИСПОЛЬЗОВАНО РАНЕЕ":
                            tk.Label(sl, bg=bbg, text=f"ПРОИГРЫШЬ,\n {d}", font=("arial", 23, "bold"), fg=red,
                                     justify="center").place(x=858, y=295)
                        zano = tk.Button(sl, command=zan, bg=bbg, activebackground=abg, relief="flat",
                                         font=("arial", 40, "bold"), text="ЗАНОВО").place(x=115, y=520)
                        ba = tk.Button(sl, command=back_slova, bg=bbg, activebackground=abg, relief="flat",
                                       font=("arial", 40, "bold"), text="НАЗАД", padx=24).place(x=405, y=520)
                        fake = tk.Label(sl, pady=56, padx=390, bg=bbg).place(x=5, y=379)
                        sl.focus_set()
                        inpt_btn.configure(command="")
                        for i in range(11):
                            globals()[chr(1040 + i)].configure(state="disabled")
                        for i in range(11):
                            globals()[chr(1051 + i)].configure(state="disabled")
                        for i in range(10):
                            globals()[chr(1062 + i)].configure(state="disabled")
                        globals()["del"].configure(state="disabled")
                        inpt.configure(state="disabled", bg=bbg)
                        sl.focus_set()
                        sl.bind('<Escape>', back_slova)
                        global sl_t
                        sl_t = False
                        return
                except:None
                letter = word[-1]
                if letter in "ьЬъыЪЫ":
                    letter = word[-2]
                    if letter in "ьЬъыЪЫ":
                        letter = word[-3]
                        if letter in "ьЬъыЪЫ":
                            letter = word[-4]
                            if letter in "ьЬъыЪЫ":
                                letter = word[-5]
                sound_short_win.play()
                data['wins'] += 1
                data['multywins'] += 1
                data['sl_count1'] += 1
                cnt1 += 1
                cnt1_lbl.configure(text=f"СЧЕТ: {cnt1}")
                words.append(word)
                inpt.insert(0, letter)
                tr.destroy()
                tr = tk.Label(sl,bd=0,image=triu1)
                tr.place(x=749,y=75)
                slovo = tk.Label(sl,bg=bbg,text=f"({word})\nСЛОВО НА БУКВУ {letter}",font=("arial", 55, "bold"),justify="center")
                slovo.place(x=30,y=198)
                word = ""
                fir = True
                wrd.configure(text=word)
                inpt.bind("<Return>",player1)
            inpt_btn = tk.Button(sl,text="ОТПРАВИТЬ",bg=bbg,activebackground=abg,relief="flat",font=("arial", 40, "bold"),
                                 command=player2)
            inpt_btn.place(x=1014,y=785)

            def back_slova(g="g"):
                global multy_time
                multy_time = False
                global sl_t
                sl_t = False
                global BACK
                BACK = True
                sl.destroy()
                multy_menu()

            #создаем слово на мышке
            def create_word(letter):
                sound_keyboard.play()
                global word,first,wrd,cont,err1,erro
                if cont <= 10 and letter != "del":
                    cont += 1
                if letter != "del" and cont <= 10:
                    word = word + letter
                if letter == "del":
                    word = word[0:-1]
                    if cont >= 1:
                        cont -= 1
                if first:
                    wrd = tk.Label(sl, bg=bbg, text=word, font=("arial", 80, "bold"))
                else: wrd.configure(text=word)
                wrd.place(x=1200-round(len(word)*38.6),y=379)
                if not err1:
                    erro.destroy()
                    err1 = True
                if cont > 10:
                    err1 = False
                    erro = tk.Label(sl, text="КОЛИЧЕСТВО БУКВ ДОЛЖНО БЫТЬ МЕНЕЕ 11", bg=bbg, fg=red,
                                    font=("arial", 25, "bold"))
                    erro.place(x=818,y=750)
                    cont -= 1
                first = False

            back_btn_slova = tk.Button(sl, image=imag, bg=bagr, command=back_slova, activebackground=bagr,
                          relief="flat", width=60, height=50, ).place(x=20, y=10)
            #создвем кнопки с буквами
            for i in range(11):
                globals()[chr(1040 + i)] = tk.Button(sl, text=chr(1040 + i), bg=bbg, fg=tex,
                                                     font=("arial", 35, "bold"),
                                                     relief="flat", activebackground=abg,
                                                     command=lambda letter=f"{chr(1040 + i)}": create_word(letter))
                globals()[chr(1040 + i)].place(x=814 + i * 72, y=540, width=60, height=60)
            for i in range(11):
                globals()[chr(1051 + i)] = tk.Button(sl, text=chr(1051 + i), bg=bbg, fg=tex,
                                                      font=("arial", 35, "bold"), relief="flat",
                                                      activebackground=abg,
                                                      command=lambda letter=f"{chr(1051 + i)}": create_word(letter))
                globals()[chr(1051 + i)].place(x=814 + i * 72, y=610, width=60, height=60)
            for i in range(10):
                globals()[chr(1062 + i)] = tk.Button(sl, text=chr(1062 + i), bg=bbg, fg=tex,
                                                     font=("arial", 35, "bold"),
                                                     relief="flat", activebackground=abg,
                                                     command=lambda letter=f"{chr(1062 + i)}": create_word(letter))
                globals()[chr(1062 + i)].place(x=814 + i * 72, y=680, width=60, height=60)
            globals()["del"] = tk.Button(sl, bg=bbg, fg=tex,font=("arial", 35, "bold"),
                                        relief="flat", activebackground=bbg,command=lambda letter=f"del": create_word(letter),image=udl)
            globals()["del"].place(x=814 + 715, y=680, width=70, height=60)
            text_lbl = tk.Label(sl,pady=56,padx=388,bg=bbg).place(x=815,y=379)

            #делаем ввод с клавиатуры
            def on_change(*args):
                current_value = entry_var.get()
                entry_var.set(current_value.upper())
            err_lbl = tk.Label(sl, bg=bbg, fg=red, text="КОЛИЧЕСТВО БУКВ ДОЛЖНО БЫТЬ МЕНЕЕ 11",font=("arial", 25, "bold"))

            def validate_input(new_value):
                global err_lbl_1,err_lbl
                if len(new_value) > 10:
                    try:
                        err_lbl.place(x=11,y=520)
                    except:
                        err_lbl = tk.Label(sl,bg=bbg,fg=red,text="КОЛИЧЕСТВО БУКВ ДОЛЖНО БЫТЬ МЕНЕЕ 11",font=("arial", 25, "bold"))
                        err_lbl.place(x=11, y=520)
                    err_lbl_1 = True
                    return False
                if not all(char in "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя" for char in new_value):
                    return False
                else:
                    if err_lbl_1:
                        err_lbl.destroy()
                        err_lbl_1 = False
                    return True
            fake = tk.Label(sl,pady=56,padx=390,bg=bbg).place(x=5,y=379)
            vcmd = (sl.register(validate_input), '%P')
            entry_var = tk.StringVar()
            entry_var.trace_add("write", on_change)
            inpt = tk.Entry(sl,justify="center",font=("arial", 80, "bold"),width=13,bg=bbg,textvariable=entry_var,
                            validate='key', validatecommand=vcmd,bd=0)
            inpt.place(x=5,y=379)
            inpt.focus_set()
            inpt.bind('<Escape>',back_slova)

            def guide_rps():
                sound_keyboard.play()
                global gh3
                how_play.configure(text="СКРЫТЬ", command=cl_rps)
                how_play.place(x=810, y=847)
                gh3 = tk.Label(sl, bg=bbg,
                               text="КАК ИГРАТЬ В СЛОВА?\nСНАЧАЛА ИГРОК 1 ДОЛЖЕН ВВЕСТИ ЛЮБОЕ СЛОВО,\nЗАТЕМ ИГРОК 2 ДОЛЖЕН ВВЕСТИ СЛОВО, НАЧИНАЮЩЕЕСЯ НА ПОСЛЕДНЮЮ БУКВУ СЛОВА ИГРОКА 1(ЕСЛИ БУКВА НЕ Ь, Ъ, Ы)\n ПОСЛЕ ЧЕГО ИГРОК 1 ДОЛЖЕН ТОЖЕ САМОЕ.\nИГРА ИДЕТ ДО ТЕХ ПОР,\n ПОКА ОДИН ИЗ ИГРОКОВ НЕ ВВЕДЕТ ПОВТОРЯЮЩЕЕСЯ СЛОВО ИЛИ СЛОВО НЕ НА ПОСЛЕДНЮЮ БУКВУ ПРЕДЫДУЩЕГО."
                               , justify="center", font=("arial", 18, "bold"),pady=5)
                gh3.place(x=16, y=186)

            def cl_rps():
                sound_keyboard.play()
                global gh3
                gh3.destroy()
                how_play.configure(text="КАК ИГРАТЬ?", command=guide_rps)
                how_play.place(x=810, y=847)
            how_play = tk.Button(sl, text="КАК ИГРАТЬ?", bg=bbg, fg=tex, font=("arial", 17, "bold"), relief="flat",
                                 activebackground=abg, command=guide_rps)
            how_play.place(x=810, y=847)

            def stat_sl():
                sound_keyboard.play()

                def ba():
                    sound_keyboard.play()
                    ab.destroy()
                    stat.configure(command=stat_sl)

                def upd():
                    try:
                        yt.configure(text=f"ОБЩИЙ СЧЕТ: {data['sl_count1']+data['sl_count2']}")
                        u.configure(text=f"СЧЕТ: {data['sl_count1']}")
                        w.configure(text=f"СЧЕТ: {data['sl_count2']}")
                        t.configure(text=f"ВРЕМЯ В ИГРЕ: {time(data['sl_time'])}")
                        window.after(10, upd)
                    except:
                        return

                ab = tk.Frame(sl, bg=bbg, height=260, width=650)
                ab.place(x=940, y=100)
                tk.Label(ab, bg=bbg, text="СТАТИСТИКА", font=("arial", 35, "bold")).place(x=162, y=-2)
                a = tk.Label(ab, bg=bbg, text=f"КЛАВИАТУРА", font=("arial", 25, "bold")).place(x=0, y=51)
                b = tk.Label(ab, bg=bbg, text=f"МЫШЬ", font=("arial", 25, "bold")).place(x=340, y=51)
                w = tk.Label(ab, bg=bbg, text=f"СЧЕТ: {data['sl_count2']}", font=("arial", 25, "bold"))
                w.place(x=0, y=91)
                u = tk.Label(ab, bg=bbg, text=f"СЧЕТ: {data['sl_count1']}", font=("arial", 25, "bold"))
                u.place(x=340, y=91)
                u1 = tk.Label(ab, bg=bbg, text=f"СЫГРАНО: {data['sl_games']}", font=("arial", 25, "bold"))
                u1.place(x=210, y=135)
                yt = tk.Label(ab, bg=bbg, text=f"ОБЩИЙ СЧЕТ: {data['sl_count1']+data['sl_count2']}", font=("arial", 25, "bold"))
                yt.place(x=186, y=175)
                t = tk.Label(ab, bg=bbg, text=f"ВРЕМЯ В ИГРЕ: {time(data['sl_time'])}",font=("arial", 25, "bold"))
                t.place(x=80, y=215)
                window.after(10, upd)
                stat.configure(command=ba)
            stat = tk.Button(sl, image=stat_im, relief='flat', activebackground=bagr, width=85,
                             height=80, bg=bagr, command=stat_sl, compound='top', text='СТАТИСТИКА',
                             font=('arial', 10, 'bold'))
            stat.place(x=1500, y=5)

            sl.place(x=0,y=0)
        menu.destroy()
        multy = tk.Frame(window, bg=bagr,)
        pick = tk.Label(multy,text = "ВЫБЕРИТЕ ИГРУ", bg=bagr, fg=tex,font=("arial", 75, "bold"), anchor="n",padx = 200).pack()
        btn1 = tk.Button(multy, text="ВИСЕЛИЦА ДЛЯ 2", bg=bbg, fg=tex, font=("arial", 40, "bold"),
                         activebackground=abg, pady=7, relief="flat",command=vis2).pack(pady=10)
        btn2 = tk.Button(multy, text="СЛОВА", bg=bbg, fg=tex, font=("arial", 40, "bold"), relief="flat",padx = 141,
                         activebackground=abg, pady=7,command=slova).pack(pady=10)
        btn4 = tk.Button(multy,width=60,height=50,image = imag,relief = "flat",command=back,activebackground=bagr).place(x = 20, y = 20)
        multy.focus_set()
        multy.bind("<Escape>",back)
        multy.pack()


    menu = tk.Frame(window)
    menu["bg"] = bagr
    menutext = tk.Label(menu, bg=bagr, fg=tex, text="МЕНЮ", font=("arial", 100, "bold"), anchor="n",padx = 400,pady=45).pack()
    solo_btn = tk.Button(menu, text="ОДИНОЧНАЯ ИГРА", bg=bbg, fg=tex, font=("arial", 50, "bold"),pady= 10,
                         activebackground=abg, command=solo,padx = 22,relief = "flat").pack()
    multy_btn = tk.Button(menu, text="СОВМЕСТНАЯ ИГРА", bg=bbg, fg=tex, font=("arial", 50, "bold"),relief = "flat",
                          activebackground=abg, pady=10,command = multy_menu,).pack(pady=20, )
    exit = tk.Button(menu, text="ВЫХОД", bg=bbg, fg=tex, font=("arial", 47, "bold"),relief = "flat",activebackground=abg, pady=10,
                     command=exit).pack(pady=100)


    def ach_menu():
        global ach_f
        global ach

        def back(g=""):
            sound_back.play()
            ach_f.destroy()
            menu_1()

        def upd():
            try:
                if data["new"] != "True":
                    a = Achievement(data["timeCount"], "ПРОВЕСТИ В ИГРЕ", 27, 120, data["time_in_game"])
                    b = Achievement(data["openCount"], "ЗАЙТИ В ИГРУ", 427, 120, data["open_in_game"])
                    с = Achievement(data["gamesCount"], "ЗАЙТИ В ЛЮБУЮ ИГРУ", 827, 120, data["games_in_game"])
                    d = Achievement(data["visCount"], f"ОДЕРЖАТЬ {data["vis_wins_с"]} ПОБЕД", 27, 280, "В ВИСИЛИЦЕ")
                    i = Achievement(data["rpsCount"], f"ОДЕРЖАТЬ {data["rps_wins_с"]} ПОБЕД", 427, 280,"В КАМ., НОЖН., БУМ.")
                    f = Achievement(data["gnCount"], f"ОДЕРЖАТЬ {data["gn_wins_c"]} ПОБЕД", 827, 280, "В УГАДАЙ ЧИСЛО")
                    g = Achievement(data["memCount"], f"ДОСТИГНУТЬ КОМБО {data["mem_wins_c"]}", 227, 440, "В ПОВТОРИ ЗА МНОЙ")
                    k = Achievement(data["bingCount"], f"ДОСТИГНУТЬ СЧЕТА {data["bing_wins_c"]}", 627, 440, "В БИНГО")
                    l = Achievement(data["vis2Count"], f"ОДЕРЖАТЬ {data["vis2_wins_с"]}", 227, 600, "В ВИСИЛИЦЕ ДЛЯ 2")
                    max = Achievement("MAX max MAX", f"{data["maxt1"]}", 427, 760, f"{data["maxt2"]}")
                    data["new"] = "True"
                window.after(50,upd)
            except: return
        sound_keyboard.play()
        menu.destroy()
        ach_f = tk.Frame(window, bg=bagr, height=900, width=1200)
        f = tk.Button(ach_f, image=imag, bg=bagr, command=back, activebackground=bagr, relief='flat', width=60,height=50).place(x=20, y=20)
        tk.Label(ach_f,bg=bbg,text="ДОСТИЖЕНИЯ",font=('arial', 60, 'bold')).place(x=306,y=0)
        ach_f.pack()
        a = Achievement(data["timeCount"], "ПРОВЕСТИ В ИГРЕ", 27, 120, data["time_in_game"])
        b = Achievement(data["openCount"], "ЗАЙТИ В ИГРУ", 427, 120, data["open_in_game"])
        с = Achievement(data["gamesCount"], "ЗАЙТИ В ЛЮБУЮ ИГРУ", 827, 120, data["games_in_game"])
        d = Achievement(data["visCount"], f"ОДЕРЖАТЬ {data["vis_wins_с"]} ПОБЕД", 27, 280, "В ВИСИЛИЦЕ")
        i = Achievement(data["rpsCount"], f"ОДЕРЖАТЬ {data["rps_wins_с"]} ПОБЕД", 427, 280, "В КАМ., НОЖН., БУМ.")
        f = Achievement(data["gnCount"], f"ОДЕРЖАТЬ {data["gn_wins_c"]} ПОБЕД", 827, 280, "В УГАДАЙ ЧИСЛО")
        g = Achievement(data["memCount"], f"ДОСТИГНУТЬ КОМБО {data["mem_wins_c"]}", 227, 440, "В ПОВТОРИ ЗА МНОЙ")
        k = Achievement(data["bingCount"], f"ДОСТИГНУТЬ СЧЕТА {data["bing_wins_c"]}", 627, 440, "В БИНГО")
        l = Achievement(data["vis2Count"], f"ОДЕРЖАТЬ {data["vis2_wins_с"]}", 227, 600, "В ВИСИЛИЦЕ ДЛЯ 2")
        m = Achievement(data["slCount"], f"ДОСТИГНУТЬ СЧЕТА {data["sl_wins_c"]}", 627, 600, "В СЛОВАХ")
        max = Achievement("MAX max MAX", f"{data["maxt1"]}", 427, 760, f"{data["maxt2"]}")
        window.after(10,upd)
        ach_f.bind("<Escape>",back)
        ach_f.focus_set()
    achive_btn = tk.Button(menu, bg=bagr,activebackground=bagr, image=ach_im_1, width=85, height=80, relief='flat', compound='top', text='ДОСТИЖЕНИЯ', font=('arial', 10, 'bold'),command=ach_menu).place(x=1000, y=806)


    def st():
        sound_keyboard.play()
        a = tk.Frame(window, bg=bagr, height=900, width=1200)

        def upd():
            try:
                tti.configure(text=f"ВРЕМЯ В ИГРЕ: {time(data['time'])}")
                ttim.configure(text=f"МАКС. ВРЕМЯ В ИГРЕ: {time(data['longtime'])}")
                window.after(1000, upd)
            except:
                return

        def mmulty_games():
            a.destroy()
            mul = tk.Frame(window,bg=bagr,width=1200,height=900)

            def back1(g="g"):
                sound_back.play()
                mul.destroy()
                st()

            f = tk.Button(mul, image=imag, bg=bagr, command=back1, activebackground=bagr, relief='flat', width=60, height=50).place(x=20, y=20)
            tk.Label(mul, text='СТАТИСТИКА ПО ИГРАМ', font=('arial', 60, 'bold'), bg=bbg).place(x=108, y=0)
            tk.Label(mul, text='ВИСЕЛИЦА ДЛЯ 2', font=('arial', 40, 'bold'), bg=bbg).place(x=6, y=110)
            tk.Label(mul, text='СЛОВА', font=('arial', 40, 'bold'), bg=bbg,padx=141).place(x=717, y=110)

            ab6 = tk.Frame(mul, bg=bbg, height=250, width=478)
            ab6.place(x=6, y=175)
            tk.Label(ab6, bg=bbg, text=f"ЗАГАДАНО: {data['vis2_games']}", font=("arial", 25, "bold")).place(x=126, y=0)
            tk.Label(ab6, bg=bbg, text=f"ПОБЕД: {data['vis2_wins']}", font=("arial", 25, "bold")).place(x=158, y=42)
            tk.Label(ab6, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['vis2_lose']}", font=("arial", 25, "bold")).place(x=111, y=84)
            tk.Label(ab6, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['vis2_time'])}", font=("arial", 25, "bold")).place(x=108, y=126)
            lk6 = tk.Frame(ab6,bg=abg,width=479,height=3)
            lk6.place(x=-1, y=-1)


            ab7 = tk.Frame(mul, bg=bbg, height=250, width=477)
            ab7.place(x=717, y=175)
            tk.Label(ab7, bg=bbg, text=f"СЫГРАНО: {data['sl_games']}", font=("arial", 25, "bold")).place(x=124, y=0)
            tk.Label(ab7, bg=bbg, text=f"СЧЕТ(КЛАВИАТУРА): {data['sl_count2']}", font=("arial", 25, "bold")).place(x=50, y=42)
            tk.Label(ab7, bg=bbg, text=f"СЧЕТ(МЫШЬ): {data['sl_count1']}", font=("arial", 25, "bold")).place(x=101, y=84)
            tk.Label(ab7, bg=bbg, text=f"ОБЩИЙ СЧЕТ: {data['sl_count1'] + data['sl_count2']}",font=("arial", 25, "bold")).place(x=101, y=126)
            tk.Label(ab7, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['sl_time'])}", font=("arial", 25, "bold")).place(x=108, y=168)
            lk7 = tk.Frame(ab7,bg=abg,width=479,height=3)
            lk7.place(x=-1, y=-1)


            mul.focus_set()
            mul.bind("<Escape>",back1)
            mul.pack()


        def ssolo_games():
            a.destroy()
            sol = tk.Frame(window,bg=bagr,width=1200,height=900)

            def back(g="g"):
                sol.destroy()
                sound_back.play()
                st()

            f = tk.Button(sol, image=imag, bg=bagr, command=back, activebackground=bagr, relief='flat', width=60, height=50).place(x=20, y=20)
            tk.Label(sol, text='СТАТИСТИКА ПО ИГРАМ', font=('arial', 60, 'bold'), bg=bbg).place(x=108, y=0)
            tk.Label(sol, text='КАМЕНЬ,\nНОЖНИЦЫ,\nБУМАГА', font=('arial', 40, 'bold'), bg=bbg).place(x=444, y=110)
            tk.Label(sol, text='УГАДАЙ\nЧИСЛО', font=('arial', 40, 'bold'), bg=bbg,padx=48,pady=32).place(x=883, y=110)
            tk.Label(sol, text='БИНГО', font=('arial', 40, 'bold'), bg=bbg,padx=63).place(x=6, y=607)
            tk.Label(sol, text='ПОВТОРИ\nЗА МНОЙ', font=('arial', 40, 'bold'), bg=bbg,padx=23,pady=32).place(x=6, y=110)
            tk.Label(sol, text='ВИСЕЛИЦА', font=('arial', 40, 'bold'), bg=bbg,padx=5).place(x=660, y=607)

            ab1 = tk.Frame(sol, bg=bbg, height=220, width=535)
            ab1.place(x=660, y=675)
            tk.Label(ab1, bg=bbg, text=f"ПОПЫТОК: {data['alphs']}", font=("arial", 25, "bold")).place(x=1, y=0)
            tk.Label(ab1, bg=bbg, text=f"ПОБЕД: {data['vis_wins']}", font=("arial", 25, "bold")).place(x=1, y=84)
            tk.Label(ab1, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['vis_lose']}", font=("arial", 25, "bold")).place(x=1, y=126)
            tk.Label(ab1, bg=bbg, text=f"СЫГРАНО: {data['vis_games']}", font=("arial", 25, "bold")).place(x=1, y=42)
            tk.Label(ab1, bg=bbg, text=f"ВРЕМЯ В ИГРЕ: {time(data['vis_time'])}", font=("arial", 25, "bold")).place(x=1, y=168)
            tk.Label(ab1, bg=bbg, text=f"(МИНИМУМ: {data['vis_min']})", font=("arial", 25, "bold")).place(x=250, y=0)
            lk5 = tk.Frame(sol,bg=abg,width=314,height=2)
            lk5.place(x=660,y=673)

            ab2 = tk.Frame(sol, bg=bbg, height=220, width=535)
            ab2.place(x=6, y=675)
            tk.Label(ab2, bg=bbg, text=f"СЫГРАНО: {data["b_games"]}", font=("arial", 25, "bold")).place(x=0, y=42)
            tk.Label(ab2, bg=bbg, text=f"ОБЩИЙ СЧЕТ: {data['bing_count']}",font=("arial", 25, "bold")).place(x=0, y=0)
            tk.Label(ab2, bg=bbg, text=f"В ИГРЕ: {time(data['b_time'])}", font=("arial", 25, "bold")).place(x=0, y=84)
            lk5 = tk.Frame(sol,bg=abg,width=315,height=2)
            lk5.place(x=6,y=673)

            ab3 = tk.Frame(sol, bg=bbg, height=250, width=313)
            ab3.place(x=6, y=290)
            tk.Label(ab3, bg=bbg, text=f"СЫГРАНО: {data['mem_games']}", font=("arial", 25, "bold")).place(x=42, y=0)
            tk.Label(ab3, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['mem_time'])}", font=("arial", 25, "bold")).place(x=26, y=84)
            tk.Label(ab3, bg=bbg, text=f"МАКС. КОМБО: {data['mem_max']}", font=("arial", 25, "bold")).place(x=16, y=42)
            lk3 = tk.Frame(ab3,bg=abg,width=314,height=3)
            lk3.place(x=-1, y=-1)

            ab4 = tk.Frame(sol, bg=bbg, height=250, width=313)
            ab4.place(x=883, y=290)
            tk.Label(ab4, bg=bbg, text=f"ПОБЕД: {data['gn_wins']}", font=("arial", 25, "bold")).place(x=75, y=42)
            tk.Label(ab4, bg=bbg, text=f"СЫГРАНО: {data['gn_games']}", font=("arial", 25, "bold")).place(x=42, y=0)
            tk.Label(ab4, bg=bbg, text=f"ПОПЫТОК: {data['gn_try']}", font=("arial", 25, "bold")).place(x=42, y=84)
            tk.Label(ab4, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['gn_time'])}", font=("arial", 25, "bold")).place(x=26, y=168)
            tk.Label(ab4, bg=bbg, text=f"МИН. ПОПЫТОК: {data['gn_min']}", font=("arial", 25, "bold")).place(x=2, y=126)
            lk2 = tk.Frame(ab4,bg=abg,width=314,height=3)
            lk2.place(x=-1, y=-1)

            ab5 = tk.Frame(sol, bg=bbg, height=250, width=314)
            ab5.place(x=444, y=290)
            tk.Label(ab5, bg=bbg, text=f"ВРЕМЯ В ИГРЕ:\n{time(data['rps_time'])}", font=("arial", 25, "bold")).place(x=26, y=168)
            tk.Label(ab5, bg=bbg, text=f"СЫГРАНО: {data['rps_games']}", font=("arial", 25, "bold")).place(x=42, y=0)
            tk.Label(ab5, bg=bbg, text=f"ПОБЕД: {data['rps_wins']}", font=("arial", 25, "bold")).place(x=75, y=42)
            tk.Label(ab5, bg=bbg, text=f"ПОРАЖЕНИЙ: {data['rps_loses']}", font=("arial", 25, "bold")).place(x=14, y=84)
            if data["rps_games"] == 0:
                tk.Label(ab5, bg=bbg, text=f"% ПОБЕД: {data["rps_wins"]*100//(data["rps_games"]+1)}", font=("arial", 25, "bold")).place(x=42, y=126)
            else:
                tk.Label(ab5, bg=bbg, text=f"% ПОБЕД: {data["rps_wins"] * 100 // (data["rps_games"])}",font=("arial", 25, "bold")).place(x=42, y=126)
            lk1 = tk.Frame(ab5,bg=abg,width=315,height=3)
            lk1.place(x=-1, y=-1)

            sol.focus_set()
            sol.bind("<Escape>",back)
            sol.pack()


        def fgh(g=""):
            sound_back.play()
            a.destroy()
            menu_1()


        f = tk.Button(a, image=imag, bg=bagr, command=fgh, activebackground=bagr, relief='flat', width=60, height=50).place(x=20, y=20)
        a.bind('<Escape>', fgh)
        a.focus_set()
        menu.destroy()
        tk.Label(a, text='СТАТИСТИКА', font=('arial', 70, 'bold'), bg=bbg).place(x=286, y=0)
        tk.Label(a, bg=bbg, pady=128, padx=350).place(x=248, y=120)
        tk.Label(a, text='ОБЩАЯ', font=('arial', 50, 'bold'), bg=bbg).place(x=468, y=120)
        tk.Label(a, text=f"СЫГРАНО: {data['games']}", font=('arial', 25, 'bold'), bg=bbg).place(x=248, y=250)
        tk.Label(a, text=f"ЗАПУСКОВ: {data['opens']}", font=('arial', 25, 'bold'), bg=bbg).place(x=248, y=200)
        tk.Label(a, text=f"ПОБЕД: {data['wins']}", font=('arial', 25, 'bold'), bg=bbg).place(x=600, y=200)
        tk.Label(a, text=f"ПОРАЖЕНИЙ: {data['loses']}", font=('arial', 25, 'bold'), bg=bbg).place(x=600, y=250)
        tti = tk.Label(a, text=f"ВРЕМЯ В ИГРЕ: {time(data['time'])}", font=('arial', 25, 'bold'), bg=bbg)
        tti.place(x=248, y=300)
        ttim = tk.Label(a, text=f"МАКС. ВРЕМЯ В ИГРЕ: {time(data['longtime'])}", font=('arial', 25, 'bold'), bg=bbg)
        ttim.place(x=248, y=350)
        window.after(1000, upd)
        tk.Label(a, bg=bbg, pady=228, padx=250).place(x=60, y=420)
        tk.Label(a, bg=bbg, pady=228, padx=250).place(x=636, y=420)
        tk.Label(a, text='ОДИНОЧНАЯ', font=('arial', 50, 'bold'), bg=bbg).place(x=90, y=420)
        tk.Label(a, text='СОВМЕСТНАЯ', font=('arial', 50, 'bold'), bg=bbg).place(x=645, y=420)
        tk.Label(a, text=f"СЫГРАНО ОДИНОЧНО: {data['sologames']}", font=('arial', 25, 'bold'), bg=bbg).place(x=60, y=500)
        tk.Label(a, text=f"СЫГРАНО СОВМЕСТНО: {data['multygames']}", font=('arial', 25, 'bold'), bg=bbg).place(x=636, y=500)
        tk.Label(a, text=f"ВРЕМЯ: {time(data['solotime'])}", font=('arial', 25, 'bold'), bg=bbg).place(x=60, y=550)
        tk.Label(a, text=f"ВРЕМЯ: {time(data['multytime'])}", font=('arial', 25, 'bold'), bg=bbg).place(x=636, y=550)
        tk.Label(a, text=f"ПОБЕД: {data['solowins']}", font=('arial', 25, 'bold'), bg=bbg).place(x=60, y=600)
        tk.Label(a, text=f"ПОРАЖЕНИЙ: {data['sololoses']}", font=('arial', 25, 'bold'), bg=bbg).place(x=60, y=650)
        tk.Label(a, text=f"ПОБЕД: {data['multywins']}", font=('arial', 25, 'bold'), bg=bbg).place(x=636, y=600)
        tk.Label(a, text=f"ПОРАЖЕНИЙ: {data['multyloses']}", font=('arial', 25, 'bold'), bg=bbg).place(x=636, y=650)
        tk.Button(a, text = "ПО ИГРАМ",font=("Arial", 50, "italic"),bg=bbg,activebackground=abg,command=ssolo_games).place(x=108, y=750)
        tk.Button(a, text = "ПО ИГРАМ", font=("Arial", 50, "italic"), bg=bbg, activebackground=abg,command=mmulty_games).place(x=684, y=750)
        a.pack()
    main_stat = tk.Button(menu, image=stat_im, relief='flat', activebackground=bagr, width=85, height=80, bg=bagr, command=st, compound='top', text='СТАТИСТИКА', font=('arial', 10, 'bold')).place(x=1100, y=807)


    def set_v(n=1.0):
        mixer.music.set_volume(0.1 * n)
        sound_ach.set_volume(0.3 * n)
        mixer.music.unpause()
        sound_win.set_volume(0.25 * n)
        sound_keyboard.set_volume(1 * n)
        sound_short_win.set_volume(0.1 * n)
        sound_back.set_volume(0.2 * n)
        sound_play.set_volume(0.4 * n)
        sound_menu.set_volume(0.15 * n)
        sound_mem.set_volume(0.35 * n)
        sound_ach.set_volume(0.2 * n)
        sound_mem1.set_volume(1 * n)
        sound_lose.set_volume(0.35 * n)


    def on(n="f"):
        global volume,xx
        volume_scale.set(xx)
        data['music'] = 'True'
        music.configure(image=image1, command=off)
        volume = True

    def off():
        global volume
        volume_scale.set(0)
        data['music'] = 'False'
        sound_ach.set_volume(0)
        mixer.music.pause()
        sound_win.set_volume(0)
        sound_keyboard.set_volume(0)
        sound_short_win.set_volume(0)
        sound_back.set_volume(0)
        sound_play.set_volume(0)
        sound_menu.set_volume(0)
        sound_mem.set_volume(0)
        sound_ach.set_volume(0)
        sound_mem1.set_volume(0)
        sound_lose.set_volume(0)
        music.configure(image=image2, command=on)
        volume = False
    if volume:
        music = tk.Button(menu, width=105, height=80, image=image1, relief='flat', bg=bagr, activebackground=bagr, command=off, compound='top', text='fnonose - blessed', font=('arial', 10, 'bold'))
    else: music = tk.Button(menu, width=105, height=80, image=image2, relief='flat', bg=bagr, activebackground=bagr, command=off, compound='top', text='fnonose - blessed', font=('arial', 10, 'bold'))
    music.place(x=15, y=806)
    def ggg(x):
        global xx
        if x == '0':
            off()
            return
        else: on()
        xx = int(x)
        set_v(int(x)/4)
    volume_scale = tk.Scale(menu, from_=0, to=10, orient='horizontal', command=ggg, bg=bagr, bd=1, length=110, highlightthickness=0, relief='flat', sliderrelief='flat')
    volume_scale.place(x=15, y=760)
    volume_scale.set(xx)
    if data['music'] == 'True':
        on()
    else: off()
    menu.pack()





menu_1()
window.mainloop()
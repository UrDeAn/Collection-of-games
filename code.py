import tkinter as tk
from pygame import mixer
from PIL import ImageTk
import random

#цвета
abg = "#396c7c"
bagr = "#71a4bb"
tex = "#111114"
bbg = "#abc2d1"
red = "#900020"
green = "#00693E"

#настройка основного окна
window = tk.Tk()
window.geometry("1200x900+350+50")
window.title("Сборник игр")
window.minsize(1200, 900)
window.iconbitmap(r'pictures\gamepad.ico')
window["bg"] = bagr

#загружаем картинки
imag = ImageTk.PhotoImage(file=r"pictures\стрелка.png")
image1 = ImageTk.PhotoImage(file=r"pictures\zzz.png")
image2 = ImageTk.PhotoImage(file=r"pictures\zz.png")
image3 = ImageTk.PhotoImage(file=r"pictures\info.png")
vic_image1=ImageTk.PhotoImage(file=r"pictures\виселица1.png")
vic_image2=ImageTk.PhotoImage(file=r"pictures\виселица2.png")
vic_image3=ImageTk.PhotoImage(file=r"pictures\виселица3.png")
vic_image4=ImageTk.PhotoImage(file=r"pictures\виселица4.png")
vic_image5=ImageTk.PhotoImage(file=r"pictures\виселица5.png")
vic_image6=ImageTk.PhotoImage(file=r"pictures\виселица6.png")
vic_image7=ImageTk.PhotoImage(file=r"pictures\виселица7.png")
vic_image8=ImageTk.PhotoImage(file=r"pictures\виселица8.png")
vic_image9=ImageTk.PhotoImage(file=r"pictures\виселица9.png")
vic_image10=ImageTk.PhotoImage(file=r"pictures\виселица10.png")
stone_image = ImageTk.PhotoImage(file =r"pictures\камень.png")
scissors_image = ImageTk.PhotoImage(file =r"pictures\ножницы.png")
paper_image = ImageTk.PhotoImage(file =r"pictures\бумага.png")
inp = ImageTk.PhotoImage(file=r"pictures\inpt.png")
del_png = ImageTk.PhotoImage(file=r"pictures\удалить.png")
tri = ImageTk.PhotoImage(file=r"pictures\треугольник.png")
qwad = ImageTk.PhotoImage(file=r"pictures\квадрат.png")
cir = ImageTk.PhotoImage(file=r"pictures\круг.png")
romb = ImageTk.PhotoImage(file=r"pictures\ромб.png")
galk = ImageTk.PhotoImage(file=r"pictures\ыыы.png")
az = ImageTk.PhotoImage(file=r"pictures\az.png")
stp = ImageTk.PhotoImage(file=r"pictures\стоп.png")
pla = ImageTk.PhotoImage(file=r"pictures\играть.png")
lev = ImageTk.PhotoImage(file=r"pictures\лево.png")
prav = ImageTk.PhotoImage(file=r"pictures\право.png")

#музыка с помощью pygame
mixer.init()
mixer.music.load(r'music\Музыка.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.0)

sound1 = mixer.Sound(r"music\нажатие кнопки.wav")
sound1.set_volume(1)


def menu_1(): #основная функция
    def exit(): #функция выхода из игры
        sound1.play()
        window.destroy()

    def solo(): #функция выбора одиночной игры
        sound1.play()
        def back(): #функция возврата в меню
            sound1.play()
            solo_menu.destroy()
            menu_1()

        def visilica(): # игра виселица
            sound1.play()
            words = ["аллея", "маска", "автор", "агент", "актер", "акула", "спорт", "алмаз", "ангар", "ангел", "анонс",
                     "бидон", "бетон", "берег", "белок", "белка", "бекон", "бедро", "бегун", "башня", "батон", "батут",
                     "басня", "барин", "баржа", "баран", "барак", "банка", "банан", "балка", "балет", "багет", "багаж",
                     "бабка", "афиша", "атлет", "атлас", "атака", "буран", "булка", "букет", "буква", "будни", "бугор",
                     "брюхо", "брошь", "броня", "бровь", "гонка", "шорты", "голос", "голод", "глушь", "культ", "табак",
                     "гамак", "линза", "ветер", "огонь", "шишка", "малыш", "ветка", "финал", "дрель", "трель", "свист",
                     "ворон", "пульс", "дятел", "дуэль", "изгой", "игрок", "колея", "колба", "кокон", "козел", "морда",
                     "хорда", "ковер", "кобра", "книга", "клоун", "класс", "макет", "мазут", "магма", "магия", "лямка",
                     "лыжня", "лопух", "ложка", "монах", "моляр", "молот", "мозги", "мишка", "мираж", "минус", "мидия",
                     "мечта", "метод", "опрос", "опора", "опера", "опека", "сырье", "сыщик", "сцена", "сфера", "схема",
                     # 110
                     "авария", "азбука", "азимут", "аккорд", "акцент", "алтарь", "альбом", "амулет", "аналог", "ангина",
                     "бензин", "белуга", "бездна", "беглец", "барьер", "баобаб", "банкир", "банкет", "бампер", "балкон",
                     "ведьма", "вахтер", "варвар", "ванная", "ваниль", "вампир", "валюта", "вакуум", "бюджет", "власть",
                     "глагол", "гитара", "гигант", "гвоздь", "гарпун", "гамбит", "галлон", "газета", "гадюка", "двойка",
                     "датчик", "данный", "журнал", "житель", "жертва", "жемчуг", "желудь", "желтый", "жасмин", "каблук",
                     "йогурт", "истина", "ирония", "индекс", "клевер", "кирпич", "кинжал", "кетчуп", "каштан", "каучук",
                     "колоша", "колпак", "логово", "ловкач", "лифтер", "листок", "медуза", "медаль", "мебель", "машина",
                     "матрас", "матрос", "мнение", "обивка", "остров", "основа", "ошибка", "пекарь", "пейзаж", "певица",
                     "пробка", "пробел", "пробег", "причал", "прицеп", "прицел", "резина", "резерв", "реестр", "регион",
                     "седина", "сговор", "сделка", "уговор", "футбол", "шантаж", "штанга", "штатив", "штекер", "штопор",
                     "анкета", "береза", "вектор", "паштет", "письмо", "поддон", "подвох", "подвиг", "подвал",
                     "подача"]
            def set_diff_visilica(): # выбор сложности
                def back_1():
                    diff_menu.destroy()
                    solo()

                def diff(difficul):
                    sound1.play()
                    global game_vis
                    game_vis = tk.Frame(window, width=1200, height=900)
                    game_vis["bg"] = bagr
                    global count
                    diff_menu.destroy()
                    if difficul == 1:
                        count = 10
                    elif difficul == 2:
                        count = 8
                        vic2 = tk.Label(game_vis,image=vic_image2, bg=bagr)
                        vic2.place(x=400, y=100)
                    elif difficul == 3:
                        count = 6
                        vic4 = tk.Label(game_vis,image=vic_image4, bg=bagr)
                        vic4.place(x=400, y=100)
                    play()
                solo_menu.destroy()
                diff_menu = tk.Frame(window, width=1200, height=900)
                diff_menu["bg"] = bagr
                diffpick = tk.Label(diff_menu, text="ВЫБЕРИТЕ СЛОЖНОСТЬ", bg=bagr, fg=tex, font=("arial", 65, "bold"),
                                    anchor="n", ).pack(pady=20)
                diff1 = tk.Button(diff_menu, text="ЛЕГКАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, command=lambda difficult=1: diff(difficult), padx=55)
                diff1.pack(pady=15)
                diff2 = tk.Button(diff_menu, text="СРЕДНЯЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, padx=27, command=lambda difficult=2: diff(difficult))
                diff2.pack(pady=15)
                diff3 = tk.Button(diff_menu, text="СЛОЖНАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                                  activebackground=abg, padx=19, command=lambda difficult=3: diff(difficult))
                diff3.pack(pady=15)
                ex = tk.Button(diff_menu, text="НАЗАД", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                               activebackground=abg, padx=27, command=back_1)
                ex.pack(pady=90)
                diff_menu.pack()
                def play():
                    diff_menu.destroy()
                    global game_vis
                    def back_vic():
                        game_vis.destroy()
                        solo()

                    back_vic_button_1 = tk.Button(game_vis, image=imag, command=back_vic, relief="flat",
                                                  activebackground=bagr,width=60,height=50, bg=bagr,
                                                  ).place(x=20, y=20)
                    global guessed, correct, word,attempts
                    guessed = []
                    correct = []
                    word = random.choice(words).upper()
                    attempts = (tk.Label(game_vis, text=f"Осталось попыток: {count}!", bg=bagr, fg=tex,
                                         font=("arial", 30, "bold")))
                    attempts.place(x=372, y=10)

                    def check(letter):
                        sound1.play()
                        global count
                        def end():
                            def again():
                                sound1.play()
                                game_vis.destroy()
                                visilica()
                            again_button_2 = tk.Button(game_vis, text="ЗАНОВО", command=again, relief="flat",
                                                     activebackground=abg, font=("arial", 45, "bold"), bg=bbg).place(x=192,y=690)
                            back_vic_button_2 = tk.Button(game_vis, text="НАЗАД", command=back_vic, relief="flat",
                                                        activebackground=abg, font=("arial", 45, "bold"), bg=bbg,
                                                        padx=29).place(x=692, y=690)
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
                            global count
                            count -= 1
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
                            attempts.configure(text=f"Вы отгадали слово {word}!",)
                            if len(word) == 5:
                                attempts.place(x=310, y=10)
                            if len(word) == 6:
                                attempts.place(x=300, y=10)
                            end()
                        elif count == 0:
                            attempts.configure(text=f"Вы не отгадали слово {word}!")
                            if len(word) == 5:
                                attempts.place(x=295, y=10)
                            if len(word) == 6:
                                attempts.place(x=286, y=10)
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
                        if len(word) == 6:
                            globals()["lab" + str(i)] = (
                                tk.Label(game_vis, text="  ", bg=bbg, fg=tex, font=("arial", 70, "bold"), padx=29, ))
                            globals()["lab" + str(i)].place(x=243 + i * 120, y=455, width=110, height=110)
                        elif len(word) == 5:
                            globals()["lab" + str(i)] = (
                                tk.Label(game_vis, text="  ", bg=bbg, fg=tex, font=("arial", 70, "bold"), padx=29, ))
                            globals()["lab" + str(i)].place(x=303 + i * 120, y=455, width=110, height=110)
                    game_vis.pack()
            set_diff_visilica()

        def RockPaperScissors():
            sound1.play() # игра камень, ножницы, бумага
            global count_rps, wins, loses, draws
            solo_menu.destroy()
            def back_RPS():
                rps.destroy()
                solo()
            def play_2(player_move):
                sound1.play()
                global count_rps, wins, loses, draws
                count_rps += 1
                count_rps_lbl.configure(text=f"СЫГРАНО: {count_rps}")
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
                    wins += 1
                    lose_or_win.configure(fg="#00693E",text="ПОБЕДА")
                    lose_or_win.place(x=405, y=12)
                    win_lbl.configure(text=f"ПОБЕД: {wins}")
                elif bot_move == 3 and player_move == 1 or bot_move == 1 and player_move == 2 or bot_move == 2 and player_move == 3:
                    loses += 1
                    lose_or_win.configure(fg="#900020", text="ПОРАЖЕНИЕ")
                    lose_or_win.place(x=315, y=12)
                    lose_lbl.configure(text=f"ПОРАЖЕНИЙ: {loses}")
                elif bot_move == 3 and player_move == 3 or bot_move == 1 and player_move == 1 or bot_move == 2 and player_move == 2:
                    draws += 1
                    lose_or_win.configure(fg="#B5B8B1", text="НИЧЬЯ")
                    lose_or_win.place(x=440, y=12)
                    draw_lbl.configure(text=f"НИЧЬИХ: {draws}")
                win_rate_lbl.configure(text=f"ПРОЦЕНТ ПОБЕД: {round(wins / (count_rps) * 100)}%")

            rps = tk.Frame(window, width=1200, height=900)
            rps["bg"] = bagr
            count_rps = 0
            wins = 0
            loses = 0
            draws = 0
            draw_lbl = tk.Label(rps,text=f"НИЧЬИХ: {draws}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
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
            count_rps_lbl = tk.Label(rps,text=f"СЫГРАНО: {count_rps}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            count_rps_lbl.place(x=513,y=370)
            win_lbl = tk.Label(rps,text=f"ПОБЕД: {wins}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            win_lbl.place(x=405,y=405)
            lose_lbl = tk.Label(rps,text=f"ПОРАЖЕНИЙ: {loses}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
            lose_lbl.place(x=585,y=405)
            win_rate_lbl = tk.Label(rps,text=f"ПРОЦЕНТ ПОБЕД: {wins//(count_rps+1)}",font=("arial", 20, "bold"),bg=bagr,fg=tex)
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
            rps.pack()

        def guess_number():
            def again_gn():
                gn.destroy()
                guess_number()
            def back_1():
                sound1.play()
                diff_menu.destroy()
                solo()

            def diff(difficul):
                sound1.play()
                global gn,max_num
                gn = tk.Frame(window, width=1200, height=900)
                gn["bg"] = bagr
                diff_menu.destroy()
                if difficul == 1:
                    max_num = 100
                elif difficul == 2:
                    max_num = 1000
                elif difficul == 3:
                    max_num = 10000
                play_2(max_num)

            solo_menu.destroy()
            diff_menu = tk.Frame(window, width=1200, height=900)
            diff_menu["bg"] = bagr
            diffpick = tk.Label(diff_menu, text="ВЫБЕРИТЕ СЛОЖНОСТЬ", bg=bagr, fg=tex, font=("arial", 65, "bold"),
                                anchor="n", ).pack(pady=20)
            diff1 = tk.Button(diff_menu, text="ЛЕГКАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, command=lambda difficult=1: diff(difficult), padx=55)
            diff1.pack(pady=15)
            diff2 = tk.Button(diff_menu, text="СРЕДНЯЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, padx=27, command=lambda difficult=2: diff(difficult))
            diff2.pack(pady=15)
            diff3 = tk.Button(diff_menu, text="СЛОЖНАЯ", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                              activebackground=abg, padx=19, command=lambda difficult=3: diff(difficult))
            diff3.pack(pady=15)
            ex = tk.Button(diff_menu, text="НАЗАД", bg=bbg, fg=tex, font=("arial", 45, "bold"), relief="flat",
                           activebackground=abg, padx=27, command=back_1)
            ex.pack(pady=90)
            diff_menu.pack()

            def play_2(max_num):
                def back_gn():
                    gn.destroy()
                    solo()
                global one, count, numbr, numb, min_numb,guess_num,min_num,first
                guess_num = random.randint(1, max_num-1)
                one = True
                first = True
                count = 0
                numbr = " "
                numb = 0
                min_num = 0
                diff_menu.destroy()

                def inpt(number):
                    global one,numb,input_menu_2,numbr,count
                    if number == " ":
                        return
                    if number == "del" and count != 0:
                        input_menu_2.destroy()
                        error_lbl.configure(text="")
                        count -= 1
                        numbr = numbr[0:-1]
                        input_menu_2 = tk.Label(text=numbr, font=("arial", 100, "bold"), bg=bbg, fg=tex)
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
                        input_menu_2 = tk.Label(text=numbr, font=("arial", 100, "bold"), bg=bbg, fg=tex)
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
                gn.pack()


        def memory():
            def menu_mem():
                global truecombo, ccc
                truecombo = ""
                ccc = 0
                for i in range(3):
                    a = random.randint(1, 9)
                    truecombo = truecombo + str(a)
                def play_3(first = True,):
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
                        f.configure(state="disabled")
                        a.place(x=125, y=120)
                        for i in range(9):
                            globals()["ll" + str(i + 1)].configure(command="")
                        if www < len(truecombo):
                            globals()["ll" + str(truecombo[www])].config(bg="yellow")
                            if int(truecombo[www]) > 4:
                                window.after(400, lambda: globals()["ll" + str(truecombo[www])].config(bg=bbg))
                            else:
                                window.after(400, lambda: globals()["ll" + str(truecombo[www])].config(bg=bagr))
                            window.after(700-ccc*10, lambda: show_combo(www + 1))
                        else:
                            a.configure(text="ПОВТОРИТЕ КОМБИНАЦИЮ")
                            f.configure(state="active")
                            for i in range (9):
                                globals()[f"ll{(i + 1)}"].configure(command=lambda x = i+1: check_mem(x))
                    ccc += 1
                    combo = ""
                    cnt = 0
                    def check_mem(x):
                        global combo, cnt, truecombo, ccc, a
                        combo = combo + str(x)
                        if combo[cnt] != truecombo[cnt]:
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
                            cnt += 1
                            if combo == truecombo:
                                truecombo += str(random.randint(1, 9))
                                play_3(False)
                    def back_play_3():
                        pl3.destroy()
                        menu_mem()
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
                    print(truecombo)
                    show_combo()


                solo_menu.destroy()
                mem = tk.Frame(window, width=1200, height=900)
                mem["bg"] = bagr
                def back_memory():
                    mem.destroy()
                    solo()
                tk.Label(mem,text="ПОВТОРИ ЗА МНОЙ",bg=bagr,font=("Arial", 60, "bold")).place(x=200,y=10)
                tk.Button(mem, image=imag, bg=bagr, command=back_memory, activebackground=bagr,
                                        relief="flat", width=60, height=50,).place(x=20,y=20)
                tk.Button(mem,text="ИГРАТЬ",font=("Arial",60,"bold"),bg=bbg,activebackground=abg,command=play_3,
                        relief="flat").place(x=404,y=700)
                t = tk.Label(mem,image = tri,bg=bagr).place(x=32,y=130)
                q = tk.Label(mem, image=qwad, bg=bagr).place(x=314, y=130)
                c = tk.Label(mem, image=cir, bg=bagr).place(x=614, y=130)
                r = tk.Label(mem, image=romb, bg=bagr).place(x=914, y=130)
                for i in range (5):
                    globals()["lbl" + str(i)] = tk.Label(mem,fg=tex,bg=bbg,padx=101,pady=90)
                    globals()["lbl" + str(i)].place(x=58+i*220,y=450)
                    globals()["lblal" + str(i)] = tk.Label(mem, fg=tex, bg=bbg,text = i + 1,font=("arial", 70, "bold"))
                    globals()["lblal" + str(i)].place(x=132 + i * 220, y=492)
                mem.pack()
            menu_mem()
        def bingo():
            def play_5():
                from random import sample,shuffle
                global end, ij, afg, stop, lbl, gs, count,zx,zxc,flf
                gs = []
                zxc = []
                zx = []
                afg = [i for i in range(1,76)]
                shuffle(afg)
                stop = False
                ij = 0
                count= 0
                end = False
                kl = tk.Frame(window, width=1200, height=900, bg=bagr)
                tr = []
                lbl = tk.Label(kl,font=("Arial", 80, "bold"),bg=bagr)
                lbl.place(x=525,y=10)
                def plaz():
                    global stop
                    stop = False
                    flf.configure(image=stp, command=step)
                    update_label()
                def step():
                    global stop, ds
                    if ds:
                        window.after_cancel(ds)
                    stop = True
                    flf.configure(image=pla,command=plaz)
                flf = tk.Button(kl,bg=bbg,image=stp,relief="flat",command=step)
                flf.place(x=1050,y=772)
                def back_play_76():
                    global stop
                    stop = True
                    kl.destroy()
                    bingo()
                f = (tk.Button(kl, image=imag, bg=bagr, command=back_play_76, activebackground=bagr,
                               relief="flat", width=60, height=50,)).place(x=20, y=20)
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
                        global stop,lbl,gs,zx,count,flf
                        lbl.destroy()
                        flf.configure(state="disabled")
                        stop = True
                        dd = tk.Label(text="ПРОИГРЫШЬ",font=("Arial", 70, "bold"),bg=bagr,fg=red)
                        labl.destroy()
                        bttn.destroy()
                        bttn2.destroy()
                        k.destroy()
                        for i in range(5):
                            for j in range(5):
                                globals()[f"btn{i}{j}"].configure(command="")
                        for i in zxc:
                            if i in tr and not i in gs:
                                if count != 12:
                                    globals()[f"btn{zx[count]}"].configure(bg="yellow")
                            if i not in tr:
                                if count != 12:
                                    globals()[f"btn{zx[count]}"].configure(bg=red)
                            count += 1
                        if set(zxc).issubset(tr):
                            dd.configure(text="ПОБЕДА",fg=green)
                            dd.place(x=400,y=10)
                        else:
                            dd.place(x=280,y=10)

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
                    global ij, stop, lbl, ds
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
                        lbl.place(x=10,y=15)
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
            def back_play_5():
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
                         activebackground=abg, pady=7, command=bingo).pack(pady=15)
        tk.Button(solo_menu,width=60,height=50,image = imag,relief = "flat",command=back,activebackground=bagr).place(x=20, y=20)
        solo_menu.pack()


    def multy_menu(): #функция выбора совместной игры
        sound1.play()

        def back(): #фунця возврата в меню
            sound1.play()
            multy.destroy()
            menu_1()

        def vis2():
            global word,w,fi,te,coun,gh,er,fgh,vi,count,fd
            coun = 0
            vi = tk.Frame(window, bg=bagr, height=900, width=1200)
            word = ""
            fi = True
            count = 10
            gh =  False
            fgh = False
            def plus():
                global count,fd
                if count != 15:
                    count += 1
                    fd.configure(text=f"ПОПЫТОК:     {count}")
                    if count >= 10:
                        pl.place(x=736)
            def min():
                global count,fd
                if count != 1:
                    count -= 1
                    fd.configure(text = f"ПОПЫТОК:     {count}")
                    if count < 10:
                        pl.place(x=712)
            def yy():
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
                def back_vic2():
                    game_vis.destroy()
                    vis2()
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
                    sound1.play()
                    global count
                    def end():
                        def again():
                            sound1.play()
                            game_vis.destroy()
                            vis2()
                        again_button_2 = tk.Button(game_vis, text="ЗАНОВО", command=again, relief="flat",
                                                     activebackground=abg, font=("arial", 45, "bold"), bg=bbg).place(x=192,y=690)
                        back_vic_button_2 = tk.Button(game_vis, text="НАЗАД", command=back_vic2, relief="flat",
                                                        activebackground=abg, font=("arial", 45, "bold"), bg=bbg,
                                                        padx=29).place(x=692, y=690)
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
                        global count
                        count -= 1
                        globals()[letter].config(bg="#900020",state="disabled")
                        attempts.configure(text=f"Осталось попыток: {count}!")
                        df()
                    if set(correct) == set(word):
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
                game_vis.pack()
            def slo():
                def d():
                    dsa.destroy()
                    y.destroy()
                    n.destroy()
                    for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЬЫЪЭЮЧШЩЯ":
                        globals()[i].configure(state="normal")
                dsa = tk.Label(vi,bg=bagr,text=f"ЗАГАДАТЬ СЛОВО: '{word}'?",font=("Arial", 50, "bold"))
                y = tk.Button(vi,text="ДА",font=("Arial", 50, "bold"),bg=green,relief="flat",padx=22,activebackground=green,command = yy)
                n = tk.Button(vi,text="НЕТ",font=("Arial", 50, "bold"),bg=red, command = d,relief="flat",activebackground=red)
                dsa.place(x=250-25*len(word),y=170)
                y.place(x=250-25*len(word),y=270)
                n.place(x=730+25*len(word),y=270)
                for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЬЫЪЭЮЧШЩЯ":
                    globals()[i].configure(state="disabled")
            def wrd(x):
                global word,fi,te,coun,gh,er,fgh,dd,fd
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
            def back_vis2():
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
                                                     command=lambda letter=f"{chr(1040 + i)}",: wrd(letter))
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
            vi.pack()
        def vik():
            global count,vopry,otvy,bac
            bac = False
            count = 1
            vopry = []
            otvy = []
            def vopr():
                global count,vopry,otvy,f,ff,bac
                f = False
                ff = False
                def sohr():
                    global f,ff,er,err,bac
                    if len(rel_vopr.get("1.0", "end").replace('\n', '')) != 0 and len(rel_otv.get("0.0", "end").replace('\n', '')) != 0:
                        if len(vopry) != count-1:
                            del vopry[count-1]
                        if len(otvy) != count-1:
                            del otvy[count-1]
                        vopry.append(rel_vopr.get("1.0", "end").replace('\n', ''))
                        otvy.append(rel_otv.get("1.0", "end").replace('\n', ''))
                        if f:
                            er.destroy()
                        if ff:
                            err.destroy()
                    if len(rel_vopr.get("1.0", "end").replace('\n', '')) == 0:
                        er = tk.Label(vk,text="ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО",bg = bagr,fg=red,font=("Arial",15,"bold"))
                        er.place(x=420,y=276)
                        f = True
                    if len(rel_otv.get("1.0", "end").replace('\n', '')) == 0:
                        err = tk.Label(vk,text="ПОЛЕ ДОЛЖНО БЫТЬ ЗАПОЛНЕНО",bg = bagr,fg=red,font=("Arial",15,"bold"))
                        err.place(x=420,y=525)
                        ff = True
                    print(vopry,otvy)
                multy.destroy()
                def cou(с=None):
                    slo.configure(text=f"{len(rel_vopr.get("1.0", "end").replace('\n', ''))}/475")
                def k(с=None):
                    df.configure(text=f"{len(rel_otv.get("1.0", "end").replace('\n', ''))}/80")
                vk = tk.Frame(window, bg=bagr, height=900, width=1200)
                vpr = tk.Label(vk,text=f"ВОПРОС №{count}:",bg=bagr,font=("Arial",40,"bold")).place(x=422,y=10)
                otv = tk.Label(vk,text=f"ОТВЕТ №{count}:",bg=bagr,font=("Arial",40,"bold")).place(x=449,y=400)
                rel_vopr = tk.Text(vk,bg=bbg,font=("Arial",20,"bold"),height=6,width=79,wrap="word")
                rel_vopr.place(x=5,y=80)
                rel_vopr.bind("<KeyRelease>", cou)
                slo = tk.Label(vk,text=f"0/475",bg=bagr,font=("Arial",15,"bold"))
                slo.place(x=1130,y=280)
                rel_otv = tk.Text(vk,bg=bbg,font=("Arial",20,"bold"),width=79,height=1,wrap="word",pady=10)
                rel_otv.place(x=5,y=470)
                rel_otv.bind("<KeyRelease>", k)
                if bac:
                    rel_vopr.insert("1.0", vopry[count - 1])
                    rel_otv.insert("1.0", otvy[count - 1])
                df = tk.Label(vk,text=f"0/80",bg=bagr,font=("Arial",15,"bold"))
                df.place(x=1130,y=530)
                def ba():
                    vk.destroy()
                    multy_menu()
                f = tk.Button(vk, image=imag, bg=bagr, command=ba, activebackground=bagr,
                              relief="flat", width=60, height=50, ).place(x=20,y=20)
                def play_g():
                    pass
                pla = tk.Button(vk,bg=bbg,text="ИГРАТЬ",relief="flat",font=("Arial",40,"bold"),activebackground=abg,command = play_g)
                pla.place(x=471, y=780)
                def b():
                    sohr()
                    global count,bac
                    count -= 1
                    vk.destroy()
                    bac = True
                    vopr()
                def fo():
                    sohr()
                    global count,bac
                    bac = False
                    count += 1
                    vk.destroy()
                    vopr()
                b_b = tk.Button(vk,bg=bagr,image=lev,activebackground=bagr, command=b,relief = "flat")
                f_b = tk.Button(vk,bg=bagr,image=prav,activebackground=bagr, command=fo, relief = "flat")
                b_b.place(x=10,y=700)
                f_b.place(x=1000,y=710)
                if count > 1:
                    b_b.configure(state="normal")
                if count < 99:
                    f_b.configure(state="normal")
                if count == 1:
                    b_b.configure(state="disabled")
                if count == 99:
                    f_b.configure(state="disabled")
                vk.pack()
            vopr()
        menu.destroy()
        multy = tk.Frame(window, bg=bagr,)
        pick = tk.Label(multy,text = "ВЫБЕРИТЕ ИГРУ", bg=bagr, fg=tex,font=("arial", 75, "bold"), anchor="n",padx = 200).pack()
        btn1 = tk.Button(multy, text="ВИСЕЛИЦА ДЛЯ 2", bg=bbg, fg=tex, font=("arial", 40, "bold"),
                         activebackground=abg, pady=7, relief="flat",command=vis2).pack(pady=10)
        btn2 = tk.Button(multy, text="ВИКТОРИНА", bg=bbg, fg=tex, font=("arial", 40, "bold"), relief="flat",padx = 72,
                         activebackground=abg, pady=7,command=vik ).pack(pady=10)
        btn3 = tk.Button(multy, text="СЛОВА", bg=bbg, fg=tex, font=("arial", 40, "bold"), relief="flat",padx = 141,
                         activebackground=abg, pady=7, ).pack(pady=10)
        btn4 = tk.Button(multy,width=60,height=50,image = imag,relief = "flat",command=back,activebackground=bagr).place(x = 20, y = 20)

        multy.pack()


    #тело фунции меню
    menu = tk.Frame(window)
    menu["bg"] = bagr
    menutext = tk.Label(menu, bg=bagr, fg=tex, text="МЕНЮ", font=("arial", 100, "bold"), anchor="n",padx = 400,pady=50).pack()
    solo_btn = tk.Button(menu, text="ОДИНОЧНАЯ ИГРА", bg=bbg, fg=tex, font=("arial", 50, "bold"),pady= 10,
                         activebackground=abg, command=solo,padx = 22,relief = "flat"
                         ).pack()
    multy_btn = tk.Button(menu, text="СОВМЕСТНАЯ ИГРА", bg=bbg, fg=tex, font=("arial", 50, "bold"),relief = "flat",
                          activebackground=abg, pady=10,command = multy_menu,
                         ).pack(pady=20, )
    exit = tk.Button(menu, text="ВЫХОД", bg=bbg, fg=tex, font=("arial", 47, "bold"),relief = "flat",activebackground=abg, pady=10,
                     command=exit
                     ).pack(pady=100)
    Music_info = tk.Label(menu,text = "fnonose - blessed",bg = bagr, fg = tex, font = ("arial", 10, "bold")).place(x = 3,y = 870)


    # функция вкл/выкл информации
    def oninf():#функция вкл информации
        sound1.play()
        def offinf(): #функция выкл информации
            sound1.play()
            info2.destroy()
            te.destroy()
            info3 = tk.Button(menu, width=70, height=60, relief="flat", bg=bagr, image=image3, command=oninf,activebackground=bagr, )
            info3.place(x=1100, y=806)

        info1.destroy()
        info2 = tk.Button(menu, width=70, height=60, relief="flat", bg=bagr, image=image3, command=offinf,activebackground=bagr, )
        info2.place(x = 1100, y = 806)
        te = tk.Label(menu,text = "ПРОГРАММА ПРОЕКТ\n АВТОР: ДЕНИС УРУСОВ ",bg = bagr, fg = tex,
                      font = ("arial", 10, "bold"))
        te.place(x=900, y=820)
    info1 = tk.Button(menu, width=70, height=60, relief="flat", bg=bagr,image = image3,command = oninf,activebackground=bagr,)
    info1.place(x= 1100,y = 806)


    #функция вкл/выкл музыки
    def off(): #функция выкл
        def on(): #функция вкл
            stop_music = tk.Button(menu, width=70, height=60, image=image1, relief="flat", bg=bagr,activebackground=bagr, command=off,)
            stop_music.place(x=20, y=806)
            mixer.music.unpause()
            sound1.set_volume(1)

        stop_music.destroy()
        play_music = tk.Button(menu, width=70, height=60, image=image2, relief="flat", bg=bagr,activebackground=bagr,command=on, )
        play_music.place(x=20, y=806)
        mixer.music.pause()
        sound1.set_volume(0)
    stop_music = tk.Button(menu,width=70,height=60,image = image1,relief = "flat",bg = bagr,activebackground=bagr,command = off,)
    stop_music.place(x = 20, y = 806)

    menu.pack()
menu_1()
window.mainloop()
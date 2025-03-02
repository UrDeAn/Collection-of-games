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
az = ImageTk.PhotoImage(file =r"pictures\az.png")
inp = ImageTk.PhotoImage(file=r"pictures\inpt.png")

#музыка с помощью pygame
mixer.init()
mixer.music.load(r'music\Музыка.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)

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
            sound1.play()
            def back_1():
                diff_menu.destroy()
                solo()

            def diff(difficul):
                sound1.play()
                global gn
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
                sound1.play()
                guess_num = random.randint(1, max_num)
                global one,count,numbr
                one = True
                count = 0
                numbr = " "
                diff_menu.destroy()
                def back_gn():
                    sound1.play()
                    gn.destroy()
                    solo()

                def inpt(number):
                    global one,numb,input_menu_2,numbr,count
                    if number == "del" and count != 0:
                        input_menu_2.destroy()
                        error_lbl.configure(text="")
                        count -= 1
                        numbr = numbr[0:-1]
                        input_menu_2 = tk.Label(text=numbr, font=("arial", 100, "bold"), bg=bbg, fg=tex)
                        if len(numbr) == 1:
                            input_menu_2.place(x=463, y=520)
                        elif len(numbr) == 2:
                            input_menu_2.place(x=426, y=520)
                        elif len(numbr) == 3:
                            input_menu_2.place(x=389, y=520)
                        elif len(numbr) == 4:
                            input_menu_2.place(x=352, y=520)
                        elif len(numbr) == 5:
                            input_menu_2.place(x=315, y=520)
                        elif len(numbr) == 6:
                            input_menu_2.place(x=278, y=520)
                        elif len(numbr) == 7:
                            input_menu_2.place(x=241, y=520)
                        elif len(numbr) == 8:
                            input_menu_2.place(x=204, y=520)
                        numb = numbr
                        print(count)
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
                            input_menu_2.place(x=463, y=520)
                        elif len(numbr) == 2:
                            input_menu_2.place(x=426, y=520)
                        elif len(numbr) == 3:
                            input_menu_2.place(x=389, y=520)
                        elif len(numbr) == 4:
                            input_menu_2.place(x=352, y=520)
                        elif len(numbr) == 5:
                            input_menu_2.place(x=315, y=520)
                        elif len(numbr) == 6:
                            input_menu_2.place(x=278, y=520)
                        elif len(numbr) == 7:
                            input_menu_2.place(x=241, y=520)
                        elif len(numbr) == 8:
                            input_menu_2.place(x=204, y=520)
                        numb = numbr
                        count += 1
                        print(count)

                back_gn_btn = tk.Button(gn,image=imag,bg=bagr,command = back_gn,activebackground=bagr,
                                            relief="flat",width=60,height=50).place(x=20,y=20)
                for i in range(10):
                    globals()["numbr" + str(i)] = tk.Button(gn,text = i,relief="flat",activebackground=abg,bg=bbg,
                                                font= ("arial", 45, "bold"),padx=10,command=lambda number = i:inpt(number))

                    globals()["numbr" + str(i)].place(x=20+i*117,y=730)
                input_menu = tk.Label(gn,bg=bbg, fg=tex,pady=70,padx=350)
                input_menu.place(x=248,y=520)
                inp_btn = tk.Button(gn,bg=bagr,activebackground=bagr,relief="flat",image = inp,height=160).place(x=50,y=510)
                del_alf = tk.Button(gn,text = "FF",command=lambda number = "del":inpt(number)).place(x=200,y=200)
                error_lbl = (tk.Label(gn,bg=bagr,font=("arial", 25, "bold"),fg=red,))
                error_lbl.place(x=262,y=476)
                gn.pack()


        menu.destroy()
        solo_menu = tk.Frame(window, bg=bagr,)
        gamepick = tk.Label(solo_menu,text = "ВЫБЕРИТЕ ИГРУ", bg=bagr, fg=tex,font=("arial", 75, "bold"), anchor="n",padx = 200).pack()
        btn1 = tk.Button(solo_menu, text="ВИСЕЛИЦА", bg=bbg, fg=tex, font=("arial", 40, "bold"),padx = 235,
                         activebackground=abg, pady=7,relief = "flat",command= visilica).pack(pady = 15)
        btn2 = tk.Button(solo_menu, text="КАМЕНЬ,НОЖНИЦЫ,БУМАГА", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",
                         activebackground=abg, pady=7,command= RockPaperScissors).pack(pady = 15)
        btn3 = tk.Button(solo_menu, text="УГАДАЙ ЧИСЛО", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 175,
                         activebackground=abg, pady=7, command = guess_number ).pack(pady=15)
        btn4 = tk.Button(solo_menu, text="ПОВТОРИ ЗА МНОЙ", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 122,
                         activebackground=abg, pady=7, ).pack(pady=15)
        btn5 = tk.Button(solo_menu, text="БИНГО", bg=bbg, fg=tex, font=("arial", 40, "bold"),relief = "flat",padx = 292,
                         activebackground=abg, pady=7, ).pack(pady=15)
        btn6 = tk.Button(solo_menu,width=60,height=50,image = imag,relief = "flat",command=back,activebackground=bagr).place(x=20, y=20)

        solo_menu.pack()


    def multy_menu(): #функция выбора совместной игры
        sound1.play()
        def back(): #фунця возврата в меню
            sound1.play()
            multy.destroy()
            menu_1()

        menu.destroy()
        multy = tk.Frame(window, bg=bagr,)
        pick = tk.Label(multy,text = "ВЫБЕРИТЕ ИГРУ", bg=bagr, fg=tex,font=("arial", 75, "bold"), anchor="n",padx = 200).pack()
        btn1 = tk.Button(multy, text="ВИСЕЛИЦА ДЛЯ 2", bg=bbg, fg=tex, font=("arial", 40, "bold"),
                         activebackground=abg, pady=7, relief="flat").pack(pady=10)
        btn2 = tk.Button(multy, text="ВИКТОРИНА", bg=bbg, fg=tex, font=("arial", 40, "bold"), relief="flat",padx = 72,
                         activebackground=abg, pady=7, ).pack(pady=10)
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
    def oninf():
        sound1.play()
        #функция вкл информации
        def offinf():
            sound1.play()
            #функция выкл информации
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
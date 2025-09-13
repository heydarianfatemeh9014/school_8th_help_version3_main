# import the mudols
from tkinter import *
from PIL import Image , ImageTk
from subprocess import *
from chem import *
from fizik import *
from riazi import*
import pygame  # ایمپورت کتابخانه pygame برای پخش موسیقی

#root setting
def mainn():
    root = Tk()
    root.geometry('800x800')
    root.resizable(False,False)
    root.title('window to knowledge')
    def sound_play():
        pygame.mixer.init()  # مقداردهی اولیه میکسر pygame
        pygame.mixer.music.load("codes\\bib.mp3")  # بارگذاری فایل صوتی
        pygame.mixer.music.play()
    #backgroun setting

    image = Image.open('imagess\\wall1.jpg')
    image = image.resize((800,800))
    bg_image = ImageTk.PhotoImage(image)

    bg_lbl = Label(root, image=bg_image)
    bg_lbl.place(relheight=1,relwidth=1)

    def chimi():
        sound_play()
        chemm()

    def fizik():

        sound_play()
        fizikk()

    def riazi():

        sound_play()
        riazii()
    chimi_btn = Button(root,bg='#C1C8F5',activeforeground='#C1C8F5',fg='#656980',activebackground='#656980' ,command= chimi , text='                                شیمی                                  ',font=('Segoe Print',20,'bold')).place(x=1,y=20)
    fizik_btn = Button(root,bg='#F5ACA6',activeforeground='#F5ACA6',fg='#80322D',activebackground='#80322D' ,command= fizik , text='                                فیزیک                                 ',font=('Segoe Print',20,'bold')).place(x=1,y=120)
    riaz_btn = Button(root,bg='#B0F4BC',activeforeground='#B0F4BC',fg='#5C8063',activebackground='#5C8063' ,command= riazi , text='                                 ریاضی                                ',font=('Segoe Print',20,'bold')).place(x=1,y=220)


    root.mainloop()
if __name__ == "__main__":
    mainn()
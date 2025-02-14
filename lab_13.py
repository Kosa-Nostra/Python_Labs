from tkinter import *

def message():
    print("Кнопка нажата!")

# Создаем объект главного окна
root = Tk()


but = Button(root, text="Печать", command=message)
but.pack()

root.mainloop()

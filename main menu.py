from tkinter import *

root = Tk()
root.title('Phone book')
root.geometry('600x500')

main_menu = Menu(root)
main_menu.add_command(label='Создать запись')
pass
main_menu.add_command(label='Найти запись')
pass
main_menu.add_command(label='Редактировать запись')
pass
main_menu.add_command(label='Удалить запись')
pass
main_menu.add_command(label='Выйти из программы')
pass

root.config(menu=main_menu)
root.mainloop()
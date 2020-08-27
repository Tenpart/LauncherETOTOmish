from tkinter import *
from PIL import Image, ImageTk

root = Tk()

#Config window
root.geometry('800x600')
root.title('Launcher HNP')
root.iconbitmap('C:/Users/lesch/Documents/Photo/space_car_icon_149810.ico')
root.resizable(width = False, height = False)



#IMG-----Button
image = ImageTk.PhotoImage(file="C:/Users/lesch/Documents/Photo/button.png", size = "20, 2")
Button(root, image=image, command=lambda: print('click')).place(x = 100, y = 100)


#IMG





#Enter



#Label



#bind





#Function




root.mainloop()
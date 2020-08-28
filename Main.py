from tkinter import *
from PIL import Image, ImageTk

root = Tk()

#Config window
root.geometry('800x600')
root.title('Launcher HNP')
root.iconbitmap('C:/Users/lesch/Documents/Photo/space_car_icon_149810.ico')
root.resizable(width = False, height = False)



#IMG-----Button
image = Image.open('C:/Users/lesch/Documents/Photo/button.png')
image = image.resize((160, 90), Image.ANTIALIAS) ## The (250, 250) is (height, width)
image = ImageTk.PhotoImage(image)
Button(root, bd = 0 ,activebackground = '#fff',image=image, command=lambda: print('click')).place(x = 300, y = 500)


#IMG





#Enter



#Label



#bind





#Function




root.mainloop()
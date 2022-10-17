from tkinter import *
#1
'''

window = Tk()

input_entry = Entry(window, width = 50)
input_entry.pack()

button = Button(window, text = '처리')
button.pack()

label = Label(window, text = ' ')
label.pack()
window.mainloop()
'''
#2
def entry_to_label():
    str = input_entry.get()
    label.config(text = str)

window = Tk()

input_entry = Entry(window, width = 50)
input_entry.pack()

button = Button(window, text = '처리',command= entry_to_label)
button.pack()

label = Label(window, text = ' ')
label.pack()
window.mainloop()

#중간고사는 제외
#제출도 제외
import tkinter

window = tkinter.Tk()
label=tkinter.Label(text='Введіть кількість елементів:')
label.pack()
s = tkinter.StringVar()
edit=tkinter.Entry(main, textvariable=s)
edit.pack()
x = []
def button_click():
    n=int(s.get())
    i=0
    for i in range(n):
        x.append(int(input()))

button=tkinter.Button(window, text='Розпочати введення',command=button_click)
button.pack()
window.mainloop()

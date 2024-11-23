from tkinter import*

window = Tk()
window.title("Number pads")
window.geometry("250x300")
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=window,relief=RAISED,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame, text=nums[i][j] ,bg="#d0efff",fg="black")
        label.pack(padx=3,pady=3)
window.mainloop()

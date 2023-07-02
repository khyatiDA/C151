from tkinter import*

window = Tk()

window.title("SALES APPLICATION ")
window.geometry("600x600")
window.config(background="SandyBrown")

months = ("Jan" ,"Feb" , "March" , "April" , "May" , "June" , "July" , "Aug" , "Sep" ,"Oct" , "Nov" ,"Dec")

profit = (20000 , 5000 , 3700 , 4500 , 2800 , 3000 , 6000 , 50000 , 79000 , 56000 , 9700 , 2002)


months_value = Label(window)
profit_value = Label(window)
max_value = Label(window)


months_value.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
profit_value.place(relx = 0.5, rely = 0.4 , anchor = CENTER)
max_value.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)



def max_fuction():
   


    highest = max(profit)
    index_max = profit.index(highest)
    profit_value['text']= "This is the highest sale :" , highest
    months_value['text']= "and the month is :" , months[index_max]+ str(months)


btn = Button(window , text = "Show Max Profitable Month" , command = max_fuction)
btn.place(relx=0.5 , rely=0.5 , anchor=CENTER)













window.mainloop()
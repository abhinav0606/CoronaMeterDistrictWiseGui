from tkinter import *
import requests
import matplotlib
from tkinter import messagebox
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
root=Tk()
root.geometry("900x500")
root.title("Corona Virus District wise Tracker")
def get_value():
    try:
        s=state.get()
        c=city.get()
        data = requests.get("https://api.covid19india.org/state_district_wise.json")
        gd = data.json()
        # pprint.pprint(gd)
        # State = input("Enter the State")
        s = s.title()
        # District = input("Enter the District")
        c = c.title()
        x = (gd[s]['districtData'][c])
        s = {}
        s['active'] = x['active']
        s['confirmed'] = x['confirmed']
        s['deaths'] = x['deceased']
        s['recovered'] = x['recovered']
        active = s['active']
        confirmed = s['confirmed']
        deaths = s['deaths']
        recovered = s['recovered']
        root3 = Tk()
        root2 = Tk()
        root3.title("Number Theory")
        root3.geometry("300x180")
        root3.config(bg="grey")
        root2.geometry("600x500")
        root2.title("Graphical Analysis")
        Active = Label(root3, text="Active:" + str(active), bg="Red")
        Active.pack()
        Confirmed = Label(root3, text="Confirmed:" + str(confirmed), bg="silver")
        Confirmed.pack()
        Deaths = Label(root3, text="Deaths:" + str(deaths), bg="Purple")
        Deaths.pack()
        Recovered = Label(root3, text="Recovered:" + str(recovered), bg="Green")
        Recovered.pack()
        fig = Figure(figsize=(1, 1))
        plot = fig.add_subplot(1, 1, 1)
        plot.bar(s.keys(), s.values())
        plt.title(f"{c} Corona Meter")
        # fig.autofmt_xdate()
        plt.savefig("Meter.png")
        canvas=FigureCanvasTkAgg(fig,master=root2)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        canvas.draw()
        root3.mainloop()
        root2.mainloop()
        # f1.tkraise()
    except:
        # messagebox.showerror("No cases")
        messagebox.showinfo("Good news","This City has no covid cases")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
# frame3=Frame(root)
# frame3.pack()
# for frame in (frame1,frame2):
    # frame.grid(row=0, column=0, sticky='news')
state=StringVar()
city=StringVar()
l=Label(root,text="Enter the State")
l.place(x=230,y=125)
l2=Label(root,text="Enter the City")
l2.place(x=230,y=190)
Input1=Entry(root,textvariable=state,width=50).place(x=230,y=150)
Input2=Entry(root,textvariable=city,width=50).place(x=230,y=210)
B1=Button(root,text="Get Details",command=get_value,bg="green")
B1.place(x=230,y=250)
# frame1.tkraise()
root.mainloop()
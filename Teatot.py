from tkinter import*
import random
import time
import datetime


root=Tk()
root.geometry("1600x800")
root.title("Tea tot management system")

Tops=Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=700,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lb1info=Label(Tops,font=('helvetica',50,'bold'),text="TEA TOT RESTURANT",fg="Black",bd=10,anchor='w')
lb1info.grid(row=0,column=0)

lb1info=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="steelblue",bd=10,anchor='w')
lb1info.grid(row=1,column=0)

def Ref():
    x=random.randint(109808,500876)
    randomRef=str(x)
    rand.set(randomRef)
    f=open("tanmay.txt","at")
    if(Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())
         
         
    if(Chapati.get()==""):
        CoChapati=0
    else:
        CoChapati=float(Chapati.get())
        
    if(Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())
         
    if(Chicken.get()==""):
        CoChicken=0
    else:
        CoChicken=float(Chicken.get())
         
    if(Beef.get()==""):
        CoBeef=0
    else:
        CoBeef=float(Beef.get())
         
    if(Drinks.get()==""):
        CoDrink=0
    else:
        CoDrink=float(Drinks.get())
         
      
    CoFries=CoFries*100
    CoDrink=CoDrink*150
    CoChapati=CoChapati*50
    CoChicken=CoChicken*260
    CoSoup=CoSoup*100
    CoBeef=CoBeef*300
     
    Costofmeal="Ksh",str('%0.2f' % (CoBeef+CoDrink+CoFries+CoSoup+CoChapati+CoChicken))
     
    paytax=((CoChicken+CoChapati+CoBeef+CoDrink+CoFries+CoSoup)*0.2)
     
    Totalcost=(CoSoup+CoBeef+CoDrink+CoSoup+CoFries+CoChicken)
     
    ser_charge=((CoChicken+CoBeef+CoDrink+CoFries+CoChapati+CoSoup)/99)
     
    Service="Ksh",str('%0.2f'% ser_charge)
     
    OverAllcost="Ksh",str('%0.2f'%(paytax+ser_charge+Totalcost))
    to=str(OverAllcost)
    paidtax="Ksh",str('%0.2f'%(paytax))
    f.write(to)
    Service_charge.set(Service)
    Cost.set(Costofmeal)
    Tax.set(paidtax)
    SubTotal.set(Costofmeal)
    Total.set(OverAllcost)
    file.write(Cost)
    file.close()
    f.close()
     
def qExit():
    root.destroy()
    
def Reset():
    rand.set("")
    Fries.set("")
    Beef.set("")
    Drinks.set("")
    Soup.set("")
    Chicken.set("")
    Chapati.set("")
    Service_charge.set("")
    SubTotal.set("")
    Tax.set("")
    Cost.set("")
    Total.set("")
    
    
rand=StringVar()
Fries=StringVar()
Chapati=StringVar()
Drinks=StringVar()
Soup=StringVar()
Chicken=StringVar()
Beef=StringVar()
Service_charge=StringVar()
SubTotal=StringVar()
Tax=StringVar()
Cost=StringVar()
Total=StringVar()


lb1Reference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lb1Reference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lb1Fries=Label(f1,font=('arial',16,'bold'),text="Fries",bd=16,anchor='w')
lb1Fries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lb1Chapati=Label(f1,font=('arial',16,'bold'),text="Chapati",bd=16,anchor='w')
lb1Chapati.grid(row=2,column=0)
txtChapati=Entry(f1,font=('arial',16,'bold'),textvariable=Chapati,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChapati.grid(row=2,column=1)

lb1Soup=Label(f1,font=('arial',16,'bold'),text="Soup",bd=16,anchor='w')
lb1Soup.grid(row=3,column=0)
txtSoup=Entry(f1,font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lb1Beef=Label(f1,font=('arial',16,'bold'),text="Beef",bd=16,anchor='w')
lb1Beef.grid(row=4,column=0)
txtBeef=Entry(f1,font=('arial',16,'bold'),textvariable=Beef,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBeef.grid(row=4,column=1)

lb1Chicken=Label(f1,font=('arial',16,'bold'),text="Chicken",bd=16,anchor='w')
lb1Chicken.grid(row=5,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChicken.grid(row=5,column=1)

lb1Drinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lb1Drinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)
    
lb1Cost=Label(f1,font=('arial',16,'bold'),text="Cost",bd=16,anchor='w')
lb1Cost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)

lb1Service=Label(f1,font=('arial',16,'bold'),text="Service",bd=16,anchor='w')
lb1Service.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)

lb1Statetax=Label(f1,font=('arial',16,'bold'),text="Statetax",bd=16,anchor='w')
lb1Statetax.grid(row=3,column=2)
txtStatetax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStatetax.grid(row=3,column=3)

lb1SubTotal=Label(f1,font=('arial',16,'bold'),text="SubTotal",bd=16,anchor='w')
lb1SubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lb1TotalCost=Label(f1,font=('arial',16,'bold'),text="TotalCost",bd=16,anchor='w')
lb1TotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

btnTotal=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),width=10,text="TOTAL",bg="powder blue",command=Ref).grid(row=7,column=1)

btnREset=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExist=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),width=10,text="Exist",bg="powder blue",command=exit).grid(row=7,column=3)

root.mainloop()
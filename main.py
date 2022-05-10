
from tkinter import *
from tkinter import ttk
root=Tk()
root.config(bg="silver")
root.title("LET'S SHOP")
root.geometry("1280x720")
root.resizable(False,False)
    #••••LEFT - KOKO's E-STORE
kokosLabel=Label(root,padx=30,pady=30,text="AFFORDABLE E-STORE",fg="Black",bg="olive",font=("Andale Mono","30","bold"))
kokosLabel.pack(side=LEFT,fill=Y)
availableLabel=Label(root,padx=5,pady=5,text="24/7 availability",fg="green",bg="gold",font=("gotham","20"))
availableLabel.place(x=90,y=380)
shopnowButton=Button(root,padx=10,pady=10,text="SHOP NOW", fg="red",bg="green", font=("Times","15","bold"))
shopnowButton.place(x=120,y=550)
    #••••CATEGORY
catLabel=Label(root,text="CATERGORY", bg= "silver",fg="grey", font=("courier","30"))
catLabel.place(x=400,y=150)
fngButton=Button(root,text="FRUITS & VEGETABLES", fg="black")
fngButton.place(x=410,y=200)
provisionButton=Button(root,text="PROVISIONS", fg="black")
provisionButton.place(x=410,y=250)
cosmeticButton=Button(root,text="COSMETICS", fg="black")
cosmeticButton.place(x=410,y=300)
    # ••••ITEM
itemLabel=Label(root,text="ITEM", bg= "silver",fg="grey", font=("courier","30"))
itemLabel.place(x=600,y=150)
itemfg=('apple','banana','mango','carrot','cucumber')
cmb=ttk.Combobox(root,value=itemfg,width=10)
cmb.place(x=600,y=200)
itemprov=('milk','coffee','sugar','cereal')
cmb=ttk.Combobox(root,value=itemprov,width=10)
cmb.place(x=600,y=250)
itemcos=('perfume','body cream','hair cream')
cmb=ttk.Combobox(root,value=itemcos,width=10)
cmb.place(x=600,y=300)
    # ••••AMOUNT
amtLabel=Label(root,text="AMOUNT", bg= "silver",fg="grey", font=("courier","30"))
amtLabel.place(x=750,y=150)
amtEntry1=Entry(root, bg="lavender",bd=2.5, width=12)
amtEntry1.place(x=750,y=200)
amtEntry2=Entry(root, bg="lavender",bd=2.5, width=12)
amtEntry2.place(x=750,y=250)
amtEntry3=Entry(root, bg="lavender",bd=2.5, width=12)
amtEntry3.place(x=750,y=300)
    #••••QUANTITY
qtyLabel=Label(root,text="QUANTITY", bg= "silver",fg="grey", font=("courier","30"))
qtyLabel.place(x=890,y=150)
qtyfg=(1,2,3,4,5)
cmb=ttk.Combobox(root,value=qtyfg,width=10)
cmb.place(x=900,y=200)
cmb=ttk.Combobox(root,value=qtyfg,width=10)
cmb.place(x=900,y=250)
cmb=ttk.Combobox(root,value=qtyfg,width=10)
cmb.place(x=900,y=300)
    # ••••TOTAL
totalLabel=Label(root,text="TOTAL", bg= "silver",fg="grey", font=("courier","30"))
totalLabel.place(x=1070,y=150)
totalEntry1=Entry(root, bg="lavender",bd=5, width=15)
totalEntry1.place(x=1070,y=200)
totalEntry1=Entry(root, bg="lavender",bd=5, width=15)
totalEntry1.place(x=1070,y=250)
totalEntry1=Entry(root, bg="lavender",bd=5, width=15)
totalEntry1.place(x=1070,y=300)
    # ••••BIG TOTAL
totalEntry1=Entry(root, bg="dark grey",bd=8, width=25)
totalEntry1.insert(0,"₦")
totalEntry1.place(x=1000,y=400)
    # ••••CHECKOUT
chkoutButton=Button(root, text="CHECKOUT",bg="silver", fg="grey", width=10)
chkoutButton.place(x=1000,y=450)
    # ••••THANK YOU FOR SHOPPING
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
thanksLabel=Label(bottomFrame, text="THANK YOU FOR SHOPPING",bg="silver", fg="grey")
thanksLabel.pack()

njnklnklnlk
root.mainloop()




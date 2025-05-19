import tkinter as tk
import pyshorteners as ps
import pyperclip
import qrcode
window= tk.Tk()
window.geometry("500x250")
window.config(bg="skyblue")
def Shorturl():
    u1=url.get()
    s= ps.Shortener()
    a =s.tinyurl.short(u1)
    
    l1= tk.Label(f1,text="Shortened URL",font="bold")
    l1.place(relx=0.35,rely=0.1)
    
    u1_w= tk.StringVar()
    u1_w.set(a)
    u1= tk.Entry(f1,width=50,textvariable= u1_w)
    u1.place(relx=0.1,rely=0.3)
    
    b2= tk.Button(f1,text="Copy URL",command= pyperclip.copy(a))
    b2.place(relx=0.4,rely=0.55)
    
def qr():
    a=url.get()
    
    qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (number of boxes)
    )
    
    # Add the URL data to the QR code
    qr.add_data(a)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_path = "qr_code.png"
    img.save(img_path)
    
    # Open the image automatically
    img.show()
    
    

l1= tk.Label(window,text="URL: ",bg="skyblue")
l1.place(relx=0.1,rely=0.2)

url= tk.StringVar()
u= tk.Entry(window,width=50,textvariable= url )
u.place(relx=0.2,rely=0.2)

gb= tk.Button(window,text="Generate link",command= Shorturl)
gb.place(relx=0.3,rely=0.3)

gb= tk.Button(window,text="Generate QR",command= qr)
gb.place(relx=0.5,rely=0.3)

f1= tk.Frame(window,width=400, height=130,bd=3, relief="ridge")
f1.place(relx=0.1,rely=0.5)

window.mainloop()

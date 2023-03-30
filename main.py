import customtkinter
import serial
import time

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x200")
root.pack_propagate = False
root.title("Arduino Communications")

target = 0

ser = serial.Serial(port="COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

def ledOn():
    ser.write("1".encode('Ascii'))

def ledOff():
    ser.write("0".encode('Ascii'))

fontH = customtkinter.CTkFont("Helvetica", 20)

label = customtkinter.CTkLabel(master=root, text="LED", font=fontH)
label.pack(pady=0, padx=10)
label.place(x=182, y=10)

frame = customtkinter.CTkFrame(master=root, bg_color="#e3e3e3")
frame.pack(pady=0, padx=20, fill="none", expand=True)

buttonOn = customtkinter.CTkButton(width=150, height=25, master=frame, text="On", command=ledOn, font=customtkinter.CTkFont("Helvetica", 15))
buttonOn.pack(pady=10, padx=10)

buttonOff = customtkinter.CTkButton(width=150, height=25, master=frame, text="Off", command=ledOff, font=customtkinter.CTkFont("Helvetica", 15))
buttonOff.pack(pady=10, padx=10)


root.mainloop()

ser.close()

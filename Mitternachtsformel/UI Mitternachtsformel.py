# Autor: Tobias Brogle
import tkinter as tk
from tkinter import messagebox

def mitternachtsformel():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = b**2 - 4*a*c
        if d < 0:
            messagebox.showinfo( f"Error, keine Lösung", "Die Diskriminante ist negativ\nDiskriminante = " + str(d))
        else:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            messagebox.showinfo("Lösung", f"x1 = {x1}\nx2 = {x2}")
    except:
        messagebox.showinfo("Error", "Bitte geben Sie nur Zahlen ein")
        
root = tk.Tk()
root.title("Mitternachtsformel")
root.geometry("300x200")

label_a = tk.Label(root, text="a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

button = tk.Button(root, text="Berechnen", command=mitternachtsformel)
button.pack()

root.mainloop()


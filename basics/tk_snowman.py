import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=1200, height=800, bg='white')
canvas.pack(side='top', fill='both', expand=True)

canvas.create_rectangle(0, 0, 1200, 450, fill="darkblue")
canvas.create_rectangle(0, 450, 1200, 800, fill="darkgrey")

Y = 200
for R in [50, 70, 100]:
    canvas.create_oval(600 - R, Y, 600 + R, Y + 2 * R, fill="white")
    Y += 2 * R

root.mainloop()

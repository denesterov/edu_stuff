import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=1200, height=800, bg='white')
canvas.pack(side='top', fill='both', expand=True)

canvas.create_rectangle(50, 50, 1150, 750, fill="lightgrey")

canvas.create_line(50, 400, 1150, 400, fill='darkgray', width=3)
canvas.create_line(600, 50, 600, 750, fill='darkgray', width=3)

unit_x = 50
unit_y = 50

for koeff, color in [(1.0, 'green'), (0.5, 'red'), (2.0, 'blue')]:
    for x in range(100, 1100, 10):
        xx = (x - 600) / unit_x
        yy = xx * koeff
        y = round(400 - yy * unit_y)
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline=color, width=2)

root.mainloop()

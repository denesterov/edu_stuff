import tkinter as tk

Koeff = -2.0
K_min, K_max, K_delta = -2.0, +2.0, 0.1


root = tk.Tk()

canvas = tk.Canvas(root, width=1200, height=800, bg='white')
canvas.pack(side='top', fill='both', expand=True)

canvas.create_rectangle(50, 50, 1150, 750, fill="lightgrey")

canvas.create_line(50, 400, 1150, 400, fill='darkgray', width=3)
canvas.create_line(600, 50, 600, 750, fill='darkgray', width=3)

unit_x = 50
unit_y = 50

tk_ids = []


def draw_graph():
    for x in range(100, 1100, 10):
        xx = (x - 600) / unit_x
        yy = xx * Koeff
        y = round(400 - yy * unit_y) # ось Y на экране направлена вниз
        tkid = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='blue', outline='blue', width=2)
        tk_ids.append(tkid)


def tick():
    for tkid in tk_ids:
        canvas.delete(tkid)
    tk_ids.clear()

    draw_graph()

    global Koeff
    Koeff += K_delta
    if Koeff > K_max:
        Koeff = K_min

    canvas.after(300, tick)


canvas.after(300, tick)
root.mainloop()

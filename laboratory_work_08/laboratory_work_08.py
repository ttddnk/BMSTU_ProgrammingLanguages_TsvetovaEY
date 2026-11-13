import tkinter as tk

def read_data():
    names = []
    wholesale = []
    retail = []
    with open("coffe.txt", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip()
            parts = line.split(";")
            names.append(parts[0])
            wholesale.append(float(parts[1]))
            retail.append(float(parts[2]))
    return names, wholesale, retail

names, wholesale, retail = read_data()
n = len(names)
print(n, names, wholesale, retail)

root = tk.Tk()
root.title("цены на кофу")

def draw(n, wholesale, retail, names):
    k = 0.7
    maxX = int(root.winfo_screenwidth()*k)
    maxY = int(root.winfo_screenheight()*k)
    cv = tk.Canvas(root, width=maxX, height=maxY, bg = "white")
    cv.grid()
    maxX, maxY
    left = top = 180
    right = 30
    bottom = 300
    x0 = left
    x1 = maxX - right
    y0 = top
    y1 = maxY - bottom
    Ymax = max(max(wholesale), max(retail))*1.1
    Ky= (y1-y0)/Ymax
    cv.create_rectangle(x0, y0, x1, y1, outline="red")
    cv.create_line(x0, y1, x1, y1, width=2, arrow="last")
    cv.create_line(x0, y0, x0, y1, width=2, arrow="first")


    #cv.create_rectangle(x0 + 20, (y1 - Ky*wholesale[0]), x0 + 60, y1, fill="blue")
    gw = (x1 - x0)/n
    bw = gw*0.4
    for i in range(n):
        cx = x0 + gw*(i +0.5)
        cv.create_rectangle(cx - bw, (y1 - Ky*wholesale[i]), cx, y1, fill="blue")
        cv.create_rectangle(cx, (y1 - Ky*retail[i]), cx + bw, y1, fill="pink")
        cv.create_text(cx, y1 +8, text=names[i], angle=90, anchor="e")

    step=int(Ymax/8)
    v = 0
    while v <= Ymax:
        y = y1 - Ky*v
        cv.create_line(x0 - 5, y, x0, y)
        cv.create_text(x0-8, y, text=str(v), anchor="e")
        cv.create_line(x0, y, x1, y, fill="black", dash=30)

        v += step


    cv.create_text(maxX / 2, 25, text="оптовые и розничные цены на кофе", font=("Arial", 15, "bold"))
    cv.create_text(x0-100, y0+5, text="цена", angle=90)
    cv.create_text(x0+100, y0+100*11+30, text="оптовые/розничные", angle=0)
draw(n, wholesale, retail, names)








root.mainloop()
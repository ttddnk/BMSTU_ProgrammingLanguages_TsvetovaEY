import tkinter as tk
import random
W = H = 640
C = W // 2
MARGIN = 60
BATCH = 100

def in_area(x, y, r):
    if (x <= 0) and (y >= 0) and (x**2 + y**2 <= r**2) and (y >= x + r):
        return True
    elif (x >= 0) and (y >= 0) and (x <= r) and (y <= r) and (x**2 + y**2 >= r**2):
        return True
    elif (x >= 0) and (y <= 0) and (x**2 + y**2 <= r**2):
        return True
    elif (x <= 0) and (y <= 0) and (x >= -r) and (y >= -r) and (x**2 + y**2 >= r**2):
        return True
    return False

root = tk.Tk()
top = tk.Frame(root)
top.pack(pady=5)
tk.Label(top, text="R =").pack(side="left")
e_r = tk.Entry(top, width=6)
e_r.insert(0, "5")
e_r.pack(side="left", padx=(0, 10))
tk.Label(top, text="Число испытаний N (до 10000) =").pack(side="left")
e_n = tk.Entry(top, width=7)
e_n.insert(0, "10000")
e_n.pack(side="left", padx=(0, 10))

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()
info = tk.Label(root, text="", font=("Consolas", 11), justify="left")
info.pack(pady=5)

st = {"after": None}

def draw_base(r, k):
    canvas.delete("all")

    def X(x):
        return C + x*k

    def Y(y):
        return C - y*k

    canvas.create_rectangle(X(-r), Y(r), X(r), Y(-r), outline="gray", dash=(4, 4))
    canvas.create_line(X(-r) - 20, Y(0), X(r) + 20, Y(0), arrow="last", width=2)
    canvas.create_line(X(0), Y(-r) + 20, X(0), Y(r) - 20, arrow="last", width=2)
    canvas.create_oval(X(-r), Y(r), X(r), Y(-r), outline="blue", width=2)
    canvas.create_line(X(-r), Y(0), X(0), Y(r), fill="blue", width=2)
    canvas.create_rectangle(X(0), Y(r), X(r), Y(0), outline="blue", width=2)
    canvas.create_rectangle(X(-r), Y(0), X(0), Y(-r), outline="blue", width=2)
    canvas.create_text(X(r), Y(0) + 12, text="R")
    canvas.create_text(X(-r), Y(0) + 12, text="-R")
    canvas.create_text(X(0) + 12, Y(r), text="R")
    canvas.create_text(X(0) + 14, Y(-r), text="-R")
    canvas.create_text(X(0) - 8, Y(0) + 10, text="0")

def step():
    r, k, n = st["r"], st["k"], st["n"]
    for _ in range(BATCH):
        if st["i"] >= n:
            break
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        hit = in_area(x, y, r)
        st["i"] += 1
        if hit:
            st["hits"] += 1
        px, py = C + x*k, C - y*k
        canvas.create_oval(px - 1.5, py - 1.5, px + 1.5, py + 1.5,
                           fill="green" if hit else "red", outline="")

    i, hits = st["i"], st["hits"]
    s_mc = 4*r*r * hits / i
    s_real = st["s_real"]
    ratio = s_mc / s_real * 100
    text = ("Испытаний: {0} из {1}, попаданий: {2}\n"
            "S (Монте-Карло) = {3:.4f}\n"
            "S (реальная)    = 1.5*R^2 = {4:.4f}\n"
            "Оценка = {5:.2f}% от реальной площади (отклонение {6:.2f}%)"
            ).format(i, n, hits, s_mc, s_real, ratio, abs(ratio - 100))
    info.config(text=text)

    if i < n:
        st["after"] = root.after(1, step)

def start():
    if st["after"] is not None:
        root.after_cancel(st["after"])
    try:
        r = float(e_r.get().replace(",", "."))
        n = int(e_n.get())
        if r <= 0 or not (1 <= n <= 10000):
            raise ValueError
    except ValueError:
        info.config(text="Введите R > 0 и целое N от 1 до 10000")
        return
    k = (C - MARGIN) / r
    draw_base(r, k)
    st.update(r=r, n=n, k=k, i=0, hits=0, s_real=1.5*r*r)
    step()

tk.Button(top, text="Запустить", command=start).pack(side="left")

start()
root.mainloop()
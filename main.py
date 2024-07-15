import tkinter as tk


def kys():
    print()


if __name__ == "__main__":
    print("chuj ci w dupe ")
    root = tk.Tk()
    frame = tk.Frame()
    kurwa = tk.Label(master=frame, text="kurwa zajebie sie chyba zaraz")
    japierdole = tk.Button(master=frame, text="no kurwa zrobie to")
    # frame = tk.Frame(root, bg="#0000ff")
    # frame.pack()
    # button = tk.Button(frame, bg="#ff0000", fg="#00ff00",
    #                    text="chuj ci w dupe")
    # button.place(frame)
    frame.pack()
    kurwa.pack()
    japierdole.pack()

    root.mainloop()

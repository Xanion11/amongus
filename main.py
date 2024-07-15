import tkinter as tk
import json


def kys():
    print()


rooms = {
    "Electrical": 0,
    "Specimen-room": 0,
    "Office": 0,
    "Laboratory": 0,
    "O2": 0,
    "Boiler": 0,
    "Admin": 0,
    "Storage": 0,
    "Security": 0,
    "Communications": 0,
    "Weapons": 0,
}
people_imp = {
    "Kacper": 0,
    "Krzysiek": 0,
    "Marcel": 0,
    "Wojtek": 0,
    "Mateusz": 0,
    "Michal": 0,
    "Piotrek": 0,
    "Gabrys": 0,
    "Olgierd": 0,
    "Patryk": 0,
}

people_killed = {
    "Kacper": 0,
    "Krzysiek": 0,
    "Marcel": 0,
    "Wojtek": 0,
    "Mateusz": 0,
    "Michal": 0,
    "Piotrek": 0,
    "Gabrys": 0,
    "Olgierd": 0,
    "Patryk": 0,
}


rounds = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
}
amount = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
}


data = {
    amount: {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
    },

    rounds: {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
    },
    people_killed: {
        "Kacper": 0,
        "Krzysiek": 0,
        "Marcel": 0,
        "Wojtek": 0,
        "Mateusz": 0,
        "Michal": 0,
        "Piotrek": 0,
        "Gabrys": 0,
        "Olgierd": 0,
        "Patryk": 0,
    },
    people_imp: {
        "Kacper": 0,
        "Krzysiek": 0,
        "Marcel": 0,
        "Wojtek": 0,
        "Mateusz": 0,
        "Michal": 0,
        "Piotrek": 0,
        "Gabrys": 0,
        "Olgierd": 0,
        "Patryk": 0,
    },
    rooms: {
        "Electrical": 0,
        "Specimen-room": 0,
        "Office": 0,
        "Laboratory": 0,
        "O2": 0,
        "Boiler": 0,
        "Admin": 0,
        "Storage": 0,
        "Security": 0,
        "Communications": 0,
        "Weapons": 0,
    }
}


print(json.dumps(people_imp, indent=4))

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

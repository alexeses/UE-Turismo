import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Agencia de Viajes")
title_label = tk.Label(root, text="Viajes de Senderismo")
title_label.pack()

root.geometry("600x500")
root.resizable(0, 0)

logo = tk.PhotoImage(file="logo100.png")
logo = logo.subsample(2, 2)
logo_label = tk.Label(root, image=logo)
logo_label.pack()

excursion_var = tk.StringVar()
excursion_var.set("Monte Abantos")

excursion1_radio = tk.Radiobutton(root, text="Monte Abantos", variable=excursion_var, value="Monte Abantos")
excursion2_radio = tk.Radiobutton(root, text="La Pedriza", variable=excursion_var, value="La Pedriza")
excursion3_radio = tk.Radiobutton(root, text="Las dehesas de Cercedilla", variable=excursion_var, value="Las dehesas de Cercedilla")
excursion4_radio = tk.Radiobutton(root, text="La Cabrera-Pico de la Miel", variable=excursion_var, value="La Cabrera-Pico de la Miel")

excursion1_radio.pack()
excursion2_radio.pack()
excursion3_radio.pack()
excursion4_radio.pack()


# Mochila,
# Linterna, GPS, Mapa, Prismáticos, Cantimplora, Botiquín y Crema Solar.

mochila_var = tk.BooleanVar()
linterna_var = tk.BooleanVar()
gps_var = tk.BooleanVar()
mapa_var = tk.BooleanVar()
prismáticos_var = tk.BooleanVar()
cantimplora_var = tk.BooleanVar()
botiquín_var = tk.BooleanVar()
crema_solar_var = tk.BooleanVar()



mochila_check = tk.Checkbutton(root, text="Mochila", variable=mochila_var)
linterna_check = tk.Checkbutton(root, text="Linterna", variable=linterna_var)

mochila_check.pack()
linterna_check.pack()

name_label = tk.Label(root, text="Nombre:")
name_entry = tk.Entry(root)

surname_label = tk.Label(root, text="Apellidos:")
surname_entry = tk.Entry(root)

address_label = tk.Label(root, text="Dirección:")
address_entry = tk.Entry(root)

phone_label = tk.Label(root, text="Teléfono:")
phone_entry = tk.Entry(root)

name_label.pack()
name_entry.pack()

surname_label.pack()
surname_entry.pack()

address_label.pack()
address_entry.pack()

phone_label.pack()
phone_entry.pack()

towns = ["Madrid", "Alcobendas"]
town_var = tk.StringVar()
town_var.set(towns[0])  # valor por defecto

town_combobox = tk.ttk.Combobox(root, textvariable=town_var, values=towns)
town_combobox.pack()

excursionists_listbox = tk.Listbox(root)
excursionists_listbox.pack()

def add_excursionist():
    name = name_entry.get()
    surname = surname_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    town = town_var.get()
    excursion = excursion_var.get()
    accessories = []
    if mochila_var.get():
        accessories.append("mochila")
    if linterna_var.get():
        accessories.append("linterna")
    accessories_str = ", ".join(accessories)

    excursionist = f"{name} {surname} ({town}) - {excursion} - {accessories_str}"
    excursionists_listbox.insert(tk.END, excursionist)

add_excursionist_button = tk.Button(root, text="Añadir Excursionista", command=add_excursionist)
add_excursionist_button.pack()

root.mainloop()



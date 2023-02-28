import tkinter as tk
from tkinter import ttk

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
    if gps_var.get():
        accessories.append("GPS")
    if mapa_var.get():
        accessories.append("mapa")
    if prismáticos_var.get():
        accessories.append("prismáticos")
    if cantimplora_var.get():
        accessories.append("cantimplora")
    if botiquín_var.get():
        accessories.append("botiquín")
    if crema_solar_var.get():
        accessories.append("crema solar")
    accessories_str = ", ".join(accessories)

    excursionist = f"{name} {surname} ({town}) - {excursion} - {accessories_str}"
    excursionists_listbox.insert(tk.END, excursionist)
    # Clear entries after adding excursionist
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Agencia de Viajes")

# Title and Logo
title_label = tk.Label(root, text="Viajes de Senderismo", font=("Arial", 20))
title_label.pack(pady=10)

logo = tk.PhotoImage(file="logo100.png").subsample(2, 2)
logo_label = tk.Label(root, image=logo)
logo_label.pack()

# Excursion Frame
excursion_var = tk.StringVar(value="Monte Abantos")
excursion_frame = tk.LabelFrame(root, text="Selecciona un monte")
excursion_frame.pack(side="left", padx=10, pady=10)

excursions = ["Monte Abantos", "La Pedriza", "Las dehesas de Cercedilla", "La Cabrera-Pico de la Miel"]
for excursion in excursions:
    excursion_radio = tk.Radiobutton(excursion_frame, text=excursion, variable=excursion_var, value=excursion, font=("Arial", 12))
    excursion_radio.pack(anchor="w", pady=5)

# Accessories Frame
accessories_frame = tk.LabelFrame(root, text="Selecciona los accesorios")
accessories_frame.pack(side="left", padx=10, pady=10)

mochila_var = tk.BooleanVar()
linterna_var = tk.BooleanVar()
gps_var = tk.BooleanVar()
mapa_var = tk.BooleanVar()
prismáticos_var = tk.BooleanVar()
cantimplora_var = tk.BooleanVar()
botiquín_var = tk.BooleanVar()
crema_solar_var = tk.BooleanVar()

mochila_check = tk.Checkbutton(accessories_frame, text="Mochila", variable=mochila_var, font=("Arial", 12))
linterna_check = tk.Checkbutton(accessories_frame, text="Linterna", variable=linterna_var, font=("Arial", 12))
gps_check = tk.Checkbutton(accessories_frame, text="GPS", variable=gps_var, font=("Arial", 12))
mapa_check = tk.Checkbutton(accessories_frame, text="Mapa", variable=mapa_var, font=("Arial", 12))
prismáticos_check = tk.Checkbutton(accessories_frame, text="Prismáticos", variable=prismáticos_var, font=("Arial", 12))
cantimplora_check = tk.Checkbutton(accessories_frame, text="Cantimplora", variable=cantimplora_var, font=("Arial", 12))
botiquín_check = tk.Checkbutton(accessories_frame, text="Botiquín", variable=botiquín_var, font=("Arial", 12))
crema_solar_check = tk.Checkbutton(accessories_frame, text="Crema solar", variable=crema_solar_var, font=("Arial", 12))

mochila_check.pack(anchor="w", pady=5)
linterna_check.pack(anchor="w", pady=5)
gps_check.pack(anchor="w", pady=5)
mapa_check.pack(anchor="w", pady=5)
prismáticos_check.pack(anchor="w", pady=5)
cantimplora_check.pack(anchor="w", pady=5)
botiquín_check.pack(anchor="w", pady=5)
crema_solar_check.pack(anchor="w", pady=5)

# Excursionists Frame
excursionists_frame = tk.LabelFrame(root, text="Excursionistas")
excursionists_frame.pack(padx=10, pady=10)

excursionists_listbox = tk.Listbox(excursionists_frame, width=50, height=20)
excursionists_listbox.pack()

# Excursionist Frame
excursionist_frame = tk.LabelFrame(root, text="Datos del excursionista")
excursionist_frame.pack(padx=10, pady=10)

name_label = tk.Label(excursionist_frame, text="Nombre", font=("Arial", 12))
surname_label = tk.Label(excursionist_frame, text="Apellidos", font=("Arial", 12))
address_label = tk.Label(excursionist_frame, text="Dirección", font=("Arial", 12))
phone_label = tk.Label(excursionist_frame, text="Teléfono", font=("Arial", 12))
town_label = tk.Label(excursionist_frame, text="Población", font=("Arial", 12))

name_entry = tk.Entry(excursionist_frame, width=30)
surname_entry = tk.Entry(excursionist_frame, width=30)
address_entry = tk.Entry(excursionist_frame, width=30)
phone_entry = tk.Entry(excursionist_frame, width=30)

town_var = tk.StringVar(value="Madrid")

name_label.grid(row=0, column=0, padx=5, pady=5)
surname_label.grid(row=1, column=0, padx=5, pady=5)
address_label.grid(row=2, column=0, padx=5, pady=5)
phone_label.grid(row=3, column=0, padx=5, pady=5)
town_label.grid(row=4, column=0, padx=5, pady=5)

town_var = tk.StringVar(value="Madrid")

name_entry = tk.Entry(excursionist_frame, width=40, font=("Arial", 12))
surname_entry = tk.Entry(excursionist_frame, width=40, font=("Arial", 12))
address_entry = tk.Entry(excursionist_frame, width=40, font=("Arial", 12))
phone_entry = tk.Entry(excursionist_frame, width=40, font=("Arial", 12))

town_menu = ttk.Combobox(excursionist_frame, width=37, textvariable=town_var, font=("Arial", 12), state="readonly")
town_menu['values'] = ('Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Málaga', 'Murcia', 'Palma', 'Las Palmas de Gran Canaria', 'Bilbao', 'Alicante', 'Córdoba', 'Valladolid', 'Vigo', 'Gijón', 'Hospitalet de Llobregat', 'A Coruña', 'Vitoria', 'Granada', 'Elche', 'Tarragona', 'Badalona', 'Oviedo', 'Cartagena', 'Terrassa', 'Jerez de la Frontera', 'Sabadell', 'Móstoles', 'Santa Cruz de Tenerife', 'Alcalá de Henares')
town_menu.current(0)

name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
surname_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
address_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
town_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
address_entry.grid(row=2, column=1, padx=5, pady=5)
phone_entry.grid(row=3, column=1, padx=5, pady=5)
town_menu.grid(row=4, column=1, padx=5, pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

add_button = tk.Button(buttons_frame, text="Añadir", font=("Arial", 12), command=add_excursionist)
add_button.pack(side="left", padx=5)

exit_button = tk.Button(buttons_frame, text="Salir", font=("Arial", 12), command=root.quit)
exit_button.pack(side="right", padx=5)

root.mainloop()
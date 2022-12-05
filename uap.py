# Restaurant Management System
# Author: Mohammad Ibnu
# Date: 05/12/2022
# Purpose: Ujian Akhir Praktikum Pemrograman Lanjut

# Import Library
import datetime
import gc
import os
import tkinter as tk
import locale
import csv
from tkinter import messagebox

header_data = ["Rincian", "Total Harga",
               "Uang Bayar", "Kembalian", "Tanggal"]
# make file if not exist and write header
if not os.path.exists("./data.csv"):
    with open("./data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header_data)


# testing variable
number = 0

# set locale to indonesia
locale.setlocale(locale.LC_ALL, 'id_ID')


def increase():
    global number
    number += 1
# class


class food:
    total = 0

    def __init__(self, name, price, order=0):
        self.name = name
        self.price = price
        self.order = order

    def add(self):
        self.order += 1
        self.total += self.price
        food.total += self.price

    def sub(self):
        self.order -= 1
        self.total -= self.price
        food.total -= self.price


# make object from class food
nasi = food("Nasi", 10000)
ayam_goreng = food("Ayam Goreng", 15000)
ayam_bakar = food("Ayam Bakar", 20000)
tahu_telur = food("Tahu Telur", 10000)
tahu = food("Tahu", 5000)
tempe = food("Tempe", 5000)
soto = food("Soto", 10000)

# Make window
window = tk.Tk()
window.title("Restaurant Management System")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="#091833")

# Set title
title = tk.Label(window, text="RESTAURANT MANAGEMENT SYSTEM",
                 font=("Arial", 18, 'bold'), anchor="center", fg="gold", bg="#091833")
title.grid(row=0, column=0, columnspan=10, pady=10)

# Set menu
menu = tk.Label(window, text="Menu - UAP Pemrograman Lanjut",
                font=("Arial", 15), bg="#091833", fg="white")
menu.grid(row=4, column=0, columnspan=10, pady=10)

# Set menu


def click_nasi(sub=False):
    if sub:
        if (nasi.order > 0):
            nasi.sub()
    else:
        nasi.add()
    label_order_nasi['text'] = str(nasi.order)
    label_price_total_nasi['text'] = "Rp." + str(nasi.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_nasi = tk.Label(
    window, text=f"{nasi.name} - Rp.{nasi.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_nasi.grid(row=5, column=0)
button_sub_nasi = tk.Button(window, text="-", command=lambda: click_nasi(True),
                            bg="#f2a343", fg="white", borderwidth=0)
button_sub_nasi.grid(row=5, column=1)
button_nasi = tk.Button(window, text="+", command=click_nasi,
                        bg="#f2a343", fg="white", borderwidth=0)
button_nasi.grid(row=5, column=2)

label_order_nasi = tk.Label(
    window, text=f"{nasi.order}", font=("Arial", 12, "bold"), bg="white")
label_order_nasi.grid(row=5, column=3)
label_price_total_nasi = tk.Label(
    window, text=f"Rp.{nasi.price * nasi.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_nasi.grid(row=5, column=4)


def click_ayam_goreng(sub=False):
    if sub:
        if (ayam_goreng.order > 0):
            ayam_goreng.sub()
    else:
        ayam_goreng.add()
    label_order_ayam_goreng['text'] = str(ayam_goreng.order)
    label_price_total_ayam_goreng['text'] = "Rp." + str(ayam_goreng.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_ayam_goreng = tk.Label(
    window, text=f"{ayam_goreng.name} - Rp.{ayam_goreng.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_ayam_goreng.grid(row=6, column=0)
button_sub_ayam_goreng = tk.Button(window, text="-", command=lambda: click_ayam_goreng(True),
                                   bg="#f2a343", fg="white", borderwidth=0)
button_sub_ayam_goreng.grid(row=6, column=1)
button_ayam_goreng = tk.Button(
    window, text="+", command=click_ayam_goreng, bg="#f2a343", fg="white", borderwidth=0)
button_ayam_goreng.grid(row=6, column=2)
label_order_ayam_goreng = tk.Label(
    window, text=f"{ayam_goreng.order}", font=("Arial", 12, "bold"), bg="white")
label_order_ayam_goreng.grid(row=6, column=3)
label_price_total_ayam_goreng = tk.Label(
    window, text=f"Rp.{nasi.order * nasi.price +ayam_goreng.price * ayam_goreng.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_ayam_goreng.grid(row=6, column=4)


def click_ayam_bakar(sub=False):
    if sub:
        if (ayam_bakar.order > 0):
            ayam_bakar.sub()
    else:
        ayam_bakar.add()
    label_order_ayam_bakar['text'] = str(ayam_bakar.order)
    label_price_total_ayam_bakar['text'] = "Rp." + str(ayam_bakar.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_ayam_bakar = tk.Label(
    window, text=f"{ayam_bakar.name} - Rp.{ayam_bakar.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_ayam_bakar.grid(row=7, column=0)
button_sub_ayam_bakar = tk.Button(window, text="-", command=lambda: click_ayam_bakar(True),
                                  bg="#f2a343", fg="white", borderwidth=0)
button_sub_ayam_bakar.grid(row=7, column=1)
button_ayam_bakar = tk.Button(
    window, text="+", command=click_ayam_bakar, bg="#f2a343", fg="white", borderwidth=0)
button_ayam_bakar.grid(row=7, column=2)
label_order_ayam_bakar = tk.Label(
    window, text=f"{ayam_bakar.order}", font=("Arial", 12, "bold"), bg="white")
label_order_ayam_bakar.grid(row=7, column=3)
label_price_total_ayam_bakar = tk.Label(
    window, text=f"Rp.{ayam_bakar.price * ayam_bakar.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_ayam_bakar.grid(row=7, column=4)


def click_tahu_telur(sub=False):
    if sub:
        if (tahu_telur.order > 0):
            tahu_telur.sub()
    else:
        tahu_telur.add()
    label_order_tahu_telur['text'] = str(tahu_telur.order)
    label_price_total_tahu_telur['text'] = "Rp." + \
        str(tahu_telur.price * tahu_telur.order)
    label_price_total_tahu_telur['text'] = "Rp." + str(tahu_telur.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_tahu_telur = tk.Label(
    window, text=f"{tahu_telur.name} - Rp.{tahu_telur.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_tahu_telur.grid(row=8, column=0)
button_sub_tahu_telur = tk.Button(window, text="-", command=lambda: click_tahu_telur(True),
                                  bg="#f2a343", fg="white", borderwidth=0)
button_sub_tahu_telur.grid(row=8, column=1)
button_tahu_telur = tk.Button(
    window, text="+", command=click_tahu_telur, bg="#f2a343", fg="white", borderwidth=0)
button_tahu_telur.grid(row=8, column=2)
label_order_tahu_telur = tk.Label(
    window, text=f"{tahu_telur.order}", font=("Arial", 12, "bold"), bg="white")
label_order_tahu_telur.grid(row=8, column=3)
label_price_total_tahu_telur = tk.Label(
    window, text=f"Rp.{tahu_telur.price * tahu_telur.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_tahu_telur.grid(row=8, column=4)


def click_tahu(sub=False):
    if sub:
        if (tahu.order > 0):
            tahu.sub()
    else:
        tahu.add()
    label_order_tahu['text'] = str(tahu.order)
    label_price_total_tahu['text'] = "Rp." + str(tahu.price * tahu.order)
    label_price_total_tahu['text'] = "Rp." + str(tahu.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_tahu = tk.Label(
    window, text=f"{tahu.name} - Rp.{tahu.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_tahu.grid(row=9, column=0)
button_sub_tahu = tk.Button(window, text="-", command=lambda: click_tahu(True),
                            bg="#f2a343", fg="white", borderwidth=0)
button_sub_tahu.grid(row=9, column=1)
button_tahu = tk.Button(window, text="+", command=click_tahu,
                        bg="#f2a343", fg="white", borderwidth=0)
button_tahu.grid(row=9, column=2)
label_order_tahu = tk.Label(
    window, text=f"{tahu.order}", font=("Arial", 12, "bold"), bg="white")
label_order_tahu.grid(row=9, column=3)
label_price_total_tahu = tk.Label(
    window, text=f"Rp.{tahu.price * tahu.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_tahu.grid(row=9, column=4)


def click_tempe(sub=False):
    if sub:
        if (tempe.order > 0):
            tempe.sub()
    else:
        tempe.add()
    label_order_tempe['text'] = str(tempe.order)
    label_price_total_tempe['text'] = "Rp." + str(tempe.total)
    label_total_price['text'] = locale.currency(food.total)
    price_entry = input_nominal_bayar.get()
    if price_entry == "":
        price_entry = 0
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(price_entry) - food.total
    )


label_tempe = tk.Label(
    window, text=f"{tempe.name} - Rp.{tempe.price}", bg="#091833", fg="white", font="Roboto 10 bold")
label_tempe.grid(row=10, column=0)
button_sub_tempe = tk.Button(window, text="-", command=lambda: click_tempe(True),
                             bg="#f2a343", fg="white", borderwidth=0)
button_sub_tempe.grid(row=10, column=1)
button_tempe = tk.Button(
    window, text="+", command=click_tempe, bg="#f2a343", fg="white", borderwidth=0)
button_tempe.grid(row=10, column=2)
label_order_tempe = tk.Label(
    window, text=f"{tempe.order}", font=("Arial", 12, "bold"), bg="white")
label_order_tempe.grid(row=10, column=3)
label_price_total_tempe = tk.Label(
    window, text=f"Rp.{tempe.price * tempe.order}", bg="#091833", fg="white", font="Roboto 10 bold")
label_price_total_tempe.grid(row=10, column=4)

label_total = tk.Label(window, text="Total", bg="#091833",
                       fg="white", font="Roboto 10 bold")
label_total.grid(row=11, column=0)
label_total_price = tk.Label(
    window, text=locale.currency(nasi.order * nasi.price + ayam_goreng.price * ayam_goreng.order + ayam_bakar.price * ayam_bakar.order + tahu_telur.price * tahu_telur.order + tahu.price * tahu.order + tempe.price * tempe.order), bg="#091833", fg="white", font="Roboto 10 bold")
label_total_price.grid(row=11, column=4)
label_nominal_bayar = tk.Label(
    window, text="Nominal Bayar", bg="#091833", fg="white", font="Roboto 10 bold")
label_nominal_bayar.grid(row=12, column=0)


def callback(sv):
    label_angka_nominal_kembalian['text'] = locale.currency(
        int(sv.get()) - food.total)


sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
input_nominal_bayar = tk.Entry(window, font=("Arial", 15), textvariable=sv)
input_nominal_bayar.grid(row=12, column=4)
label_nominal_kembalian = tk.Label(
    window, text="Nominal Kembalian", bg="#091833", fg="white", font="Roboto 10 bold")
label_nominal_kembalian.grid(row=13, column=0)
label_angka_nominal_kembalian = tk.Label(
    window, text=food.total, bg="#091833", fg="white", font="Roboto 10 bold")
label_angka_nominal_kembalian.grid(row=13, column=4)


def bayar():
    if food.total == 0:
        messagebox.showinfo("Error", "Belum ada pesanan")
        return
    if input_nominal_bayar.get() == "":
        messagebox.showinfo("Error", "Masukkan nominal bayar")
        return
    if int(input_nominal_bayar.get()) < food.total:
        messagebox.showinfo("Error", "Nominal bayar kurang")
        return
    messagebox.showinfo("Success", "Terima kasih sudah berbelanja")
    # save to csv
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        rincian = f"{nasi.name} x {nasi.order} = Rp.{nasi.total}, {ayam_goreng.name} x {ayam_goreng.order} = Rp.{ayam_goreng.total}, {ayam_bakar.name} x {ayam_bakar.order} = Rp.{ayam_bakar.total}, {tahu_telur.name} x {tahu_telur.order} = Rp.{tahu_telur.total}, {tahu.name} x {tahu.order} = Rp.{tahu.total}, {tempe.name} x {tempe.order} = Rp.{tempe.total}"
        writer.writerow([rincian, food.total, input_nominal_bayar.get(
        ), int(input_nominal_bayar.get()) - food.total, datetime.datetime.now()])
    # reset all input
    nasi.order = 0
    ayam_goreng.order = 0
    ayam_bakar.order = 0
    tahu_telur.order = 0
    tahu.order = 0
    tempe.order = 0
    label_order_nasi['text'] = str(nasi.order)
    label_order_ayam_goreng['text'] = str(ayam_goreng.order)
    label_order_ayam_bakar['text'] = str(ayam_bakar.order)
    label_order_tahu_telur['text'] = str(tahu_telur.order)
    label_order_tahu['text'] = str(tahu.order)
    label_order_tempe['text'] = str(tempe.order)
    label_price_total_nasi['text'] = "Rp." + str(nasi.price * nasi.order)
    label_price_total_ayam_goreng['text'] = "Rp." + \
        str(ayam_goreng.price * ayam_goreng.order)
    label_price_total_ayam_bakar['text'] = "Rp." + \
        str(ayam_bakar.price * ayam_bakar.order)
    label_price_total_tahu_telur['text'] = "Rp." + \
        str(tahu_telur.price * tahu_telur.order)
    label_price_total_tahu['text'] = "Rp." + str(tahu.price * tahu.order)
    label_price_total_tempe['text'] = "Rp." + str(tempe.price * tempe.order)
    food.total = 0
    label_total_price['text'] = locale.currency(food.total)
    input_nominal_bayar.delete(0, 'end')
    label_angka_nominal_kembalian['text'] = locale.currency(food.total)


button_bayar = tk.Button(window, text="BAYAR",
                         font=("Arial", 15, "bold"), command=bayar, bg="#f2a343", fg="white", borderwidth=0)
button_bayar.grid(row=14, column=3)

# loop window
window.mainloop()

import tkinter as tk
import random
from tkinter import messagebox

# Variabel global untuk menyimpan kotak yang aktif dan huruf yang dipilih
active_boxes = []
selected_letters = []

# Fungsi untuk mengaktifkan atau menonaktifkan kotak yang diklik
def toggle_box(event):
    global active_boxes, selected_letters
    box = event.widget
    
    # Jika kotak sudah aktif, nonaktifkan
    if box in active_boxes:
        box.config(bg="lightgrey")
        active_boxes.remove(box)
        selected_letters.remove(box.cget("text"))
    else:
        # Aktifkan kotak dan simpan hurufnya
        box.config(bg="lightblue")
        active_boxes.append(box)
        selected_letters.append(box.cget("text"))

# Fungsi untuk mengecek apakah huruf yang dipilih membentuk kata "API"
def check_word():
    # Sort huruf dan cek apakah berisi "A", "P", "I" secara lengkap
    if sorted(selected_letters) == ["A", "I", "P"]:
        messagebox.showinfo("Hasil", "Kata 'API' ditemukan!")
    else:
        messagebox.showinfo("Hasil", "Kata yang dipilih tidak membentuk 'API'.")

# Inisialisasi aplikasi tkinter
root = tk.Tk()
root.title("Aktivasi Kotak dengan Pengecekan Kata")

# Daftar huruf dan memilih tiga kotak untuk huruf "A", "P", dan "I"
letters = ["A", "P", "I"] + [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(2)]
random.shuffle(letters)

# Membuat kotak dengan huruf acak
for i in range(5):
    box = tk.Label(root, text=letters[i], bg="lightgrey", width=20, height=5)
    box.grid(row=i, column=0, padx=10, pady=10)

    # Menambahkan event binding
    box.bind("<Button-1>", toggle_box)  # Mengaktifkan atau menonaktifkan kotak saat diklik

# Menambahkan tombol untuk pengecekan
check_button = tk.Button(root, text="Cek Kata", command=check_word)
check_button.grid(row=5, column=0, pady=20)

# Menjalankan aplikasi
root.mainloop()

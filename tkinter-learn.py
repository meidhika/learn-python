import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("350x350")
window.resizable(False, False)
window.title("Belajar Tkinter")

# Variable Input
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Function
def tombol_click():
    ''''Fungsi ini akan dipanggil oleh tombol'''
    pesan= f"Halloo {NAMA_DEPAN.get()}{NAMA_BELAKANG.get()}, apa kabar?"
    showinfo(title="Whatsup!", message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, pady=10, fill="x", expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=10,fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang")
nama_belakang_label.pack(padx=10, pady=10, fill="x", expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, pady=10,fill="x", expand=True)

# 5. Tombol
sapa_button = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
sapa_button.pack(padx=10, pady=10, fill="x", expand=True)



window.mainloop()

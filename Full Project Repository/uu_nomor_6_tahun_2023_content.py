import re
import pandas as pd

# Baca isi file teks
with open("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_text/spelling_checker/uu_nomor_6_thn_2023_karakter1.txt", "r") as file:
    text = file.read()

# Proses teks untuk mendapatkan halaman dan konteks
matches = re.findall(r"PRESIDEN REPUBLIK INDONESIA -(\d+)&&\n(.*?)\n(?=PRESIDEN REPUBLIK INDONESIA|\Z)", text, re.DOTALL)

# Inisialisasi list untuk menyimpan data
data = []

# Memproses setiap pasangan halaman dan konten
for page, content in matches:
    # Mencari kalimat-kalimat yang dimulai dan diakhiri dengan tanda $
    sentences = re.findall(r'\$(.*?)\$', content, re.DOTALL)
    # Menambahkan setiap kalimat ke dalam list data dengan halaman yang sesuai
    for sentence in sentences:
        data.append((int(page), sentence.strip()))

# Membuat DataFrame dari list of tuples
df = pd.DataFrame(data, columns=['halaman', 'content'])

# Tampilkan dataframe
print(df)

# Simpan dataframe ke file Excel
df.to_excel("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_table/tabular/uu_nomor_6_tahun_2023_content.xlsx", index=False)

import re
import pandas as pd

# Baca isi file teks
with open("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_text/spelling_checker/uu_nomor_6_thn_2023_karakter1.txt", "r") as file:
    text = file.read()

# Proses teks untuk mendapatkan halaman dan konteks
matches = re.findall(r"PRESIDEN REPUBLIK INDONESIA -(\d+)&&\n(.*?)\n(?=PRESIDEN REPUBLIK INDONESIA|\Z)", text, re.DOTALL)

# Susun data menjadi tabel
data = []
for match in matches:
    page = match[0]
    contexts = re.findall(r"(BAB|Bagian|Pasal|Ayat)~\s*!(\w+)", match[1])
    for context in contexts:
        data.append((page, context[0], context[1]))
    #else:
        #data.append((page, "(NULL)", "(NULL)"))

# Buat dataframe menggunakan pandas
df = pd.DataFrame(data, columns=["halaman", "context", "context_number"])

# Hapus karakter && dan ~ dari kolom halaman dan context
df['halaman'] = df['halaman'].str.replace("&", "")
df['context'] = df['context'].str.replace("~", "")
df['context_number'] = df['context_number'].str.replace("!", "")

# Tampilkan dataframe
print(df)

# Simpan dataframe ke file Excel
df.to_excel("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_table/tabular/uu_nomor_6_thn_2023_context.xlsx", index=False)

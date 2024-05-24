## Deskripsi Teknis Project Data Preparation Script UU Ketenagakerjaan

[CLICK HERE FOR END RESULT]()
### Tujuan Project
Project ini bertujuan untuk membuat skrip persiapan data untuk dokumen UU Indonesia tentang ketenagakerjaan. Proses ini melibatkan parsing PDF menjadi teks dan kemudian mengonversi teks tersebut ke dalam bentuk tabel, lalu dikembangkan dengan manipulation script. Skrip ini dirancang untuk mengatasi kendala teknis yang ditemukan selama pengembangan, dan pemisahan antara konteks dan konten terbukti menjadi solusi yang efektif.

### Skrip Parsing PDF ke Teks
Skrip ini bertugas untuk mengonversi dokumen PDF menjadi teks dengan format yang mudah diolah lebih lanjut. Berikut adalah penjelasan teknis dari fungsi utama yang digunakan:

#### `pdf to text .py`
- **fitz**: Digunakan untuk membuka dan membaca dokumen PDF.
- **re**: Digunakan untuk manipulasi string dan pola teks.
- **format_text_with_line_breaks(pdf_path)**: Fungsi ini membuka dokumen PDF, mengekstrak teks dari setiap halaman, dan memformat teks tersebut dengan menambahkan jeda baris setelah setiap poin.

```python
import fitz 
import re

def format_text_with_line_breaks(pdf_path):
    doc = fitz.open(pdf_path)
    formatted_text = ""
    for page in doc:
        text = page.get_text()
        text = text.replace('-\\n', '')  
        text = ' '.join(text.split()) 
        text = re.sub(r'([a-z])\\.\\s', r'\\1.\\n', text)  
        formatted_text += text + "\\n\\n"
    return formatted_text

pdf_path_with_breaks = "C://Users//Ajeng//Documents//Project Intern Xeratic//UU Nomor 13 Tahun 2003.pdf"
text_with_breaks = format_text_with_line_breaks(pdf_path_with_breaks)
output_with_breaks_path = "C://Users//Ajeng//Documents//Project Intern Xeratic//output script uud no 13.txt"
with open(output_with_breaks_path, "w") as file:
    file.write(text_with_breaks)

```

### Proses Parsing Teks ke Tabel

Dalam proyek ini, kami memanfaatkan dua file utama untuk membantu dalam proses parsing teks ke tabel: `context parsing.py` dan `content parsing.py`. [Karakterisasi teks UU 13 tahun 2003](https://github.com/jfzr99/Intern-Project/blob/main/Full%20Project%20Repository/uu_nomor_13_tahun_2003_karakter.txt) dan [Karakterisasi teks UU no 6 tahun 2023](https://github.com/jfzr99/Intern-Project/blob/main/Full%20Project%20Repository/uu_nomor_6_thn_2023_karakter1.txt)menggunakan karakter khusus untuk memudahkan pendeteksian variabel yang diperlukan saat parsing dari teks ke tabel PDF.

#### Karakter Khusus yang Digunakan:
- **Halaman:** ditandai dengan `&&`
- **Context:** ditandai dengan tanda `~` di akhir kata
  - Jenis Context: Judul, Pembuka, Penetapan, Pengingat, Persetujuan, Pertimbangan, BAB, Bagian, Pasal, Ayat
- **Context_numbering:** ditandai dengan `!` sebelum kata atau angka
  - Angka BAB
  - Angka Bagian
  - Angka Pasal
  - Angka Ayat
- **Content:** ditandai dengan diawali dan diakhiri tanda `$`
  - Isi Bab, Isi Bagian, Isi Pasal, Isi Ayat

### Skrip Parsing Konteks
#### `context parsing.py`
Skrip ini berfungsi untuk mengekstrak konteks dari teks yang telah diparsing untuk membuat tabel yang berisi informasi tentang bab, bagian, pasal, dan ayat. Berikut adalah contoh implementasi dan deskripsi teknisnya:

```python
import re
import pandas as pd

# Baca isi file teks
with open("user\patht", "r") as file:
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

# Buat dataframe menggunakan pandas
df = pd.DataFrame(data, columns=['halaman', 'context', 'context_number'])
df['halaman'] = df['halaman'].str.replace("&", "")
df['context'] = df['context'].str.replace("~", "")
df['context_number'] = df['context_number'].str.replace("!", "")

# Tampilkan dataframe
print(df)

# Simpan dataframe ke file Excel
df.to_excel("user\path", index=False)
```

### Skrip Parsing Konten
#### `content parsing.py`
Skrip ini memproses teks yang telah dihasilkan dari PDF untuk mengekstrak dan mengorganisir konten ke dalam bentuk tabel. Berikut adalah contoh implementasi dan deskripsi teknisnya:

```python
import re
import pandas as pd

# Baca isi file teks
with open("\user\path", "r") as file:
    text = file.read()

# Proses teks untuk mendapatkan halaman dan konten
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
df.to_excel("\user\path", index=False)
```

Dengan menggunakan tanda-tanda khusus ini, proses parsing teks ke tabel menjadi lebih terstruktur dan mudah untuk diolah, memungkinkan ekstraksi data yang akurat dan efisien dari dokumen PDF ke format tabel yang dapat digunakan untuk analisis lebih lanjut.
### Alasan Pemisahan Konteks dan Konten
Pemisahan antara konteks dan konten dilakukan untuk mengatasi kendala teknis yang ditemukan selama pengembangan. Pemisahan ini memungkinkan pengolahan data yang lebih efisien dan terstruktur, sehingga memudahkan dalam proses ekstraksi dan analisis data.


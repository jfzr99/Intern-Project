## Deskripsi Teknis Proyek

### Tujuan Proyek
Proyek ini bertujuan untuk membuat skrip persiapan data untuk dokumen UU Indonesia tentang ketenagakerjaan. Proses ini melibatkan parsing PDF menjadi teks dan kemudian mengonversi teks tersebut ke dalam bentuk tabel, lalu dikembangkan dengan manipulation script. Skrip ini dirancang untuk mengatasi kendala teknis yang ditemukan selama pengembangan, dan pemisahan antara konteks dan konten terbukti menjadi solusi yang efektif.

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

### Skrip Parsing Konten
Skrip ini memproses teks yang telah dihasilkan dari PDF untuk mengekstrak dan mengorganisir konten ke dalam bentuk tabel.

#### `content parsing.py`
- **re**: Digunakan untuk menemukan dan memanipulasi pola dalam teks.
- **pandas**: Digunakan untuk membuat dan mengolah DataFrame.
- **Proses Utama**:
  - Membaca isi file teks.
  - Memproses teks untuk mendapatkan halaman dan konten.
  - Mengekstraksi kalimat yang dimulai dan diakhiri dengan tanda `$`.
  - Membuat DataFrame dan menyimpan hasilnya ke dalam file Excel.

```python
import re
import pandas as pd

with open("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_text/spelling_checker/uu_nomor_13_tahun_2003_karakter.txt", "r") as file:
    text = file.read()

matches = re.findall(r"PRESIDEN REPUBLIK INDONESIA -(\\d+)&&\\n(.*?)\\n(?=PRESIDEN REPUBLIK INDONESIA|\\Z)", text, re.DOTALL)
data = []

for page, content in matches:
    sentences = re.findall(r'\\$(.*?)\\$', content, re.DOTALL)
    for sentence in sentences:
        data.append((int(page), sentence.strip()))

df = pd.DataFrame(data, columns=['halaman', 'content'])
df.to_excel("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_table/tabular/uu_nomor_13_tahun_2003_content.xlsx", index=False)
```

### Skrip Parsing Konteks
Skrip ini berfungsi untuk mengekstrak konteks dari teks yang telah diparsing untuk membuat tabel yang berisi informasi tentang bab, bagian, pasal, dan ayat.

#### `context parsing.py`
- **re**: Digunakan untuk menemukan pola dalam teks.
- **pandas**: Digunakan untuk membuat dan mengolah DataFrame.
- **Proses Utama**:
  - Membaca isi file teks.
  - Memproses teks untuk mendapatkan halaman dan konteks.
  - Mengekstraksi informasi tentang bab, bagian, pasal, dan ayat.
  - Membuat DataFrame dan menyimpan hasilnya ke dalam file Excel.

```python
import re
import pandas as pd

with open("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_text/spelling_checker/uu_nomor_6_thn_2023_karakter1.txt", "r") as file:
    text = file.read()

matches = re.findall(r"PRESIDEN REPUBLIK INDONESIA -(\\d+)&&\\n(.*?)\\n(?=PRESIDEN REPUBLIK INDONESIA|\\Z)", text, re.DOTALL)
data = []
for match in matches:
    page = match[0]
    contexts = re.findall(r"(BAB|Bagian|Pasal|Ayat)~\\s*!(\\w+)", match[1])
    for context in contexts:
        data.append((page, context[0], context[1]))

df = pd.DataFrame(data, columns=['halaman', 'context', 'context_number'])
df['halaman'] = df['halaman'].str.replace("&", "")
df['context'] = df['context'].str.replace("~", "")
df['context_number'] = df['context_number'].str.replace("!", "")
df.to_excel("D:/LAPTOP/Documents/Tetris Program/Materi Tetris Program/Internship/data_table/tabular/uu_nomor_6_thn_2023_context.xlsx", index=False)
```

### Alasan Pemisahan Konteks dan Konten
Pemisahan antara konteks dan konten dilakukan untuk mengatasi kendala teknis yang ditemukan selama pengembangan. Pemisahan ini memungkinkan pengolahan data yang lebih efisien dan terstruktur, sehingga memudahkan dalam proses ekstraksi dan analisis data.

---

Dengan deskripsi ini, Anda dapat menjelaskan secara komprehensif bagaimana skrip ini bekerja dan alasan di balik pemisahan antara konteks dan konten dalam proyek Anda.

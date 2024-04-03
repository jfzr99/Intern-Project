import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Text has been saved to {file_path}")

# Specify the path to your PDF
pdf_path = 'C://Users//Ajeng//Documents//Project Intern Xeratic//UU Nomor 13 Tahun 2003.pdf'
output_path = 'C://Users//Ajeng//Documents//Project Intern Xeratic//UU Nomor 13 Tahun 2003.txt'

# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a file
save_text_to_file(text, output_path)

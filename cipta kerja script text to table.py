import re
import pandas as pd


# Load the text data
with open('C://Users//Ajeng//Documents//Project Intern Xeratic//cleaned script for cipta kerja.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

# Define patterns to extract data
pasal_pattern = re.compile(r'(Pasal \d+)[^\n]*(\n\d+\.\s*(.*?)\n)(Pasal \d+|$)', re.DOTALL)
ayat_pattern = re.compile(r'(\(\d+\))([^(\(]*?)\n', re.DOTALL)

# Create structured data
data = []
content_id = 1
for pasal_match in pasal_pattern.finditer(text_data):
    pasal_text = pasal_match.group(1)
    pasal_content = pasal_match.group(3).strip()
    pasal_number = int(re.search(r'\d+', pasal_text).group(0))
    hierarchy_text_code = f"pasal_{pasal_number}"

    # Add the pasal entry
    data.append({
        "content_id": content_id,
        "document_id": "uu_no_6_2013",
        "context": "pasal",
        "context_number": pasal_number,
        "hierarchy_number": "",
        "content": pasal_content,
        "hierarchy_text_code": hierarchy_text_code,
        "halaman": pasal_match.start()
    })
    content_id += 1

    # Add ayat entries under the pasal
    for ayat_match in ayat_pattern.finditer(pasal_content):
        ayat_text = ayat_match.group(1).strip()
        ayat_content = ayat_match.group(2).strip()
        ayat_number = int(re.search(r'\d+', ayat_text).group(0))
        hierarchy_text_code_ayat = f"{hierarchy_text_code}_ayat_{ayat_number}"

        data.append({
            "content_id": content_id,
            "document_id": "uu_no_6_2013",
            "context": "ayat",
            "context_number": ayat_number,
            "hierarchy_number": ayat_text,
            "content": ayat_content,
            "hierarchy_text_code": hierarchy_text_code_ayat,
            "halaman": pasal_match.start()  # Simplification, page detection not implemented
        })
        content_id += 1

# Convert to DataFrame
parsed_data = pd.DataFrame(data)
parsed_data.head()

output_file_path = 'C://Users//Ajeng//Documents//Project Intern Xeratic//table_output.xlsx'
parsed_data.to_excel(output_file_path, index=False)

output_file_path


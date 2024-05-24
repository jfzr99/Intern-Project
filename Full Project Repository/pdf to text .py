# Revised function to format the text with line breaks after each point
import fitz 
import re
def format_text_with_line_breaks(pdf_path):
    doc = fitz.open(pdf_path)
    formatted_text = ""
    for page in doc:
        # Extract text
        text = page.get_text()
        
        # Initial cleanup to remove hyphens and extra spaces
        text = text.replace('-\n', '')  # Remove hyphenation at the end of lines
        text = ' '.join(text.split())  # Remove additional spaces

        # Apply formatting rules with line breaks after each point
        text = re.sub(r'([a-z])\.\s', r'\1. ', text)  # Ensure points are in the same paragraph
        text = re.sub(r'([a-z])\.\s', r'\1.\n', text)  # Add line break after each point

        # Concatenate formatted text from each page
        formatted_text += text + "\n\n"  # Double line break between pages
        
    return formatted_text

# Path to the PDF document
pdf_path_with_breaks = "C://Users//Ajeng//Documents//Project Intern Xeratic//UU Nomor 13 Tahun 2003.pdf"

# Format the text from the PDF with line breaks after each point
text_with_breaks = format_text_with_line_breaks(pdf_path_with_breaks)

# Save the formatted text to a new file with line breaks
output_with_breaks_path = "C://Users//Ajeng//Documents//Project Intern Xeratic//output script uud no 13.txt"
with open(output_with_breaks_path, "w") as file:
    file.write(text_with_breaks)

output_with_breaks_path

import pandas as pd
import re

def text_to_dataframe(text):
    # Regular expression to extract "Pasal" numbers and their content.
    # This pattern needs to be adjusted based on the actual format of your document.
    pattern = re.compile(r'Pasal (\d+)\s*(.*?)\n(.*?)\n', re.DOTALL)
    
    # Find all matches of the pattern in the text
    matches = pattern.findall(text)
    
    # Create a list to hold our extracted data
    data = []
    
    # Process each match
    for match in matches:
        pasal_number = match[0]
        # Attempt to split the subject from the content at the first period, assuming it ends the first sentence.
        split_content = match[2].split('.', 1)
        subjek = split_content[0].strip()
        isi_pasal = split_content[1].strip() if len(split_content) > 1 else ""
        
        # Append a tuple with our extracted data
        data.append((pasal_number, subjek, isi_pasal))
    
    # Convert the list of tuples into a pandas DataFrame
    df = pd.DataFrame(data, columns=['Pasal', 'Subjek', 'Isi Pasal'])
    
    return df

# Assuming `text` is the cleaned text from the PDF
# Here, replace 'text' with the actual variable containing your text, or read it from the saved file
df_articles = text_to_dataframe(text)

# Save the DataFrame to an Excel file
df_articles.to_excel('articles_table.xlsx', index=False)

print("Data has been saved to 'articles_table.xlsx'")



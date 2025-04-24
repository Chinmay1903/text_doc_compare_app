import fitz  # PyMuPDF

def extract_pdf_text(file):
    file.seek(0)
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_file(file):
    if file.name.endswith('.pdf'):
        return extract_pdf_text(file)
    else:
        file.seek(0)
        return file.read().decode('utf-8', errors='ignore')

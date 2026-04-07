from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF using pypdf"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def validate_pdf(pdf_path: str) -> bool:
    """Validate PDF file"""
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError("Only PDF files are supported")

    import os
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    return True

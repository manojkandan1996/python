import cv2
import pytesseract
import re
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_receipt_data(image_path):
    img = cv2.imread(image_path)
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return
    
    if img is None:
        print("❌ Error: Could not load image. Check the file path.")
        return
    

    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(thresh)

    store = re.search(r'(Walmart|Target|Reliance|Big Bazaar)', text, re.IGNORECASE)
    date = re.search(r'\d{2}/\d{2}/\d{4}', text)
    total = re.search(r'Total\s*[:\-]?\s*\₹?\s*(\d+\.\d{2})', text, re.IGNORECASE)

    print("===== Parsed Receipt =====")
    print(f"Store: {store.group(0) if store else 'Not found'}")
    print(f"Date: {date.group(0) if date else 'Not found'}")
    print(f"Total: ₹{total.group(1) if total else 'Not found'}")
    print("\nRaw Text:\n", text)

# Example usage
extract_receipt_data(r"C:\Users\DELL\OneDrive\Desktop\Python class\Python\Extra Project\15 Projects-4Batch\2-Financial and Utility Tools\5-Expense Receipt Parser\sample_receipt.jpg")
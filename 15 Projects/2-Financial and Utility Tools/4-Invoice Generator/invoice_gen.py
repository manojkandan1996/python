from reportlab.pdfgen import canvas
from datetime import datetime

def generate_invoice(client_name, items, filename="invoice.pdf"):
    c = canvas.Canvas(filename, pagesize=(595, 842))  # A4 size in points
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Client: {client_name}")
    c.drawString(50, 765, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    c.drawString(50, 740, "Items:")
    y = 720
    total = 0
    for item, price in items:
        c.drawString(60, y, f"{item}")
        c.drawRightString(500, y, f"₹{price:.2f}")
        total += price
        y -= 20

    c.line(50, y, 500, y)
    c.drawString(60, y - 20, "Total:")
    c.drawRightString(500, y - 20, f"₹{total:.2f}")

    c.save()
    print(f"✅ Invoice saved as {filename}")

# Example usage
items = [("Web Design", 15000), ("Hosting", 2000), ("Maintenance", 3000)]
generate_invoice("Acme Corp", items, "invoice_acme.pdf")
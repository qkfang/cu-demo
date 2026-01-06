"""
Script to generate sample documents for testing Azure Content Understanding service.
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_pdfs():
    """Create sample PDF documents."""
    output_dir = "sample_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # Sample PDF 1: Simple invoice
    pdf_path_1 = os.path.join(output_dir, "sample_invoice.pdf")
    c = canvas.Canvas(pdf_path_1, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height - 1*inch, "INVOICE")
    
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.5*inch, "Invoice #: INV-2024-001")
    c.drawString(1*inch, height - 1.8*inch, "Date: January 6, 2024")
    c.drawString(1*inch, height - 2.1*inch, "Customer: ABC Corporation")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, height - 2.7*inch, "Items:")
    
    c.setFont("Helvetica", 11)
    c.drawString(1*inch, height - 3*inch, "1. Cloud Services - $500.00")
    c.drawString(1*inch, height - 3.3*inch, "2. Support Package - $200.00")
    c.drawString(1*inch, height - 3.6*inch, "3. Training Session - $300.00")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, height - 4*inch, "Total: $1,000.00")
    
    c.save()
    print(f"Created: {pdf_path_1}")
    
    # Sample PDF 2: Receipt
    pdf_path_2 = os.path.join(output_dir, "sample_receipt.pdf")
    c = canvas.Canvas(pdf_path_2, pagesize=letter)
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height - 1*inch, "RECEIPT")
    
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.5*inch, "Store: Tech Mart")
    c.drawString(1*inch, height - 1.8*inch, "Date: January 5, 2024")
    c.drawString(1*inch, height - 2.1*inch, "Transaction ID: TXN-456789")
    
    c.setFont("Helvetica", 11)
    c.drawString(1*inch, height - 2.7*inch, "Laptop Computer - $1,299.99")
    c.drawString(1*inch, height - 3*inch, "Wireless Mouse - $29.99")
    c.drawString(1*inch, height - 3.3*inch, "USB Cable - $9.99")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, height - 3.8*inch, "Subtotal: $1,339.97")
    c.drawString(1*inch, height - 4.1*inch, "Tax: $107.20")
    c.drawString(1*inch, height - 4.4*inch, "Total: $1,447.17")
    
    c.save()
    print(f"Created: {pdf_path_2}")

def create_sample_images():
    """Create sample images with text."""
    output_dir = "sample_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # Sample Image 1: Business card
    img_path_1 = os.path.join(output_dir, "business_card.png")
    img1 = Image.new('RGB', (600, 350), color='white')
    draw1 = ImageDraw.Draw(img1)
    
    # Draw border
    draw1.rectangle([(10, 10), (590, 340)], outline='black', width=2)
    
    # Add text
    try:
        # Try to use a default font, fallback to basic if not available
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    draw1.text((50, 50), "John Smith", fill='black', font=font_large)
    draw1.text((50, 90), "Software Engineer", fill='gray', font=font_medium)
    draw1.text((50, 150), "Email: john.smith@example.com", fill='black', font=font_small)
    draw1.text((50, 180), "Phone: +1 (555) 123-4567", fill='black', font=font_small)
    draw1.text((50, 210), "Company: Tech Solutions Inc.", fill='black', font=font_small)
    
    img1.save(img_path_1)
    print(f"Created: {img_path_1}")
    
    # Sample Image 2: Sign with text
    img_path_2 = os.path.join(output_dir, "sign_text.png")
    img2 = Image.new('RGB', (800, 400), color='lightblue')
    draw2 = ImageDraw.Draw(img2)
    
    draw2.text((100, 100), "PARKING", fill='black', font=font_large)
    draw2.text((100, 150), "Customer Only", fill='black', font=font_medium)
    draw2.text((100, 200), "No Parking 8PM - 6AM", fill='darkred', font=font_medium)
    draw2.text((100, 250), "Violators will be towed", fill='black', font=font_small)
    
    img2.save(img_path_2)
    print(f"Created: {img_path_2}")

if __name__ == "__main__":
    print("Generating sample documents...")
    create_sample_pdfs()
    create_sample_images()
    print("Sample documents created successfully!")

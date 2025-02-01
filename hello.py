from fpdf import FPDF

def sanitize_text(text):
    """Replace non-latin1 characters with ASCII equivalents."""
    return text.encode("latin-1", "ignore").decode("latin-1")

def main():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    # Title
    pdf.cell(190, 10, sanitize_text("Invoice"), ln=True, align="C")
    pdf.ln(10)

    # From Details
    pdf.set_font("Arial", "", 12)
    pdf.cell(100, 8, sanitize_text("From:"), ln=True)
    pdf.cell(100, 8, sanitize_text("Abraham Jesulayomi Olaobaju"), ln=True)
    pdf.cell(100, 8, sanitize_text("Edinburgh, Scotland, UK"), ln=True)
    pdf.cell(100, 8, sanitize_text("Email: [your email]"), ln=True)
    pdf.cell(100, 8, sanitize_text("Phone: [your phone number]"), ln=True)
    pdf.ln(5)

    # To Details
    pdf.cell(100, 8, sanitize_text("To:"), ln=True)
    pdf.cell(100, 8, sanitize_text("[Client’s Name]"), ln=True)
    pdf.cell(100, 8, sanitize_text("[Client’s Address]"), ln=True)
    pdf.cell(100, 8, sanitize_text("Email: [Client’s Email]"), ln=True)
    pdf.ln(5)

    # Invoice Details
    pdf.cell(100, 8, sanitize_text("Invoice Number: INV-20240201"), ln=True)
    pdf.cell(100, 8, sanitize_text("Invoice Date: 01-Feb-2025"), ln=True)
    pdf.cell(100, 8, sanitize_text("Due Date: 15-Feb-2025"), ln=True)
    pdf.ln(10)

    # Service Description Table
    pdf.set_font("Arial", "B", 12)
    pdf.cell(100, 8, sanitize_text("Description"), border=1)
    pdf.cell(40, 8, sanitize_text("Quantity"), border=1)
    pdf.cell(50, 8, sanitize_text("Total"), border=1, ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(100, 8, sanitize_text("[Service Description]"), border=1)
    pdf.cell(40, 8, sanitize_text("1"), border=1)
    pdf.cell(50, 8, sanitize_text("£1000.00"), border=1, ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(140, 8, sanitize_text("Total Amount Due:"), border=0)
    pdf.cell(50, 8, sanitize_text("£1000.00"), border=0, ln=True)

    pdf.ln(10)

    # Payment Details
    pdf.set_font("Arial", "", 12)
    pdf.cell(100, 8, sanitize_text("Payment Details:"), ln=True)
    pdf.cell(100, 8, sanitize_text("Bank Name: [Your Bank Name]"), ln=True)
    pdf.cell(100, 8, sanitize_text("Sort Code: [Your Sort Code]"), ln=True)
    pdf.cell(100, 8, sanitize_text("Account Number: [Your Account Number]"), ln=True)
    pdf.cell(100, 8, sanitize_text("Payment Reference: INV-20240201"), ln=True)

    # Save PDF
    pdf.output("invoice.pdf")


if __name__ == "__main__":
    main()

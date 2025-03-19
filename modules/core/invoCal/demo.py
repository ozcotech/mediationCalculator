from .calculator import InvoiceCalculator, CalculationOption

def demo_run():
    """Run a simple demo for invoice calculation."""
    print("Demo çalışıyor...")
    
    # Example inputs
    mediation_fee = 100000  # Example fee
    option = CalculationOption.KDV_STOPAJ_DAHIL.value  # Example calculation type

    print(f"\nDemo: {mediation_fee} ₺ için hesaplama yapılmaktadır. Seçenek: {option}")
    
    # Create an instance of InvoiceCalculator
    invoice = InvoiceCalculator(mediation_fee, option)
    
    # Print the calculation results
    invoice.print_table()

if __name__ == "__main__":
    demo_run()

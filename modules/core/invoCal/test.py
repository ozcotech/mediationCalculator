import unittest
from .calculator import InvoiceCalculator, CalculationOption

class TestInvoiceCalculator(unittest.TestCase):
    """Unit tests for InvoiceCalculator."""

    def test_kdv_stopaj_dahil(self):
        """Tests the calculation when both VAT and withholding tax are included in the total."""
        """Test KDV ve Stopaj Dahil hesaplaması."""
        calculator = InvoiceCalculator(100000, CalculationOption.KDV_STOPAJ_DAHIL.value)
        self.assertAlmostEqual(calculator.result["Brüt (KDV Hariç)"][0], 83333.33, places=2)
        self.assertAlmostEqual(calculator.result["Gelir Vergisi Stopajı (%20)"][0], 16666.67, places=2)
        self.assertAlmostEqual(calculator.result["KDV (%20)"][0], 16666.67, places=2)

    def test_kdv_dahil_stopaj_haric(self):
        """Tests the calculation when only VAT is included and withholding tax is excluded."""
        """Test KDV Dahil, Stopaj Hariç hesaplaması."""
        calculator = InvoiceCalculator(100000, CalculationOption.KDV_DAHIL_STOPAJ_HARIC.value)
        self.assertAlmostEqual(calculator.result["Brüt (KDV Hariç)"][0], 100000.00, places=2)
        self.assertAlmostEqual(calculator.result["KDV (%20)"][0], 20000.00, places=2)

    def test_kdv_ve_stopaj_haric(self):
        """Tests the calculation when both VAT and withholding tax are excluded from the total."""
        """Test KDV ve Stopaj Hariç hesaplaması."""
        calculator = InvoiceCalculator(100000, CalculationOption.KDV_STOPAJ_HARIC.value)
        self.assertAlmostEqual(calculator.result["Brüt (KDV Hariç)"][0], 125000.00, places=2)
        self.assertAlmostEqual(calculator.result["KDV (%20)"][0], 25000.00, places=2)

    def test_kdv_haric_stopaj_dahil(self):
        """Tests the calculation when VAT is excluded and withholding tax is included."""
        """Test KDV Hariç, Stopaj Dahil hesaplaması."""
        calculator = InvoiceCalculator(100000, CalculationOption.KDV_HARIC_STOPAJ_DAHIL.value)
        self.assertAlmostEqual(calculator.result["Brüt (KDV Hariç)"][0], 100000.00, places=2)
        self.assertAlmostEqual(calculator.result["KDV (%20)"][0], 20000.00, places=2)

if __name__ == "__main__":
    unittest.main()

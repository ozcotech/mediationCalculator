from enum import Enum

class CalculationOption(Enum):
    """Enum for calculation options to improve code readability."""
    KDV_STOPAJ_DAHIL = 1
    KDV_DAHIL_STOPAJ_HARIC = 2
    KDV_STOPAJ_HARIC = 3
    KDV_HARIC_STOPAJ_DAHIL = 4

class InvoiceCalculator:
    """Class for calculating the professional invoice for mediation fees."""
    
    TAX_RATE = 0.20  # 20% VAT and Withholding Tax Rate

    def __init__(self, mediation_fee, option):
        self.mediation_fee = mediation_fee
        self.option = option
        self.result = {}
        self.calculate()

    def calculate(self):
        """Determines which calculation method to use based on the selected option."""
        if self.option == CalculationOption.KDV_STOPAJ_DAHIL.value:
            self.result = self.calculate_kdv_stopaj_dahil()
        elif self.option == CalculationOption.KDV_DAHIL_STOPAJ_HARIC.value:
            self.result = self.calculate_kdv_dahil_stopaj_haric()
        elif self.option == CalculationOption.KDV_STOPAJ_HARIC.value:
            self.result = self.calculate_kdv_ve_stopaj_haric()
        elif self.option == CalculationOption.KDV_HARIC_STOPAJ_DAHIL.value:
            self.result = self.calculate_kdv_haric_stopaj_dahil()
        else:
            raise ValueError("Geçersiz seçenek!")

    def calculate_kdv_stopaj_dahil(self):
        """Calculates for Option 1: KDV ve Stopaj Dahil"""
        brut = self.mediation_fee / 1.20
        stopaj = brut * self.TAX_RATE
        net_tuzel = brut - stopaj
        net_gercek = brut  # Gerçek Kişi için stopaj olmayacak
        kdv = brut * self.TAX_RATE
        tahsil_tuzel = brut
        tahsil_gercek = brut + kdv
        stopaj_gercek = 0
        
        return {
            "Brüt (KDV Hariç)": (brut, brut),
            "Gelir Vergisi Stopajı (%20)": (stopaj, stopaj_gercek),
            "Alınan Net Ücret": (net_tuzel, net_gercek),
            "KDV (%20)": (kdv, kdv),
            "Tahsil Edilen Ücret": (tahsil_tuzel, tahsil_gercek)
        }

    def calculate_kdv_dahil_stopaj_haric(self):
        """Calculates for Option 2: KDV Dahil, Stopaj Hariç"""
        brut_tuzel = self.mediation_fee
        stopaj_tuzel = brut_tuzel * self.TAX_RATE
        net_tuzel = brut_tuzel - stopaj_tuzel
        kdv_tuzel = brut_tuzel * self.TAX_RATE
        tahsil_tuzel = brut_tuzel

        brut_gercek = self.mediation_fee / 1.20
        stopaj_gercek = 0
        net_gercek = brut_gercek
        kdv_gercek = brut_gercek * self.TAX_RATE
        tahsil_gercek = self.mediation_fee
        
        return {
            "Brüt (KDV Hariç)": (brut_tuzel, brut_gercek),
            "Gelir Vergisi Stopajı (%20)": (stopaj_tuzel, stopaj_gercek),
            "Alınan Net Ücret": (net_tuzel, net_gercek),
            "KDV (%20)": (kdv_tuzel, kdv_gercek),
            "Tahsil Edilen Ücret": (tahsil_tuzel, tahsil_gercek)
        }

    def calculate_kdv_ve_stopaj_haric(self):
        """Calculates for Option 3: KDV ve Stopaj Hariç"""
        brut_tuzel = self.mediation_fee / (1 - 0.20)
        stopaj_tuzel = brut_tuzel * self.TAX_RATE
        net_tuzel = self.mediation_fee
        kdv_tuzel = brut_tuzel * self.TAX_RATE
        tahsil_tuzel = brut_tuzel

        brut_gercek = self.mediation_fee
        stopaj_gercek = 0
        net_gercek = brut_gercek
        kdv_gercek = brut_gercek * self.TAX_RATE
        tahsil_gercek = brut_gercek + kdv_gercek
        
        return {
            "Brüt (KDV Hariç)": (brut_tuzel, brut_gercek),
            "Gelir Vergisi Stopajı (%20)": (stopaj_tuzel, stopaj_gercek),
            "Alınan Net Ücret": (net_tuzel, net_gercek),
            "KDV (%20)": (kdv_tuzel, kdv_gercek),
            "Tahsil Edilen Ücret": (tahsil_tuzel, tahsil_gercek)
        }

    def calculate_kdv_haric_stopaj_dahil(self):
        """Calculates for Option 4: KDV Hariç, Stopaj Dahil"""
        brut = self.mediation_fee
        stopaj = brut * self.TAX_RATE
        net_tuzel = brut - stopaj
        net_gercek = brut
        kdv = brut * self.TAX_RATE
        tahsil_tuzel = brut
        tahsil_gercek = brut + kdv
        stopaj_gercek = 0
        
        return {
            "Brüt (KDV Hariç)": (brut, brut),
            "Gelir Vergisi Stopajı (%20)": (stopaj, stopaj_gercek),
            "Alınan Net Ücret": (net_tuzel, net_gercek),
            "KDV (%20)": (kdv, kdv),
            "Tahsil Edilen Ücret": (tahsil_tuzel, tahsil_gercek)
        }

    def print_table(self):
        """Prints the invoice table in a structured format."""
        print("\nMakbuz Kalemleri | Tüzel Kişi | Gerçek Kişi")
        print("-" * 40)
        for key, (tuzel, gercek) in self.result.items():
            print(f"{key:<25} | {tuzel:,.2f} ₺ | {gercek:,.2f} ₺")
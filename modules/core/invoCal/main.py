from .calculator import InvoiceCalculator, CalculationOption

def run_program():
    """Run the program in a loop until the user chooses to exit."""
    while True:
        try:
            # Get user input for mediation fee
            mediation_fee = float(input("\033[1;34mTahsil edilecek arabuluculuk ücretini girin (₺): \033[0m").replace(",", "."))

            # Display available options
            print("\n\033[1;32mSeçenekler:\033[0m")
            for option in CalculationOption:
                print(f"\033[1;33m{option.value}\033[0m - {option.name.replace('_', ' ').title()}")

            # Get user's calculation choice
            option = int(input("\n\033[1;34mLütfen bir seçenek girin (1-4): \033[0m"))
            if option not in [1, 2, 3, 4]:
                raise ValueError("\033[1;31mGeçersiz seçenek!\033[0m")

            invoice = InvoiceCalculator(mediation_fee, option)

            # Display dynamic header
            option_text = list(CalculationOption)[option - 1].name.replace('_', ' ')
            print(f"\n\033[1;36m₺{mediation_fee:,.2f} için {option_text} Serbest Meslek Makbuzu Hesabı\033[0m")

            # Print table headers
            print("\n\033[1;37m{:30} {:>15} {:>15}".format("Makbuza Yazılacak", "Tüzel Kişi", "Gerçek Kişi"))
            print("=" * 65)

            # Print formatted results
            for key, (tuzel, gercek) in invoice.result.items():
                print("\033[1;37m{:30} {:>15,.2f} ₺ {:>15,.2f} ₺\033[0m".format(key, tuzel, gercek))

            # Ask if the user wants to continue
            continue_choice = input("\n\033[1;34mBaşka bir hesaplama yapmak istiyor musunuz? (E/H): \033[0m").strip().upper()
            if continue_choice != 'E':
                print("\033[1;31mProgram sonlandırılıyor...\033[0m")
                break
        except ValueError as e:
            print(f"\033[1;31mHata: {e}. Lütfen tekrar deneyin.\033[0m")

if __name__ == "__main__":
    run_program()

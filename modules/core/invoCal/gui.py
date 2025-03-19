from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import os
from .calculator import InvoiceCalculator
from kivy.graphics import Color, Rectangle

current_dir = os.path.dirname(os.path.abspath(__file__))
# Builder.load_file(f"{current_dir}/mediationinvoice.kv")

class InvoiceScreen(BoxLayout):
    def calculate(self):
        self.ids.result_table.clear_widgets()
        try:
            fee_input = self.ids.fee_input.text.replace(",", ".")
            mediation_fee = float(fee_input)

            option = self.ids.option_spinner.text
            option_map = {
                "KDV ve Stopaj Dahil": 1,
                "KDV Dahil, Stopaj Hariç": 2,
                "KDV ve Stopaj Hariç": 3,
                "KDV Hariç, Stopaj Dahil": 4,
            }

            invoice = InvoiceCalculator(mediation_fee, option_map[option])

            self.ids.result_label.text = (
                f"₺{mediation_fee:,.2f} için {option} Serbest Meslek Makbuzu Hesabı"
            )

            colors = [(0.9, 0.95, 1, 1), (0.8, 0.85, 0.95, 1)]
            for index, (key, (tuzel, gercek)) in enumerate(invoice.result.items()):
                row_color = colors[index % 2]

                for text in [key, f"{tuzel:,.2f} ₺", f"{gercek:,.2f} ₺"]:
                    label = Label(text=text, color=(0, 0, 0, 1))
                    with label.canvas.before:
                        Color(*row_color)
                        rect = Rectangle(size=label.size, pos=label.pos)
                        label.bind(size=lambda instance, value, rect=rect: setattr(rect, "size", value),
                                   pos=lambda instance, value, rect=rect: setattr(rect, "pos", value))
                    self.ids.result_table.add_widget(label)

        except ValueError as e:
            self.ids.result_label.text = f"Geçersiz giriş! {e}"

class InvoiceApp(App):
    def build(self):
        return InvoiceScreen()

if __name__ == "__main__":
    InvoiceApp().run()
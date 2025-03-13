# Mediation Time Calculator

Mediation Time Calculator (MedTime) is a Python application designed to help calculate mediation timeframes for various types of legal disputes. This program automatically calculates deadlines for different dispute types based on a start date.

## Features

- Time calculations for various legal dispute types
- User-friendly graphical interface
- Can run as a standalone application or embedded in another application
- Date-based calculations

## Supported Dispute Types

- Labor Law Disputes
- Commercial Law Disputes
- Consumer Law Disputes
- Disputes Arising from Rental Relationships
- Disputes Related to Dissolution of Partnership
- Disputes Arising from Condominium Law
- Disputes Arising from Neighbor Law
- Disputes Arising from Agricultural Production Contracts

## Installation

1. Download and install Python 3.x from the [official Python website](https://www.python.org/downloads/).
2. Clone or download this repository.
3. The only dependency required is tkinter, which typically comes bundled with Python.

## Usage

### Standalone Mode

To run the application as a standalone program:

```bash
python demo.py
```

### Embedded Mode

To run the application embedded in another application:

```bash
python demo.py --embedded
```

## Program Structure

- `__init__.py`: Module definition and exports.
- `calculator.py`: Main class containing time calculation logic.
- `gui.py`: Tkinter-based user interface components.
- `demo.py`: Example code demonstrating application usage.

## How It Works

1. The user enters a start date in the "DD.MM.YYYY" format in the date input field on the interface.
2. When the "Calculate" button is clicked, deadlines are calculated for each dispute type according to different week intervals.
3. The calculated dates are displayed in the table for each dispute type and week value.

## Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## License

[****]

## Contact

info@ozco.studio

---

Mediation Time Calculator - A helpful tool for time planning in legal mediation processes.
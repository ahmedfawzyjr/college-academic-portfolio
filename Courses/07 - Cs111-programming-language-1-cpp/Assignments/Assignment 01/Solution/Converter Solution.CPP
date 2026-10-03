#include <iostream>

double celsiusToFahrenheit(double c) { return (c * 9.0 / 5.0) + 32.0; }
double fahrenheitToCelsius(double f) { return (f - 32.0) * 5.0 / 9.0; }
double celsiusToKelvin(double c) { return c + 273.15; }

int main() {
    int choice;
    std::cout << "--- Unit Converter ---\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\nSelect: ";
    if (std::cin >> choice) {
        double val;
        std::cout << "Enter value: ";
        std::cin >> val;
        if (choice == 1) std::cout << "Result: " << celsiusToFahrenheit(val) << " °F\n";
        else if (choice == 2) std::cout << "Result: " << fahrenheitToCelsius(val) << " °C\n";
        else if (choice == 3) std::cout << "Result: " << celsiusToKelvin(val) << " K\n";
    }
    return 0;
}

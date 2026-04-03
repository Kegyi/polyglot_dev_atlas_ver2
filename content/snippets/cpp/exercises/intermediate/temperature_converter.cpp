#include <iostream>
#include <iomanip>

int main() {
    double celsius = 25.0;
    double fahrenheit = (celsius * 9/5) + 32;
    double kelvin = celsius + 273.15;
    
    std::cout << std::fixed << std::setprecision(2);
    std::cout << celsius << " deg C = " << fahrenheit << " deg F = " << kelvin << "K\n";
    return 0;
}

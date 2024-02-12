#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>

// Function prototypes
std::tuple<int, int, int> data_input_handler();
std::pair<std::vector<int>, std::vector<int>> power_decomposition(int power);
int computer(int number, int divisor, const std::vector<int>& powers_of_2, const std::vector<int>& powers);
void handler();

int main() {
    std::cout << "\nFigyelem! Csak pozitív, egész számokat adhat meg!\n\n";

    auto [number, power, divisor] = data_input_handler(); // szám, hatvány, oszto

    auto [powers_of_2, powers] = power_decomposition(power);
    int value = computer(number, divisor, powers_of_2, powers);

    std::cout << "\nA " << number << "^" << power << " MOD " << divisor << " értéke: " << value;

    handler();
    return 0;
}

std::tuple<int, int, int> data_input_handler() {
    int number, power, divisor;
    try {
        std::cout << "Kérem, adja meg a hatványozandó számot: ";
        std::cin >> number;
        std::cout << "Kérem, adja meg a hatványozandó szám hatványkitevőjét: ";
        std::cin >> power;
        std::cout << "Kérem, adja meg a hatványozandó szám osztóját: ";
        std::cin >> divisor;
        if (std::cin.fail() || number <= 0 || power < 0 || divisor <= 0) {
            throw std::invalid_argument("Csak pozitív, egész számokat adhat meg!");
        }
    } catch (const std::invalid_argument& e) {
        std::cerr << "\n" << e.what() << "\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return data_input_handler();
    }
    return std::make_tuple(number, power, divisor);
}

std::pair<std::vector<int>, std::vector<int>> power_decomposition(int power) {
    std::vector<int> powers_of_2;
    int counter = 0;
    while (power > 0) {
        if (power & 1) {
            powers_of_2.push_back(1 << counter);
        }
        power >>= 1;
        counter++;
    }
    std::vector<int> powers(powers_of_2.rbegin(), powers_of_2.rend());
    return std::make_pair(powers_of_2, powers);
}

int computer(int number, int divisor, const std::vector<int>& powers_of_2, const std::vector<int>& powers) {
    std::vector<int> idx_values(powers_of_2.size());
    for (size_t i = 0; i < powers_of_2.size(); ++i) {
        // Calculate power iteratively to avoid floating-point operations
        int powered_number = 1;
        for (int j = 0; j < powers_of_2[i]; ++j) {
            powered_number = (powered_number * number) % divisor;
        }
        idx_values[i] = powered_number;
    }
    std::vector<int> values;
    for (size_t i = 0; i < powers_of_2.size(); ++i) {
        if (std::find(powers.begin(), powers.end(), powers_of_2[i]) != powers.end()) {
            values.push_back(idx_values[i]);
        }
    }
    while (values.size() > 1) {
        values[0] = (values[0] * values[1]) % divisor;
        values.erase(values.begin() + 1);
    }
    return values[0];
}

void handler() {
    char repeat;
    std::cout << "\n\n\nSzeretné ismét futtatni a programot? (I/N): ";
    std::cin >> repeat;
    repeat = std::tolower(repeat);
    if (repeat == 'i' || repeat == 'y') {
        main();
    } else if (repeat == 'n') {
        std::exit(0);
    } else {
        std::cerr << "\n\nHoppá! Valamit elrontott!\n";
        handler();
    }
}

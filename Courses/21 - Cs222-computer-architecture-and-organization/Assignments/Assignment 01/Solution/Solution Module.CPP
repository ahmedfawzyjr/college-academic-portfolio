// CS222: Computer Architecture & Organization
// Practical C++ Demonstration

#include <iostream>
#include <vector>
#include <numeric>

void run_cs222() {
    std::cout << "Executing C++ implementation for CS222 - Computer Architecture & Organization" << std::endl;
    std::vector<int> values = {10, 25, 42, 68, 99};
    int sum = 0;
    for (int v : values) sum += v;
    std::cout << "Sum of elements: " << sum << std::endl;
}

int main() {
    run_cs222();
    return 0;
}

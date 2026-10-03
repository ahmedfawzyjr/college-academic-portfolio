// EE242: Logic Design (Self Study)
// Practical C++ Demonstration

#include <iostream>
#include <vector>
#include <numeric>

void run_ee242() {
    std::cout << "Executing C++ implementation for EE242 - Logic Design (Self Study)" << std::endl;
    std::vector<int> values = {10, 25, 42, 68, 99};
    int sum = 0;
    for (int v : values) sum += v;
    std::cout << "Sum of elements: " << sum << std::endl;
}

int main() {
    run_ee242();
    return 0;
}

// CSC312: System Programming
// Practical C++ Demonstration

#include <iostream>
#include <vector>
#include <numeric>

void run_csc312() {
    std::cout << "Executing C++ implementation for CSC312 - System Programming" << std::endl;
    std::vector<int> values = {10, 25, 42, 68, 99};
    int sum = 0;
    for (int v : values) sum += v;
    std::cout << "Sum of elements: " << sum << std::endl;
}

int main() {
    run_csc312();
    return 0;
}

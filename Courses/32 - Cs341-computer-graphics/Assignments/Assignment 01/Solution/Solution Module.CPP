// CS341: Computer Graphics
// Practical C++ Demonstration

#include <iostream>
#include <vector>
#include <numeric>

void run_cs341() {
    std::cout << "Executing C++ implementation for CS341 - Computer Graphics" << std::endl;
    std::vector<int> values = {10, 25, 42, 68, 99};
    int sum = 0;
    for (int v : values) sum += v;
    std::cout << "Sum of elements: " << sum << std::endl;
}

int main() {
    run_cs341();
    return 0;
}

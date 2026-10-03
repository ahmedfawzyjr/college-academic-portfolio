#include <iostream>
#include <vector>

int main() {
    std::vector<int> burst = {6, 8, 4, 3};
    int n = burst.size();
    std::vector<int> wait(n, 0), turn(n, 0);

    for (int i = 1; i < n; i++) wait[i] = wait[i - 1] + burst[i - 1];
    for (int i = 0; i < n; i++) turn[i] = wait[i] + burst[i];

    double totalWait = 0;
    for (int w : wait) totalWait += w;

    std::cout << "Avg Waiting Time: " << (totalWait / n) << std::endl;
    return 0;
}

#include <iostream>
#include <vector>

struct Process {
    int id;
    int burstTime;
    int waitingTime;
    int turnaroundTime;
};

void calculateFCFS(std::vector<Process>& processes) {
    int n = processes.size();
    processes[0].waitingTime = 0;
    processes[0].turnaroundTime = processes[0].burstTime;

    for (int i = 1; i < n; i++) {
        processes[i].waitingTime = processes[i - 1].waitingTime + processes[i - 1].burstTime;
        processes[i].turnaroundTime = processes[i].waitingTime + processes[i].burstTime;
    }
}

int main() {
    std::vector<Process> proc = {{1, 10, 0, 0}, {2, 5, 0, 0}, {3, 8, 0, 0}};
    calculateFCFS(proc);

    std::cout << "P\tBurst\tWaiting\tTurnaround\n";
    for (const auto& p : proc) {
        std::cout << p.id << "\t" << p.burstTime << "\t" << p.waitingTime << "\t" << p.turnaroundTime << "\n";
    }
    return 0;
}

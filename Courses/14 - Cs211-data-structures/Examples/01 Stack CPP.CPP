#include <iostream>
#include <vector>

template <typename T>
class Stack {
private:
    std::vector<T> elements;
public:
    void push(T val) { elements.push_back(val); }
    void pop() { if (!empty()) elements.pop_back(); }
    T top() const { return elements.back(); }
    bool empty() const { return elements.empty(); }
};

int main() {
    Stack<int> s;
    s.push(10); s.push(20); s.push(30);
    while (!s.empty()) {
        std::cout << s.top() << " ";
        s.pop();
    }
    std::cout << "\n";
    return 0;
}

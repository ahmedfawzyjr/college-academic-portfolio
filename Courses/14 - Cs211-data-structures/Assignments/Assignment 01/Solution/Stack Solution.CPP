#include <iostream>
#include <stack>
#include <string>

bool isBalanced(const std::string& expr) {
    std::stack<char> s;
    for (char c : expr) {
        if (c == '(' || c == '{' || c == '[') {
            s.push(c);
        } else if (c == ')' || c == '}' || c == ']') {
            if (s.empty()) return false;
            char top = s.top();
            if ((c == ')' && top == '(') || (c == '}' && top == '{') || (c == ']' && top == '[')) {
                s.pop();
            } else {
                return false;
            }
        }
    }
    return s.empty();
}

int main() {
    std::string test = "{[()]}";
    std::cout << test << " -> " << (isBalanced(test) ? "Balanced" : "Unbalanced") << std::endl;
    return 0;
}

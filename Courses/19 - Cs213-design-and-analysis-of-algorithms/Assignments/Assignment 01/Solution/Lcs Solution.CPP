#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int lcs(const std::string& X, const std::string& Y) {
    int m = X.length();
    int n = Y.length();
    std::vector<std::vector<int>> L(m + 1, std::vector<int>(n + 1, 0));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;
            else
                L[i][j] = std::max(L[i - 1][j], L[i][j - 1]);
        }
    }
    return L[m][n];
}

int main() {
    std::string s1 = "AGGTAB", s2 = "GXTXAYB";
    std::cout << "LCS Length: " << lcs(s1, s2) << std::endl; // Output: 4 ("GTAB")
    return 0;
}

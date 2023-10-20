#include <bits/stdc++.h>

using namespace std;

string a, b;

bool isSubstring() {
    int n = a.length();
    int m = b.length();

    if (m > n) {
        return false;
    }

    for (int i = n - m; i < n; i++) {
        if (a[i] != b[i - n + m]) {
            return false;
        }
    }

    return true;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(0);

    int n;

    cin >> n;

    while (n--) {
        cin >> a >> b;

        if (isSubstring()) {
            cout << "encaixa" << endl;
        } else {
            cout << "nao encaixa" << endl;
        }
    }

    return 0;
}
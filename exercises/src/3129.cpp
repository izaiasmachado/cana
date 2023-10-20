#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, num, r = 0, u = 0;
    set<int> s;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> num;

        auto pos = s.find(num);

        if (pos != s.end()) {
            r++;
        } else {
            u++;
        }

        s.insert(num);
    }

    cout << u << endl;
    cout << r << endl;

    return 0;
}
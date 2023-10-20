#include <bits/stdc++.h>
#define E 2.71828182845904523536
#define TOL 10e-9

using namespace std;

int p, q, r, s, t, u;

double solveEquation(double x) {
    return p * pow(E, -x) + q * sin(x) + r * cos(x) + s * tan(x) + t * pow(x, 2) + u;
}

double truncate(double var) {
    double value = (int)(var * 10000);
    return (double)value / 10000;
}

double solveBissection(double a, double b) {
    if ((b - a) < TOL) {
        return a;
    }

    double c = (a + b) / 2;
    double res = solveEquation(c);

    if (res >= 0) {
        return solveBissection(c, b);
    }

    return solveBissection(a, c);
}

int main() {
    while (cin >> p >> q >> r >> s >> t >> u) {
        FILE *fp = fopen("out.txt", "a");
        double res = solveBissection(0, 1);

        if (solveEquation(0) * solveEquation(1) > 0) {
            printf("No solution\n");
            fprintf(fp, "No solution\n");
        } else {
            printf("%.4lf\n", res);
            fprintf(fp, "%.4lf\n", res);
        }

        fclose(fp);
    }

    return 0;
}
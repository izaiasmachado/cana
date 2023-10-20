/**
 * Descrição   : UVA ONLINE JUDGE 10245 - Closest Pair Problem
 * Autor(a)    : Izaias Machado Pessoa Neto
 * Data        : 13/10/2023
 */
 
#include <bits/stdc++.h>
#define MAXN 10001
#define MIND 10000

using namespace std;

typedef struct {
    double x;
    double y;
} Point;

vector<Point> points(MAXN);

Point createPoint(double x, double y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}

double getDistance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double bruteForceClosestPair(int p, int r) {
    double minDistance = -1;
    
    for (int i = p; i <= r; i++) {
        for (int j = i + 1; j <= r; j++) {
            double d = getDistance(points[i], points[j]);
            if (minDistance == -1 || d < minDistance) {
                minDistance = d;
            }
        }
    }

    return minDistance;
}

vector<Point> getCandidates(int p, int r, double d, double x) {
    vector<Point> candidates;

    for (int i = p; i <= r; i++) {
        if (abs(points[i].x - x) <= d) {
            candidates.push_back(points[i]);
        }
    }

    sort(candidates.begin(), candidates.end(), [](Point a, Point b) {
        return a.y < b.y;
    });

    return candidates;
}

double mergeSh(int p, int r, double dl, double dr, double x) {
    double d = min(dl, dr);
    vector<Point> candidates = getCandidates(p, r, d, x);

    for (int i = 0; i < candidates.size(); i++) {
        for (int j = i + 1; j < candidates.size(); j++) {
            double distance = getDistance(candidates[i], candidates[j]);

            if (distance < d) {
                d = distance;
            }
        }
    }

    return d;
}

double recursiveShDistance(int p, int r) {
    if (r <= p + 2) {
        return bruteForceClosestPair(p, r);
    }

    int q = (p + r) / 2;
    double dl = recursiveShDistance(p, q);
    double dr = recursiveShDistance(q + 1, r);
    return mergeSh(p, r, dl, dr, points[q].x);
}

double shDistance(int n) {
    sort(points.begin(), points.begin() + n, [](Point a, Point b) {
        return a.x < b.x;
    });

    return recursiveShDistance(0, n - 1);
}

int main() {
    int n;
    double x, y, distance = 0;

    while (cin >> n && (n != 0)) {
        for (int i = 0; i < n; i++) {
            cin >> x >> y;
            points[i] = createPoint(x, y);
        }

        distance = shDistance(n);

        if (distance >= MIND || distance < 0) {
            cout << "INFINITY" << endl;
        } else {
            printf("%.4lf\n", distance);
        }
    }

    return 0;
}
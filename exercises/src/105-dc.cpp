/**
 * Disciplina  : ECO0047 - Construção e Análise de Algoritmos
 * Professor   : Antônio Josefran de Oliveira Bastos
 * Descrição   : Trabalho 02 - UVA ONLINE JUDGE 105 (Divisão e Conquista)
 * Autor(a)    : Izaias Machado Pessoa Neto
 * Data        : 11/10/2023
 */

#include <bits/stdc++.h>
#define MAXN 10000

using namespace std;

typedef struct {
    int x;
    int h;
} Point;

typedef struct {
    int l;
    int h;
    int r;
} Building;

Point createPoint(int x, int h) {
    Point point;
    point.x = x;
    point.h = h;
    return point;
}

Building createBuilding(int l, int h, int r) {
    Building building;
    building.l = l;
    building.h = h;
    building.r = r;
    return building;
}

Building buildings[MAXN];
vector<Point> Points;

vector<Point> mergeSkylines(vector<Point> *v1, vector<Point> *v2) {
    vector<Point> result = vector<Point>();
    int h1 = 0, h2 = 0;
    int i = 0, j = 0;
    int s1, s2, maxH;

    while (i < v1->size() && j < v2->size()) {
        Point* p1 = &v1->at(i);
        Point* p2 = &v2->at(j);
        
        if (p1->x < p2->x || (p1->x == p2->x && p1->h > p2->h)) {
            h1 = p1->h;
            maxH = max(h1, h2);
            result.push_back(createPoint(p1->x, maxH));
            i++;
        } else if (p1->x > p2->x || (p1->x == p2->x && p1->h < p2->h)) {
            h2 = p2->h;
            maxH = max(h1, h2);
            result.push_back(createPoint(p2->x, maxH));
            j++;
        } else {
            h1 = p1->h;
            h2 = p2->h;
            maxH = max(h1, h2);
            result.push_back(createPoint(p1->x, maxH));
            i++;
            j++;
        }
    }

    while (i < v1->size()) {
        result.push_back(v1->at(i));
        i++;
    }

    while (j < v2->size()) {
        result.push_back(v2->at(j));
        j++;
    }

    return result;
}

vector<Point> solveSkyline(int start, int end) {
    vector<Point> result;

    if (start == end) {
        result = vector<Point>();
        result.push_back(createPoint(buildings[start].l, buildings[start].h));
        result.push_back(createPoint(buildings[start].r, 0));
        return result;
    }

    int mid = (start + end) / 2;
    vector<Point> t1 = solveSkyline(start, mid);
    vector<Point> t2 = solveSkyline(mid + 1, end);
    return mergeSkylines(&t1, &t2);
}

int main() {
    int count = 0;
    int l, h, r;

    while (cin >> l >> h >> r && (l != 0)) {
        buildings[count++] = createBuilding(l, h, r);
    }

    vector<Point> result = solveSkyline(0, count - 1);
    int height = -1;

    for (int i = 0; i < result.size(); i++) {
        if (result[i].h != height) {
            if (height != -1) {
                cout << height << " ";
            }

            cout << result[i].x << " ";
            height = result[i].h;
        }
    }

    cout << 0 << endl;

    return 0;
}

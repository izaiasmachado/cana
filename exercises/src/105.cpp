/**
 * Disciplina  : ECO0047 - Construção e Análise de Algoritmos
 * Professor   : Antônio Josefran de Oliveira Bastos
 * Descrição   : Trabalho 02 - UVA ONLINE JUDGE 105 (Solução Original)
 * Autor(a)    : Izaias Machado Pessoa Neto
 * Data        : 07/10/2023
 */

#include <bits/stdc++.h>
#define MAXN 10000

using namespace std;

int main() {
    int l, h, r, count;
    int i = 0, sizeHs = 0, number = -1;
    int hs[MAXN];
    memset(hs, 0, sizeof(hs));

    while (cin >> l >> h >> r && (l != 0)) {
        if (i == 0) count = l;

        for (int j = l; j < r; j++) {
            hs[j - 1] = max(hs[j - 1], h);
        }

        i++;
        sizeHs = max(sizeHs, r);
    }

    if (l == 0) i--;
    
    for (int j = 0; j < sizeHs; j++) {
        if (hs[j] != number) {
            if (number != -1) {
                cout << number << " ";
            }

            cout << j + 1 << " ";
            number = hs[j];
        }
    }

    cout << 0 << endl;

    return 0;
}
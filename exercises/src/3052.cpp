#include <bits/stdc++.h>
#define MAXN 500

using namespace std;

char v[MAXN][MAXN];
bool visited[MAXN][MAXN];

int n, m;
int nextX[] = {0, 1, 0, -1};
int nextY[] = {1, 0, -1, 0};

bool isValid(int x, int y) {
  return x >= 0 && x < n && y >= 0 && y < m;
}

bool shouldBecomeWater(int x, int y) {
  if (!isValid(x, y) || v[x][y] != '.') return false;

  if (isValid(x - 1, y) && v[x - 1][y] == 'o') {
    return true;
  } else if (isValid(x, y - 1) && v[x][y - 1] == 'o' && isValid(x + 1, y - 1) && v[x + 1][y - 1] == '#') {
    return true;
  } else if (isValid(x, y + 1) && v[x][y + 1] == 'o' && isValid(x + 1, y + 1) && v[x + 1][y + 1] == '#') {
    return true;
  }

  return false;
}

void dfs(int x, int y) {
  visited[x][y] = true;

  for (int i = 0; i < 4; i++) {
    int a = x + nextX[i];
    int b = y + nextY[i];

    if (!visited[a][b] && shouldBecomeWater(a, b)) {
      v[a][b] = 'o';
      dfs(a, b);
    }
  }
}

int main() {
  int wX, wY;

  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> n >> m;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> v[i][j];

      if (v[i][j] == 'o') {
        wX = i;
        wY = j;
      }
    }
  }

  dfs(wX, wY);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cout << v[i][j];
    }

    cout << endl;
  } 

  return 0;
}

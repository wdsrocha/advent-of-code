#include <iostream>
#include <queue>
using namespace std;
#define ii pair<int, int>
#define oo 1000000000

struct Cell {
  int i, j;
  Cell() {}
  Cell(int i, int j) : i(i), j(j) {}
  bool operator==(const Cell& other) const {
    return i == other.i && j == other.j;
  }
};

const Cell UP = {-1, 0};
const Cell RIGHT = {0, 1};
const Cell DOWN = {1, 0};
const Cell LEFT = {0, -1};
const vector<Cell> DIRECTIONS = {UP, RIGHT, DOWN, LEFT};

int n, m;
vector<string> grid;
vector<vector<int>> dist;
string line;
Cell source;

// UP RIGHT DOWN LEFT
int f(char c) {
  if (c == '.') return 0b0000;
  if (c == '|') return 0b1010;
  if (c == '-') return 0b0101;
  if (c == 'L') return 0b1100;
  if (c == 'J') return 0b1001;
  if (c == '7') return 0b0011;
  if (c == 'F') return 0b0110;
  if (c == 'S') return 0b1111;
  return -1;  // ?
}

ii g(Cell direction) {
  if (direction == UP) return {0b1000, 0b0010};
  if (direction == RIGHT) return {0b0100, 0b0001};
  if (direction == DOWN) return {0b0010, 0b1000};
  if (direction == LEFT) return {0b0001, 0b0100};
  return {0b0000, 0b0000};
}

bool canMove(Cell from, Cell to, Cell d) {
  if (to.i < 0 || to.i >= n || to.j < 0 || to.j >= m) {
    return false;
  }

  char u = grid[from.i][from.j];
  char v = grid[to.i][to.j];

  return (f(u) & g(d).first) && (f(v) & g(d).second);
}

int main() {
  for (int i = 0; cin >> line; i++) {
    grid.push_back(line);
    dist.push_back(vector<int>(line.size(), oo));
    for (int j = 0; j < line.size(); j++) {
      if (line[j] == 'S') {
        source = {i, j};
      }
    }
  }
  n = grid.size();
  m = grid[0].size();

  queue<Cell> q;
  q.push(source);
  dist[source.i][source.j] = 0;

  int farthestDistance = 0;

  while (q.size()) {
    auto u = q.front();
    q.pop();

    for (auto direction : DIRECTIONS) {
      Cell v = {u.i + direction.i, u.j + direction.j};

      if (canMove(u, v, direction) && dist[v.i][v.j] == oo) {
        q.push(v);
        dist[v.i][v.j] = dist[u.i][u.j] + 1;
        farthestDistance = max(farthestDistance, dist[v.i][v.j]);
      }
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cout << (dist[i][j] == oo ? 0 : dist[i][j]) << ' ';
    }
    cout << endl;
  }

  cout << farthestDistance << endl;

  return 0;
}
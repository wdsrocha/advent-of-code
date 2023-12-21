#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#define int long long
using namespace std;

// const int MAX_STEPS = 6;
// const int MAX_STEPS = 10;
// const int MAX_STEPS = 50;
const int MAX_STEPS = 100;
// const int MAX_STEPS = 64;
// const int MAX_STEPS = 26501365;
const pair<int, int> UP = {-1, 0};
const pair<int, int> RIGHT = {0, 1};
const pair<int, int> DOWN = {1, 0};
const pair<int, int> LEFT = {0, -1};
const vector<pair<int, int>> DIRECTIONS = {UP, RIGHT, DOWN, LEFT};

int n, m;
vector<string> grid;
map<int, map<int, bool>> visited;
map<int, map<int, int>> dist;

struct Cell {
  int i, j, min_steps;

  Cell() {}
  Cell(int i, int j, int min_steps) : i(i), j(j), min_steps(min_steps) {}

  int to_int() { return n * m * this->min_steps + m * this->i + this->j; }
};

// bool isGarden(int i, int j) {
//   i = (i + n) % n;
//   j = (j + m) % m;
//   return grid[i][j] == '.';
// }

bool isGarden(int i, int j) {
  if (i < 0 || i >= n) return false;
  if (j < 0 || j >= m) return false;
  return grid[i][j] == '.';
}

signed main() {
  string row;
  Cell source;

  for (int i = 0; cin >> row; i++) {
    grid.push_back(row);
    for (int j = 0; j < row.size(); j++) {
      if (grid[i][j] == 'S') {
        source = Cell(i, j, 0);
        grid[i][j] = '.';
      }
    }
  }

  n = grid.size();
  m = grid[0].size();

  queue<Cell> q;
  dist[source.i][source.j] = 1;
  q.push(source);

  // vector<int> count(MAX_STEPS + 1, 0);

  while (q.size()) {
    auto curr = q.front();
    q.pop();
    // count[curr.min_steps]++;

    for (int k = 0; k < 4; k++) {
      Cell next = Cell(curr.i + DIRECTIONS[k].first,
                       curr.j + DIRECTIONS[k].second, curr.min_steps + 1);

      if (isGarden(next.i, next.j) && !dist[next.i][next.j] &&
          next.min_steps <= MAX_STEPS) {
        dist[next.i][next.j] = dist[curr.i][curr.j] + 1;
        q.push(next);
      }
    }
  }

  int pair_ans = 0;
  int odd_ans = 0;
  for (auto it = dist.begin(); it != dist.end(); ++it) {
    int i = it->first;
    for (auto jt = it->second.begin(); jt != it->second.end(); ++jt) {
      int j = jt->first;
      int distance = jt->second;
      // Process the distance value

      if (distance % 2) {
        odd_ans++;
      } else {
        pair_ans++;
      }
    }
  }

  // Print the grid matrix with dist[i][j] values in empty fields
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (source.i == i && source.j == j) {
        cout << "S";
      } else if (dist[i][j]) {
        cout << dist[i][j] % 2;
      } else if (grid[i][j] == '#') {
        cout << '#';
      } else {
        cout << ' ';
      }
    }
    cout << endl;
  }

  cout << "Pair: " << pair_ans << endl;
  cout << "Odd: " << odd_ans << endl;

  return 0;
}
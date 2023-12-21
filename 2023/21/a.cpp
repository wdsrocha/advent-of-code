#include <iostream>
#include <queue>
using namespace std;

const int MAX_STEPS = 6;
// const int MAX_STEPS = 64;
const pair<int, int> UP = {-1, 0};
const pair<int, int> RIGHT = {0, 1};
const pair<int, int> DOWN = {1, 0};
const pair<int, int> LEFT = {0, -1};
const vector<pair<int, int>> DIRECTIONS = {UP, RIGHT, DOWN, LEFT};

struct Cell {
  int i, j, min_steps;

  Cell() {}
  Cell(int i, int j, int min_steps) : i(i), j(j), min_steps(min_steps) {}
};

int main() {
  vector<string> grid;
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

  int n = grid.size();
  int m = grid[0].size();

  queue<Cell> q;
  q.push(source);

  vector<vector<vector<bool>>> marked(
      n, vector<vector<bool>>(m, vector<bool>(MAX_STEPS, false)));

  vector<int> count(MAX_STEPS + 1, 0);

  int garden_plots_walked = 0;
  while (q.size()) {
    auto curr = q.front();
    q.pop();

    if (marked[curr.i][curr.j][curr.min_steps]) {
      continue;
    }
    marked[curr.i][curr.j][curr.min_steps] = true;

    count[curr.min_steps]++;

    // cout << curr.i << ' ' << curr.j << ' ' << curr.min_steps << endl;

    for (int k = 0; k < 4; k++) {
      Cell next = Cell(curr.i + DIRECTIONS[k].first,
                       curr.j + DIRECTIONS[k].second, curr.min_steps + 1);

      if (next.i < 0 || next.i >= n || next.j < 0 || next.j >= m) {
        continue;
      }

      // next.i = (next.i + n) % n;
      // next.j = (next.j + m) % m;

      if (grid[next.i][next.j] == '.' && next.min_steps <= MAX_STEPS) {
        q.push(next);
      }
    }
  }

  // for (int i = 0; i < n; i++) {
  //   for (int j = 0; j < m; j++) {
  //     cout << grid[i][j];
  //   }
  //   cout << endl;
  // }

  for (int i = 0; i <= MAX_STEPS; i++) {
    cout << i << ' ' << count[i] << endl;
  }

  return 0;
}
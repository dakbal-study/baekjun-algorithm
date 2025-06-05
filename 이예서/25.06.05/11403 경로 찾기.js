const fs = require("fs");
const [n, ...lines] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = parseInt(n, 10);
const graph = lines.map((line) => line.split(" ").map(Number));
const answer = [...Array(N)].map(() => Array(N).fill(0));

const dfs = (row, start, visit) => {
  for (let i = 0; i < N; i++) {
    if (graph[row][i] && !visit[i]) {
      visit[i] = true;
      answer[start][i] = 1;
      dfs(i, start, visit);
    }
  }
};

for (let i = 0; i < N; i++) {
  const visited = Array(N).fill(false);
  dfs(i, i, visited);
}

console.log(answer.map((v) => v.join(" ")).join("\n"));
const [n, m] = line1.split(" ").map(Number);
const maze = lines.map((row) => row.split("").map(Number));

const dist = Array.from({ length: n }, () => Array(m).fill(0));
const visited = Array.from({ length: n }, () => Array(m).fill(false));
const queue = [];

// 시작점 초기화
queue.push([0, 0]);
visited[0][0] = true;
dist[0][0] = 1;

const dirs = [
  [-1, 0], // up
  [1, 0], // down
  [0, -1], // left
  [0, 1], // right
];

while (queue.length) {
  const [x, y] = queue.shift();

  // 목적지에 도달했다면 바로 종료해도 무방
  for (const [dx, dy] of dirs) {
    const nx = x + dx;
    const ny = y + dy;

    // 유효 범위, 이동 가능, 미방문 체크
    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
    if (visited[nx][ny] || maze[nx][ny] === 0) continue;

    visited[nx][ny] = true;
    dist[nx][ny] = dist[x][y] + 1;
    queue.push([nx, ny]);
  }
}

// 결과 출력: 출발부터 도착까지 최소 칸 수
console.log(dist[n - 1][m - 1]);

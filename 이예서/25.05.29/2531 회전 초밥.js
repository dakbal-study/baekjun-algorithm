const fs = require("fs");
const [info, ...lines] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, d, k, c] = info.split(" ").map(Number);
const belt = lines.map(Number);
const sushi = belt.concat(belt.slice(0, k - 1));

const count = new Array(d + 1).fill(0);
let distinct = 0;
for (let i = 0; i < k; i++) {
  if (count[sushi[i]]++ === 0) distinct++;
}

let answer = distinct + (count[c] === 0 ? 1 : 0);
for (let i = 1; i < N; i++) {
  const out = sushi[i - 1];
  if (--count[out] === 0) distinct--;
  const ino = sushi[i + k - 1];
  if (count[ino]++ === 0) distinct++;

  const current = distinct + (count[c] === 0 ? 1 : 0);
  if (current > answer) answer = current;
}

console.log(answer);
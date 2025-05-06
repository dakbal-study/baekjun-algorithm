const fs = require("fs");
const [first, second] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, K] = first.split(" ").map(Number);
const A = second.split(" ").map(BigInt);

const S = new Array(N);
let sum = 0n;
for (let i = 0; i < N; i++) {
  sum += A[i];
  S[i] = sum;
}

S.sort((a, b) => (a > b ? -1 : a < b ? 1 : 0));

let answer = 0n;
for (let i = 0; i < K; i++) {
  answer += S[i];
}

console.log(answer.toString());

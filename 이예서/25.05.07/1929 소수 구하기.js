const fs = require("fs");
const [M, N] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

// ** 문자열 누적 **
// 메모리: 18204 KB, 시간: 184 ms
const isPrime = new Uint8Array(N + 1).fill(1);
isPrime[0] = isPrime[1] = 0;

let output = "";

for (let i = 2; i <= N; i++) {
  if (!isPrime[i]) continue;
  if (i >= M) output += i + "\n";

  for (let j = i * i; j <= N; j += i) {
    isPrime[j] = 0;
  }
}

process.stdout.write(output);

// ** 배열 누적 **
// 메모리: 24568 KB, 시간: 184 ms

// const isPrime = new Array(N + 1).fill(true);
// isPrime[0] = isPrime[1] = false;

// for (let i = 2; i <= Math.sqrt(N); i++) {
//   if (!isPrime[i]) continue;
//   for (let j = i * i; j <= N; j += i) {
//     isPrime[j] = false;
//   }
// }

// const answer = [];
// for (let i = M; i <= N; i++) {
//   if (isPrime[i]) answer.push(i);
// }

// console.log(answer.join("\n"));

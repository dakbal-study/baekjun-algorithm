const fs = require("fs");
const [line1, line2] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, K] = line1.split(" ").map(Number);
const arr = line2.split(" ").map(Number);
const cnt = new Array(100001).fill(0);
let ans = 0;
let left = 0;

for (let right = 0; right < N; right++) {
  const x = arr[right];
  cnt[x]++;

  while (cnt[x] > K) {
    cnt[arr[left]]--;
    left++;
  }

  ans = Math.max(ans, right - left + 1);
}

console.log(ans);
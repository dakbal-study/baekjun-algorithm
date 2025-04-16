const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const len = Number(input[0]);
const nums = input[1].split(" ").map(Number);

const dp = new Array(nums);
dp[0] = 1;

for (let i = 0; i < len; i++) {
  let max = 0;
  for (let j = 0; j <= i; j++) {
    if (nums[j] < nums[i]) {
      max = Math.max(max, dp[j]);
    }
  }
  dp[i] = max + 1;
}

console.log(Math.max(...dp));

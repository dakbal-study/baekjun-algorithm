const fs = require("fs");
const n = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const MOD = 10007;
const dp = new Array(n + 1).fill(0);

dp[1] = 1;
if (n >= 2) dp[2] = 2;

for (let i = 3; i <= n; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
}

console.log(dp[n]);
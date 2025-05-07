const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = input.shift();

for (let i = 0; i < T * 2; i += 2) {
  const N = Number(input[i]);
  const arr = input[i + 1].split(" ").map(Number);
  let profit = 0, max = 0;

  for (let i = N - 1; i >= 0; i--) {
    const price = arr[i];
    if (price > max) max = price;
    else profit += max - price;
  }

  console.log(profit);
}
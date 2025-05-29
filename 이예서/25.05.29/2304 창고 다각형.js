const fs = require("fs");
const [N, ...pillars] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let minL = Infinity, maxL = -Infinity;
let maxH = 0, peak = 0;
let area = 0, height = 0;
const arr = Array(1001).fill(0);

for (let i = 0; i < N; i++) {
  const [L, H] = pillars[i].split(" ").map(Number);
  arr[L] = H;
  if (L < minL) minL = L;
  if (L > maxL) maxL = L;
  if (H > maxH) {
    maxH = H;
    peak = L;
  }
}

for (let i = minL; i <= peak; i++) {
  height = Math.max(height, arr[i]);
  area += height;
}

height = 0;
for (let i = maxL; i > peak; i--) {
  height = Math.max(height, arr[i]);
  area += height;
}

console.log(area);
const fs = require("fs");
const str = fs.readFileSync("/dev/stdin").toString().trim().split("");
const n = str.length;

for (let i = 0; i < n; i++) {
  const sliceStr = str.slice(i);
  const reverseSliceStr = [...sliceStr].reverse().join("");
  if (sliceStr.join("") === reverseSliceStr) {
    console.log(n + i);
    process.exit();
  }
}
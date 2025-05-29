const fs = require("fs");
const [t, ...datas] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// Stack
for (let i = 0; i < Number(t); i++) {
  const data = datas[i];
  const stack = [];

  if (data[0] === ")" || data[data.length - 1] === "(") {
    console.log("NO");
    continue;
  }

  for (let j = 0; j < data.length; j++) {
    const l = data[j];
    if (l === "(") {
      stack.push(l);
    } else if (stack[stack.length - 1] === "(") {
      stack.pop();
    } else {
      stack.push(l);
    }
  }

  console.log(stack.length === 0 ? "YES" : "NO");
}

// Counting
// for (let i = 0; i < Number(t); i++) {
//   const s = datas[i];
//   let balance = 0;
//   let valid = true;

//   for (const ch of s) {
//     if (ch === "(") {
//       balance++;
//     } else {
//       balance--;
//     }
//     if (balance < 0) {
//       valid = false;
//       break;
//     }
//   }

//   console.log(valid && balance === 0 ? "YES" : "NO");
// }

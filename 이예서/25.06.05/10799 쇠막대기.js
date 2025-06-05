const fs = require("fs");
const lasor = fs.readFileSync("/dev/stdin").toString().trim().split("");

const stack = [];
let rods = 0;

lasor.forEach((p, i) => {
  if (p === "(") {
    stack.push(p);
  } else {
    stack.pop();

    if (lasor[i - 1] === "(") {
      rods += stack.length;
    } else {
      rods++;
    }
  }
});

console.log(rods);
const fs = require("fs");
const [N, ...Xs] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s+/)
  .map(Number);

const sortedUnique = Array.from(new Set(Xs)).sort((a, b) => a - b);
const XMap = new Map();
sortedUnique.forEach((x, i) => XMap.set(x, i));
const answer = Xs.map((x) => XMap.get(x)).join(" ");

console.log(answer);
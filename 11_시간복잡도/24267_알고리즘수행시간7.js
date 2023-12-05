const fs = require("fs");
let n = fs.readFileSync("/dev/stdin").toString();

console.log(`${BigInt(n) * BigInt(n - 1) * BigInt(n - 2) / BigInt(6)}`);
console.log(3);
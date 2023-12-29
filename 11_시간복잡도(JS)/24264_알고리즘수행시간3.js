const fs = require("fs");
let n = +fs.readFileSync("/dev/stdin").toString();

console.log(n * n);
console.log(2);
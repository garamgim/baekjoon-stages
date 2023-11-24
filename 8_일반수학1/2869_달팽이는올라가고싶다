const fs = require("fs");
let [up, down, peak] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);
let a = (peak - up) / (up - down);
console.log(Math.ceil(a) + 1);
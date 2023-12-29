const fs = require("fs");
let [x, y, w, h] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);

const a = Math.abs(x - w);
const b = Math.abs(y - h);

console.log(Math.min(a, b, x, y));

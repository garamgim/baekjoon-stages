const fs = require("fs");
const input = +fs.readFileSync('/dev/stdin').toString();
const vrt = Math.pow(2, input) + 1;

console.log(Math.pow(vrt, 2));
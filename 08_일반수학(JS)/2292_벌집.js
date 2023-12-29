const fs = require("fs");
let input = +fs.readFileSync('/dev/stdin').toString();
let n = 1;
while (3 * n * (n - 1) + 1 < input) {
    n++;
}
console.log(n);
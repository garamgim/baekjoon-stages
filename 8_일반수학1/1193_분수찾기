const fs = require("fs");
let input = +fs.readFileSync('/dev/stdin').toString();

let n = 1;

while ((n * (n + 1) / 2) < input) {
    n++;
}

let a = input - (n * (n - 1) / 2);

if (n % 2 === 0) {
    console.log(`${a}/${n - a + 1}`)
} else {
    console.log(`${n - a + 1}/${a}`)
}

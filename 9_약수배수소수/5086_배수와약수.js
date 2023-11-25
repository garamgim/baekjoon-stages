const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

let i = 0;
while (input[i] !== '0 0') {
    const [a, b] = input[i].split(" ").map(Number);
    if (b % a === 0) {
        console.log("factor");
    } else if (a % b === 0) {
        console.log("multiple");
    } else {
        console.log("neither");
    }
    i++;
}
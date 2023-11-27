const fs = require("fs");
let [a, b, c] = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number).sort((a, b) => a - b);;

if (a === b && b === c) {
    console.log(a * 3);
} else if ((a + b) <= c) {
    console.log(2 * (a + b) - 1);
} else {
    console.log(a + b + c);
}

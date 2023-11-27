const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let i = 0;

while (input[i] !== "0 0 0") {
    [a, b, c] = input[i].split(" ").map(Number).sort((a, b) => a - b);
    if (a + b <= c) {
        console.log("Invalid");
    } else {
        if (a === b && b === c) {
            console.log("Equilateral");
        } else if (a === b || b === c) {
            console.log("Isosceles");
        } else {
            console.log("Scalene");
        }
    }
    i++;
}
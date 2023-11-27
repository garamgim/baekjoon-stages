const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

for (let i = 0; i < 3; i++) {
    input[i] = input[i].split(" ").map(Number);
}

let x = [];
let y = [];

for (let i = 0; i < 3; i++) {
    x.push(input[i][0]);
    y.push(input[i][1]);
}

let ansX = 0;
let ansY = 0;

if (x[0] === x[1]) {
    ansX = x[2];
} else if (x[0] === x[2]) {
    ansX = x[1];
} else if (x[1] === x[2]) {
    ansX = x[0];
}

if (y[0] === y[1]) {
    ansY = y[2];
} else if (y[0] === y[2]) {
    ansY = y[1];
} else if (y[1] === y[2]) {
    ansY = y[0];
}

console.log(`${ansX} ${ansY}`)
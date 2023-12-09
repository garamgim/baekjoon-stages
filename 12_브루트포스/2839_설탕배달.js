const fs = require("fs");
let n = +fs.readFileSync("/dev/stdin").toString();

let bag = 0;
let fivekgMax = 0;

for (let i = 1; i <= parseInt(n / 5); i++) {
    if ((n - 5 * i) % 3 === 0) {
        fivekgMax = Math.max(fivekgMax, i);
    }
}

if (fivekgMax !== 0) {
    bag = fivekgMax + (n - fivekgMax * 5) / 3;
} else {
    if (n % 3 === 0) {
        bag = n / 3;
    } else {
        bag = -1;
    }
}

console.log(bag);
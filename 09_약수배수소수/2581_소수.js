const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split("\n").map(Number);

let prm = [];

for (let i = input[0]; i <= input[1]; i++) {
    let isPrime = true;

    if (i === 1) { isPrime = false; }

    for (let j = 2; j <= Math.sqrt(i); j++) {
        if (i % j === 0) {
            isPrime = false;
            break
        }
    }

    if (isPrime) { prm.push(i); }
}

let sum = 0;
for (let i = 0; i < prm.length; i++) {
    sum += prm[i];
}

if (prm.length === 0) {
    console.log(-1);
} else {
    console.log(sum);
    console.log(prm[0]);
} 
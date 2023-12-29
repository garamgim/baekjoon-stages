const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split("\n");
const inputArr = input[1].split(" ").map(Number);

let cnt = Number(input[0]);

for (const num of inputArr) {
    if (num === 1) {
        cnt -= 1;
    }

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            cnt -= 1;
            break
        }
    }
}

console.log(cnt);

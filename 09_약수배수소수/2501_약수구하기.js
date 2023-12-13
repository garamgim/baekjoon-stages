const fs = require("fs");
let [a, b] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);

let arr = [];
for (let i = 1; i <= a; i++) {
    if (a % i === 0) {
        arr.push(i);
    }
}

(b > arr.length) ? console.log(0) : console.log(arr[b - 1])
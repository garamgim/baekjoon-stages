const fs = require("fs");
[a, c, n] = fs.readFileSync("/dev/stdin").toString().split("\n");
[a, b] = a.split(" ").map(Number);
if (((a * n + b) <= c * n) && (a <= c)) {
    console.log(1);
} else {
    console.log(0);
}
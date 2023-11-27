const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n")
let xArr = [];
let yArr = [];
for (let i = 1; i <= +input[0]; i++) {
    xArr.push(input[i].split(" ").map(Number)[0]);
    yArr.push(input[i].split(" ").map(Number)[1]);
}

console.log((Math.max(...xArr) - Math.min(...xArr)) * (Math.max(...yArr) - Math.min(...yArr)))

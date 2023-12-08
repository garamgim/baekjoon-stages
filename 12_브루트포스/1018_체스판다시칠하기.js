const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [n, m] = input[0].split(" ").map(Number);
let inputArr = [];
for (let i = 1; i < input.length; i++) {
    const tempArr = input[i].split("");
    inputArr.push(tempArr);
}

const board = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

function counter(arr, x, y) {
    let cnt = 0;
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (board[i][j] !== arr[x + i][y + j]) {
                cnt += 1;
            }
        }
    }
    return Math.min(cnt, 64 - cnt);
}

let min = 64;

for (let i = 0; i <= (n - 8); i++) {
    for (let j = 0; j <= (m - 8); j++) {
        if (min > counter(inputArr, i, j)) {
            min = counter(inputArr, i, j);
        }
    }
}

console.log(min);
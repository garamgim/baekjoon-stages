const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n")
const [n, m] = input[0].split(" ").map(Number);
const chosenCards = input[1].split(" ").map(Number);

let max = 0;

for (let i = 0; i < chosenCards.length; i++) {
    for (let j = i + 1; j < chosenCards.length; j++) {
        for (let k = j + 1; k < chosenCards.length; k++) {
            const sum = chosenCards[i] + chosenCards[j] + chosenCards[k];
            if (sum > max && sum <= m) {
                max = sum;
            }
        }
    }
}

console.log(max);
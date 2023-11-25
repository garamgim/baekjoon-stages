const fs = require("fs");
const inputArr = fs.readFileSync('/dev/stdin').toString().split("\n");

let i = 0

while (inputArr[i] !== "-1") {

    const input = Number(inputArr[i]);
    let ms = [];

    for (let j = 1; j <= input; j++) {
        if (input / j > j) {
            if (input % j === 0) {
                ms.push(j);
                ms.push(input / j);
            }
        } else if (input / j === j) {
            ms.push(j);
        } else {
            break
        }
    }

    ms = ms.sort((a, b) => a - b);
    ms.pop();

    let sum = 0;
    for (let j = 0; j < ms.length; j++) {
        sum += ms[j];
    }

    if (sum === input) {
        console.log(`${input} = ${ms.join(" + ")}`)
    } else {
        console.log(`${input} is NOT perfect.`)
    }

    i++;

}
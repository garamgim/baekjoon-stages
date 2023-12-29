const fs = require("fs");
let input = +fs.readFileSync('/dev/stdin').toString();

function isPrime(x) {
    if (x === 1) { return false }
    for (let i = 2; i <= Math.sqrt(x); i++) {
        if (x % i === 0) {
            return false
        }
    }
    return true
}

if (!isPrime(input)) {
    let primeFactors = [];

    for (let i = 2; i < input; i++) {
        if (input % i === 0 && isPrime(i)) {
            primeFactors.push(i);
        }
    }

    primeFactors.sort((a, b) => a - b);

    let repeat = [];

    for (let num of primeFactors) {
        let temp = input;
        let cnt = 0;
        while (Number.isInteger(temp / num)) {
            temp /= num;
            cnt += 1;
        }
        repeat.push(cnt);
    }

    for (let i = 0; i < primeFactors.length; i++) {
        for (let j = 0; j < repeat[i]; j++) {
            console.log(primeFactors[i]);
        }
    }

} else { console.log(input); }
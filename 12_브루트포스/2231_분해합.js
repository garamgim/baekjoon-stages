const fs = require("fs");
let n = +fs.readFileSync("/dev/stdin").toString();

for (let i = 1; i <= n; i++) {
    let num = i;
    let sum = i;
    while (num > 0) {
        sum += num % 10;
        num = parseInt(num / 10);
    }
    if (sum === n) {
        console.log(i);
        break
    }

    if (i === n) {
        console.log(0)
    }
}

// 계속 통과가 되지 않고 있다가 인덱스 값의 범위를 (<n)에서 (<=n)로 변경해주니 맞았다.
// 한 숫자가 자기 자신의 생성자가 될 수 없을 것 같은데 이유가 있나...?
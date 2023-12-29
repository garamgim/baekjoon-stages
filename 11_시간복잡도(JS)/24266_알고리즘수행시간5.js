const fs = require("fs");
let n = fs.readFileSync("/dev/stdin").toString();
n = BigInt(n)
console.log(`${n * n * n}`);
console.log(3);

// BitInt 사용시에는 n이 붙어 나오기 때문에 문자열로 다시 변경해줘야함
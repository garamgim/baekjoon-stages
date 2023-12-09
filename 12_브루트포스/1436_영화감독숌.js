const fs = require("fs");
let n = +fs.readFileSync("/dev/stdin").toString();

let doom = 666;
let cnt = 1;

while (cnt !== n) {
    doom += 1;
    if ((doom).toString().indexOf("666") !== -1) {
        cnt += 1;
    }
}

console.log(doom);
const fileReader = require("../fileReader");

let file = fileReader("./input.txt").split(/\n/);

// console.log(file);

const pairs = { ")": "(", "]": "[", "}": "{", ">": "<" };
const points = { ")": 3, "]": 57, "}": 1197, ">": 25137 };

function sumIncorrectSyntax(file) {
  const stack = [];
  let sum = 0;

  for (let i = 0; i < file.length; i++) {
    for (let char of file[i]) {
      if (pairs[char]) {
        if (stack[stack.length - 1] === pairs[char]) {
          stack.pop();
        } else {
          sum += points[char];
          file[i] = false;
          break;
        }
      } else {
        stack.push(char);
      }
    }
  }
  return sum;
}
console.log(sumIncorrectSyntax(file));

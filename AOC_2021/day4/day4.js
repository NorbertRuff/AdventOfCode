const fileReader = require("../fileReader");

let file = fileReader("./input.txt");

// const lines = file.toString().split("\n")[0];
// inputs = inputs.split(",");
// let boards = file.toString().split("\n\n");
// boards.shift();

// boards = boards.map((board) => {
//   board = board
//     .split("\n")
//     .map((board) => board.split(/[\s]+/).filter((board) => board !== ""))
//     .filter((board) => board.length !== 0);
//   return board;
// });

// for (let number of inputs) {
//   for (let board of boards) {
//     board.forEach(function(item, i) { if (item == number) board[i] = 'x'; });
//   }
// }
// console.log(boards)

const getLines = () => file.split("\n").map((t) => t.trim());
const getNumbers = (lines) => {
  return lines[0].split(",").map(Number);
};

const hasBingo = (board, numbers) => {
  for (let i = 0; i < 5; i++) {
    if (
      board[i].every((c) => numbers.includes(c)) ||
      board.map((elem) => elem[i]).every((c) => numbers.includes(c))
    ) {
      return true;
    }
  }
  return false;
};

const generateBoards = (lines) => {
  let boards = [];
  for (let i = 0; i < (lines.length - 1) / 6; i++) {
    boards[i] = [];
    for (let j = 1; j < 6; j++) {
      boards[i][j - 1] = lines[i * 6 + j + 1].match(/(\d+)/g).map(Number);
    }
  }
  return boards;
};

const part1 = () => {
  let lines = getLines();
  let numbers = getNumbers(lines);
  let boards = generateBoards(lines);

  for (let i = 5; i <= numbers.length; i++) {
    let sublist = numbers.slice(0, i);
    let winningBoard = boards.find((b) => hasBingo(b, sublist));

    if (winningBoard) {
      return (
        numbers[i - 1] *
        winningBoard.reduce(
          (s, row) =>
            s +
            row
              .filter((r) => !sublist.includes(r))
              .reduce((sum, a) => sum + a, 0),
          0
        )
      );
    }
  }
};

const part2 = () => {
  let lines = getLines();
  let numbers = getNumbers(lines);
  let boards = generateBoards(lines);

  for (let i = 5; i <= numbers.length; i++) {
    let sublist = numbers.slice(0, i);
    if (boards.length > 1) {
      boards = boards.filter((b) => !hasBingo(b, sublist));
    } else if (hasBingo(boards[0], sublist)) {
      return (
        numbers[i - 1] *
        boards[0].reduce(
          (s, row) =>
            s +
            row
              .filter((r) => !sublist.includes(r))
              .reduce((sum, a) => sum + a, 0),
          0
        )
      );
    }
  }
};

console.log(part1());
console.log(part2());

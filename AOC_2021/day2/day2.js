const fileReader = require("../fileReader");

const input = fileReader("./input.txt").split('\n');


const calculateMove = (input) => {
  let horizontal = 0;
  let aim = 0;
  let depth = 0;

  for (let element of input) {
    let coord = element.split(" ");
    if (coord[0] == "forward") {
      handleForward(coord);
    }
    if (coord[0] == "down") {
        handleDown(coord);
    }
    if (coord[0] == "up") {
        handleUp(coord);
    }
  }
  return horizontal * depth;

  function handleUp(coord) {
    aim -= parseInt(coord[1]);
  }

  function handleDown(coord) {
    aim += parseInt(coord[1]);
  }

  function handleForward(coord) {
    horizontal += parseInt(coord[1]);
    depth += parseInt(coord[1]) * aim;
  }
}


const result = calculateMove(input);
console.log(result);

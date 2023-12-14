const fileReader = require("../fileReader");

const file = fileReader("./input.txt").split("\n");
const matrix = file.map((line) => [...line].map((element) => +element));


console.log(matrix);
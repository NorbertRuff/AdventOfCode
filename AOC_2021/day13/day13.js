const fileReader = require("../fileReader");

const file = fileReader("./input.txt").split("\n\n");

const coords = file[0].split("\n");
const folds = file[1].split("\n");

const generateMatrix = () => {
  let array2d = [];

  coords.forEach((data) => {
    const coordsArr = data.split(",");
    const y = parseInt(coordsArr[1]);
    const x = parseInt(coordsArr[0]);

    if (array2d[y] === undefined) {
      array2d[y] = [];
    }

    array2d[y][x] = "#";
  });
  return array2d;
};

let array2d = generateMatrix();
// console.log(folds);

const foldCoord = folds.map((foldData) => {
  return foldData.replace("fold along ", "");
});

// console.log(foldCoord);

for (let coord of foldCoord) {
  if (coord.indexOf("y=") === 0) {
    const splitByYCoord = parseInt(coord.replace("y=", ""));

    for (let downCoord = splitByYCoord - 1; downCoord >= 0; downCoord--) {
      let upCoord = splitByYCoord + splitByYCoord - downCoord;

      if (!array2d[upCoord]) {
        continue;
      }

      array2d[upCoord].forEach((colData, colIndex) => {
        if (colData === "#") {
          if (array2d[downCoord] === undefined) {
            array2d[downCoord] = [];
          }

          array2d[downCoord][colIndex] = "#";
        }
      });
    }
    array2d = array2d.slice(0, splitByYCoord);
  }

  if (coord.indexOf("x=") === 0) {
    const splitByXCoord = parseInt(coord.replace("x=", ""));

    array2d.forEach((rowData, rowIndex) => {
      for (let leftCoord = splitByXCoord - 1; leftCoord >= 0; leftCoord--) {
        let rightCoord = splitByXCoord + splitByXCoord - leftCoord;

        if (array2d[rowIndex][rightCoord] === "#") {
          array2d[rowIndex][leftCoord] = "#";
        }
      }

      array2d[rowIndex] = array2d[rowIndex].slice(0, splitByXCoord);
    });
  }
}

// console.log(array2d);

const printWord = () => {
  array2d.map((rowData) => {
    let newRow = "";

    for (let i = 0; i < rowData.length; i++) {
      const cellData = rowData[i];

      if (!cellData) {
        newRow += " ";
      } else {
        newRow += cellData;
      }
    }
    console.log(newRow);
  });
};


printWord();

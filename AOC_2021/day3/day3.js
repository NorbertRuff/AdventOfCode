const fileReader = require("../fileReader");

let input = fileReader("./input.txt").split('\n');

const getGammaRate = () => {
  let result = "";
  for (let i = 0; i < input[0].length; i++) {
    let zeroCount = 0;
    let oneCount = 0;
    for (let binaryCode of input) {
      if (binaryCode[i] === "0") {
        zeroCount++;
      } else {
        oneCount++;
      }
    }
    zeroCount < oneCount ? (result += "1") : (result += "0");
  }
  return result;
};

const getEpsilonRate = () => {
  let result = "";
  for (let i = 0; i < input[0].length; i++) {
    let zeroCount = 0;
    let oneCount = 0;
    for (let binaryCode of input) {
      if (binaryCode[i] === "0") {
        zeroCount++;
      } else {
        oneCount++;
      }
    }
    zeroCount < oneCount ? (result += "0") : (result += "1");
  }
  return result;
};

const binaryDiagnostic = (input) => {
  let gammaRate = getGammaRate();
  let epsilonRate = getEpsilonRate();
  return parseInt(gammaRate, 2) * parseInt(epsilonRate, 2);
};

const getLifeSupportRating = () => {
  let counter = 0;
  const find = (items, operation) => {
    let zeroCount = 0;
    let oneCount = 0;
    items.map((item) => (item[counter] == 1 ? oneCount++ : zeroCount++));
    let binaryChar = oneCount >= zeroCount ? 1 : 0;
    if (operation === "findRare") {
      binaryChar = oneCount < zeroCount ? 1 : 0;
    }
    const filtered = items.filter((item) => (item[counter] == binaryChar ? item : null));
    counter++;
    if (filtered.length > 1) return find(filtered, operation);
    return filtered;
  };

  const oxygenGeneratorRating = parseInt(find(input, "findRare").join(""), 2);
  counter = 0;
  const COScrubberRating = parseInt(find(input, "findCommon").join(""), 2);
  return(oxygenGeneratorRating * COScrubberRating);
};

console.log(binaryDiagnostic())
console.log(getLifeSupportRating())


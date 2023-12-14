const fileReader = require("../fileReader");

let file = fileReader("./input.txt");

// const  getInput = async() => {
//   const result = await axios
//     .get("https://adventofcode.com/2021/day/1/input", {
//       headers: {
//         accept:
//           "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
//         "accept-language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7",
//         cookie:
//           "_ga=GA1.2.2059448827.1638723865; _gid=GA1.2.1131151960.1638723865; session=53616c7465645f5f0598921eb6939d8ece2a72eea098dd262811e2e3297f959db3643fb2dc74e363c66d24970fcb56dd",
//       },
//       referrerPolicy: "strict-origin-when-cross-origin",
//       body: null,
//       method: "GET",
//     })
//     .then((res) => {
//       return res.split('\n');
//     })
//     .catch((err) => {
//       console.log("Error: ", err.message);
//     });
//     console.log(result);
// };
function countLargerThanPrev(values, blockSize = 1) {
    let largerThanPrev = 0

    for (let i = blockSize; i < values.length; i++) {        
        const prev = Number(values[i - blockSize])
        const curr = Number(values[i])
        const diff = curr - prev
        if (diff > 0) largerThanPrev++
    }

    return largerThanPrev
}

console.log(countLargerThanPrev(file, 3))
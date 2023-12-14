const fileReader = require("../fileReader");

let file = fileReader("./input.txt").split(",");
// let file = ["1", "2", "4", "4"];



function countFish(input, days) {
    const array = simulate(input)
  
    for (let i = 0; i < days; i++) {
      const canBorn = array.shift()
  
      if (canBorn) {
        array[6] += canBorn
        array.push(canBorn)
      } else {
        array.push(0)
      }
    }
  
    return array.reduce((a, b) => a + b, 0)
  }
  
  function simulate(input) {
    const array = Array(9).fill(0)
    input.forEach(val => {
      array[parseInt(val)]++
    })
    return array
  }
  
  console.log(countFish(file, 80))
  console.log(countFish(file, 256))

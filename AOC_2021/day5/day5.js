const fileReader = require("../fileReader");

let file = fileReader("./input.txt").split("\n");
let coords = file.map(x=>x.split(' -> '));
coords = coords.map(x=>x.map(y=>y.split(',')));

console.log(coords[0]);

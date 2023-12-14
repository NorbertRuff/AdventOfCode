const fs = require('fs')


const fileReader = (filename) => {
    return fs.readFileSync(filename, {encoding: 'utf8'})
}


module.exports = fileReader
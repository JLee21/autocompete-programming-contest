const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function (line) {
  console.log(reverse(line))
});

function reverse(line) {
  let ss = ''
  for (let i = line.length - 1; i >= 0; i--) {
    ss += line.charAt(i)
  }
  return ss
}


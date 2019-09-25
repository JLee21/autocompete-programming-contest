### Team name: __________________ GitHub URL: ____________________________

## Flatiron Seattle AutoCompete Rules
* Up to three people per team
* Only one computer per team
* Pen and paper will be provided
* Internet access is allowed (though probably mostly unuseful)
* No third party libraries (no gems, no pip, no npm, etc)
* You may solve problems in any order
* Rankings are ordered by the number of problems solved and time taken

Follow the directions about how to read program input below.  Write one program
called `reverse` that reads from STDIN line-by-line and prints out each line
reversed. Commit your program to the repo.

Fill out your team name and provide a GitHub URL and bring this paper to the
judge table. The judges will confirm they are able to run your program and that
it properly reads input and produces reversed text.

## Sample Boiler Plate
All of the programs are required to read input from STDIN (standard input).
Each language has it's own way of accessing this input. Here are samples to
get you started. You can use this boilerplate to build the rest of your
programs around, or read from STDIN any other way you wish. Judges will run
your program by piping text into it via `cat`.

```
cat input | python foo.py
cat input | ruby foo.rb
cat input | node foo.js
```

Try this out to make sure your programs execute correctly!

```py
#python
import fileinput
for line in fileinput.input():
  print(line)
```

```ruby
# ruby
lines = ARGF.read.split("\n")
lines.each do |line|
  puts line
end
```

```js
// javascript
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

const lines = []
rl.on('line', (line) => lines.push(line));
rl.on('close', (line) => compute(lines));

function compute(lines) { console.log(lines) }
```

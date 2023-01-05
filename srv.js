const http = require('http');

const hostname = "localhost";
const port = 3000;

class Person {
  constructor(date) {
    this.birthday = date;
  }
}

let myBirthday = new Date(1998, 1, 1);
let me = new Person(myBirthday);

class View {
  constructor(person) {
    this.person = person;
    this.now = new Date();
    this.year = [];
    this.text = "";
    this.init(person);
  }
  init(person) {
    let currYr = this.now.getFullYear();
    // for (let eachMod = person.birthday.getMonth(); eachMod < 12; eachMod++) {
    //   this.year.push()
    // }
    this.text += '<style type="text/css">';
    this.text += ' .week{ height: 10px;width: 10px; margin-left: 1px;margin-bottom: 1px;margin-right: 1px;margin-top: 1px;} ';
    this.text += ' .year-div{ line-height:8px } ';
    this.text += ' .year-txt{ line-height:10px; font-size: 10px; } ';
    this.text += '</style>\n';
    let limit = person.birthday.getFullYear() + 80;
    for (let eachYr = person.birthday.getFullYear();
        eachYr < limit;
        eachYr++) {
      let tmpDate = new Date(eachYr, 0, 1);
      while (tmpDate.getDay() != 0) {
        tmpDate.setDate(tmpDate.getDate() + 1);
      }
      console.log('yr = %d', eachYr);
      this.text += '<div class="year-div"> <span class="year-txt">' + eachYr + '</span>' + "\n";
      for (;
        tmpDate.getFullYear() == eachYr;
        tmpDate.setDate(tmpDate.getDate() + 7)) {
        this.text += '<input type="checkbox" class="week"' + (tmpDate < this.now ? " checked " : "") + "/>";
      }
      this.text += "</div>" + "\n";
    }
    // console.log("%s", this.text);
  }
  getText() {
    return this.text;
  }
}

class WeekOfYear {
  constructor() {

  }
}
console.log("hello")
let date = new Date();

let view = new View(me);

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html; charset=UTF-8');
  res.end('你好世界\n' + view.getText());
})

server.listen(port, () => {
  console.log(`服务器运行在 http://${hostname}:${port}/`);
});

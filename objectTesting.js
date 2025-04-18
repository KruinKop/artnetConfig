class Person {
    constructor(naam, leeftijd, beroep) {
        this.naam = naam;
        this.leeftijd = leeftijd;
        this.beroep = beroep;
    }
}

class Bedrijf {
    constructor() {
        this.team = [];
        this.topEmployer;
    }
}

let LL = new Bedrijf;
let p1 = new Person("JJ", 30, "Developer");
let p2 = new Person("TT", 35, "Hardware");
let p3 = new Person("JT", 33, "Manager");

LL.team.push(p1, p2, p3);
LL.topEmployer = p2;

console.log(LL.team);
LL.team[1].leeftijd = 50;
console.log(LL.topEmployer)


class Person {
  constructor (firstName, lastName, age){
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
    this.eyes = 2
    this.legs = 2
    this.alwaysLazy = true
  }
}

Person.prototype.fullname = function(){
  return this.firstName + " " + this.lastName
}

const person1 = new Person("Rynn", "Lee", 19)
console.log(person1.fullname())

//----------------------------------------------------------

let head = {
  glasses: 1
};

let table = {
  pen: 3,
  __proto__: head
};

let bed = {
  sheet: 1,
  pillow: 2,
  __proto__: table
};

let pockets = {
  money: 2000,
  __proto__: bed
};

console.log(pockets.pen) // 3
console.log(bed.glasses) // 1

//----------------------------------------------------------
let hamster = {
  stomach: [],

  eat(food) {
    this.stomach.push(food);
  }
};

let speedy = {
  stomach: [],
  __proto__: hamster
};

let lazy = {
  stomach: [],
  __proto__: hamster
};

speedy.eat("apple");
console.log( speedy.stomach ); // apple
console.log( lazy.stomach ); // should be empty
class Entity {
  constructor (name, age){
    this.name = name
    this.age = age
    this.vegan = false
    this.eyes = 2
    this.legs = 2
    this.canSpeak = false
    this.predator = true
    this.sound = "MHHHHM"
  }
  makeSound(){
    if(!this.canSpeak){
      console.warn(`${this.name} cannot speak!`)
      return
    }
    console.log(this.sound)
  }
}

class Bird extends Entity{
  constructor (name, age){
    super(name, age)
    this.vegan = false
    this.canSpeak = true
    this.predator = false
    this.sound = "Tip! Tiptiptip!"
  }
}

class Person extends Entity{ 
  constructor (name, age, country) {
    super(name, age)
    this.country = country
    this.canSpeak = true
    this.predator = false
    this.sound = "Wife, kids, job, kill me aAAAAAAH!!!!!!!"
  }
}

class Ant extends Entity {
  constructor (name, age){
    super(name, age)
    this.legs = 8
  }
}

const person = new Person("Rosette", 18, "Canada")
const bird = new Bird("Sparrow", 1)
const ant = new Ant("FireAnt")

person.makeSound()
bird.makeSound()
ant.makeSound()
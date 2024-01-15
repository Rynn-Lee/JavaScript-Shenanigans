function greetings(name){
  const message = "gell"
  function sayHello(){console.log(message + name)}
  return sayHello
}

const helloJohn = greetings('john')
helloJohn()
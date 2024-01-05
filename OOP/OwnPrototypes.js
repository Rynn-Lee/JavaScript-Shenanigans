if(!Object.prototype.keysToString){
  Object.prototype.keysToString = function(decorator){
    return Object.keys(this).join(decorator ? decorator : " ")
  }
}

const object = {
  "Ехал": 1,
  "Грека": 2,
  "Через": 3,
  "Реку": 4,
  "Видит": 5,
  "Грека": 6,
  "В": 7,
  "Реке": 8,
  "Рак": 9
}

console.log(object.keysToString("+"))

// ------------------------------------------------------------

if(!Function.prototype.delay){
  Function.prototype.delay = function(time){
    let fn = this
    return function(...args){
      setTimeout(()=>fn.apply(this, args), time)
    }
  }
}

function showText(a, b){
  console.log("Solved:", a + b)
}

showText.delay(1000)(1,2)


// ------------------------------------------------------------

function slow(x){
  for(let i = 0; i <= x; i++){
    if(i == x){console.log("Done counting")}
  }
  return x
}

function cachingDecorator(func){
  let cache = new Map()

  return function(x){
    if(cache.has(x)){
      return cache.get(x)
    }
    let result = func.call(this, x)
    cache.set(x, result)
    return result
  }
}

slow = cachingDecorator(slow)

console.log(slow(3000000000))
console.log("Calling again")
console.log(slow(3000000000))
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
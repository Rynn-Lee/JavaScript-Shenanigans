const playground = document.getElementById("playground")
let color = {r: 90, g: 90, b: 90};
let currentColor = 'r';
let direction = 1

let lastCoords = {
  x: 0,
  y: 0,
  timestamp: Date.now()
}

const colors = [
  "red", "coral", "yellow", "chocolate", "crimson", "gold", "darkgoldenrod"
]



window.addEventListener('mousemove', (event) => {
  const timeDiff = Date.now() - lastCoords.timestamp
  if(timeDiff > 400 || trackDistance(lastCoords, {x: event.clientX, y: event.clientY}, 0)){
    lastCoords.x = event.clientX
    lastCoords.y = event.clientY
    lastCoords.timestamp = Date.now()
    createDot()
  }
})

const trackDistance = (first, second, distance) => {
  if(Math.abs(first.x - second.x) >= distance)
    return true
  if(Math.abs(first.y - second.y) >= distance)
    return true
  return false
}

const colorFlow = () => {
  color[currentColor] += direction;

    if(color[currentColor] >= 255) {
        direction = -3;
    } else if(color[currentColor] <= 90) {
        direction = 3;
        currentColor = currentColor === 'r' ? 'g' : currentColor === 'g' ? 'b' : 'r';
    }

  let hexColor = '#' + Object.values(color).map(c => c.toString(16).padStart(2, '0')).join('');
  playground.innerHTML = `color: ${hexColor}`

  return hexColor
}

const createDot = (coords) => {
  const dot = document.createElement("span")
  dot.style.left = event.clientX + "px"
  dot.style.top = event.clientY + "px"
  dot.style.background = `${colorFlow()}`
  dot.className = "dot"
  document.body.appendChild(dot)
  setTimeout(()=>{
    document.body.removeChild(dot)
  }, 2000)
}
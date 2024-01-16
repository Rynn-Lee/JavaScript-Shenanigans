var countrycode = document.getElementById("country-code")
countrycode.innerHTML = "Everrynn✨"
let removedButtons = false
let removedShorts = false


const obliterateButtons = () => {
  const PCButtons = document.getElementsByClassName("yt-simple-endpoint")
  const MiniButtons = document.getElementsByTagName("ytd-mini-guide-entry-renderer")

  if((!PCButtons.length || !MiniButtons.length) && !removedButtons){
    setTimeout(()=>{
      obliterateButtons()
      console.log("AGAIN BUTTONS", removedButtons)
    }, 100)
    return
  }
  removedButtons = true
  for(let i = 0; i < PCButtons.length; i++){
    let button = PCButtons[i]
    if(button.getAttribute('title') == "Shorts"){button.remove()}
  }
  
  for(let i = 0; i < MiniButtons.length; i++){
    let button = MiniButtons[i]
    if(button.getAttribute('aria-label') == "Shorts"){button.remove()}
  }
}
const obliterateShorts = () => {
  var shortsShelves = document.getElementsByTagName("ytd-reel-shelf-renderer")
  var shortsShelvesRich = document.getElementsByTagName("ytd-rich-shelf-renderer")
  if((!shortsShelves.length && !shortsShelvesRich.length) && !removedShorts){
    setTimeout(()=>{
      obliterateShorts()
    }, 100)
    return
  }
  removedShorts = true
  for(let i = 0; i < shortsShelves.length; i++){
    let shelve = shortsShelves[i]
    shelve.remove()
  }
  for(let i = 0; i < shortsShelvesRich.length; i++){
    let shelve = shortsShelvesRich[i]
    shelve.remove()
  }
}

window.onload = function(){
    obliterateShorts()
    obliterateButtons()
}

window.addEventListener('popstate', function (event) {
    obliterateShorts()
    alert("ERROR:", error)
});


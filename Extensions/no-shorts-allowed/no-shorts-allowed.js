const obliterateButtons = () => {
  const PCButtons = document.getElementsByClassName("yt-simple-endpoint")
  const MiniButtons = document.getElementsByTagName("ytd-mini-guide-entry-renderer")
  if(!PCButtons.length && !MiniButtons.length){return}
  for(let i = 0; i < PCButtons.length; i++){
    let button = PCButtons[i]
    if(button.getAttribute('title') == "Shorts"){button.remove()}
  }
  for(let i = 0; i < MiniButtons.length; i++){
    let button = MiniButtons[i]
    if(button.getAttribute('aria-label') == "Shorts"){button.remove()}
  }
  setTimeout(obliterateButtons, 100)
}
const obliterateShorts = () => {
  var shortsShelves = document.getElementsByTagName("ytd-reel-shelf-renderer")
  var shortsShelvesRich = document.getElementsByTagName("ytd-rich-shelf-renderer")
  if(!shortsShelvesRich.length && !shortsShelves.length){return}
  for(let i = 0; i < shortsShelves.length; i++){
    let shelve = shortsShelves[i]
    shelve.remove()
  }
  for(let i = 0; i < shortsShelvesRich.length; i++){
    let shelve = shortsShelvesRich[i]
    shelve.remove()
  }
  setTimeout(obliterateShorts, 100)
}

const changeCountry = () => {
  let countrycode = document.getElementById("country-code")
  if(countrycode.innerHTML == "Everrynn✨"){return}
  countrycode.innerHTML = "Everrynn✨"
  changeCountry()
}

const checkIfShortsPage = () => {
  let pathArray = window.location.pathname.split('/');
  if(!pathArray.includes("shorts")){return}
  window.location.replace("https://leetcode.com/problemset/");
} 

const resized = () => {
  changeCountry()
  obliterateShorts()
  obliterateButtons()
  checkIfShortsPage()
}

window.onload = function(){
  changeCountry()
  obliterateShorts()
  obliterateButtons()
  checkIfShortsPage()
}

window.addEventListener('popstate', function (event) {
  changeCountry()
  obliterateShorts()
  checkIfShortsPage()
}, {passive: true});

let resizeTimer;
window.onresize = function(){
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(resized, 100);
};
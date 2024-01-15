var shortsShelves = document.getElementsByTagName("ytd-reel-shelf-renderer")
var shortsShelvesRich = document.getElementsByTagName("ytd-rich-shelf-renderer")
var countrycode = document.getElementById("country-code")

countrycode.innerHTML = "Everrynn✨"

const obliterateShorts = (shorts) => {
  for(let i = 0; i < shorts.length; i++){
    let shelve = shorts[i]
    shelve.innerHTML = ""
    shelve.style.display = "none"
  }
}

window.onload = function(){
  try{
    obliterateShorts(shortsShelves)
    obliterateShorts(shortsShelvesRich)
  } catch (error) {
    alert("ERROR:", error)
  }
}

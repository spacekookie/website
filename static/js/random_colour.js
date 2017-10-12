
var elements = document.getElementsByClassName('naughty');

for (var i = 0; i < elements.length; i++) {
  var randomColor = "#"+((1<<24)*Math.random()|0).toString(16);

  elements[i].style.color = randomColor;
}

  // console.log("Calling random colour code!" + randomColor);

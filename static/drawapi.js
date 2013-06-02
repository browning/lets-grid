function random_color() {
  function c() {
    return Math.floor(Math.random()*256).toString(16)
  }
  return "#"+c()+c()+c();
}

function draw(x,y,color) {
	color = typeof color !== 'undefined' ? color : 'black';
	
	$("#grid_" + x + "_" + y).css('background-color', color);
}



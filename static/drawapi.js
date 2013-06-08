function random_color() {
  function c() {
    return Math.floor(Math.random()*256).toString(16)
  }
  return "#"+c()+c()+c();
}

function draw(x,y,color) {
	color = typeof color !== 'undefined' ? color : 'black';
	
	$("#grid_" + y + "_" + x).css('background-color', color);
}

function clear_grid() {

	for (x=0; x<20; x++) {
		for(y=0; y<25; y++) {
			$("#grid_" + y + "_" + x).css('background-color', '');
		}
	}
}



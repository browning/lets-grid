messages = new Array();

function post_messages() {
	if (messages.length > 0 ) {
		postMessage(messages)
	}
}

setInterval(post_messages, 50);

function draw(x,y,color) {
	color = typeof color !== 'undefined' ? color : 'black';
	var i = messages.length;
	while (i--) {
    	if(messages[i].x == x && messages[i].y == y){
    		messages.splice(i,1);
    	}
	}
	messages.push({'x': x, 'y':y, 'color':color});
}

function clear_grid() {
	messages.push({'x': 0, 'y':0, 'color':'clear'});
}

onmessage = function (oEvent) {
  eval(oEvent.data);
};
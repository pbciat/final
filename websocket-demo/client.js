var websocket = new WebSocket("ws://127.0.0.1:8765/");
var times = 0;
var detect_key = true;
var start = new Date().getTime();


/*
ToDo: Ignore keys other than space on staring or interval trials
*/
document.onkeydown = function(e){
    e = e || window.event;
    
    
    if (detect_key && ( (e.keyCode == 69 || e.keyCode == 73) || e.keyCode == 32) ) {
        // pressed left key
        if (e.keyCode == 69){   // keycode for e   i: 73
            RT = getRT();
            correct = (data.answer == 'left') ? 'true':'false';
            if (data.answer == 'right') {
                document.getElementById("content-text").innerHTML = 'WRONG';
            }
            
        // pressed right key
        } else if (e.keyCode == 73) {
            RT = getRT();
            correct = (data.answer == 'right') ? 'true':'false';
            if (data.answer == 'left') {
                document.getElementById("content-text").innerHTML = 'WRONG';
            }
        // first trial: pressed space
        } else {
            RT = -1;
            correct = 'false'
            document.getElementById("content-text").innerHTML = 'Get Ready';
        }
        
        // Clean up if Correct
        if (correct == 'true') {
            document.getElementById("content-text").innerHTML = '';
        }
        
        // Print RT on browser for feed back (remove later)
        document.getElementById("rt").innerHTML = 'RT: ' + RT + 'sec';
        
        // send data to server
        sending = {'correct': correct, 'rt': RT}
        websocket.send(JSON.stringify(sending))
        detect_key = false
    }
}


/*
block: 3
type: text 
content: 真誠
answer: left
*/
websocket.onmessage = function (event) {
    data = JSON.parse(event.data);
    
    if (data.block == '3') {
        // present button layouts: pos & DPP on left
        document.getElementById("left-cue1").innerHTML = '正向';
        document.getElementById("left-cue2").innerHTML = '民進黨';
        document.getElementById("right-cue1").innerHTML = '負向';
        document.getElementById("right-cue2").innerHTML = '國民黨';
        
        // present stimulus
        if (data.type == 'text') {
            document.getElementById("content-text").innerHTML = data.content
        } else if (data.type == 'img') {
            document.getElementById("content-img").src = data.content;
        } else {
            console.log('data.type not text nor img')
        }
    }
    
    // start timer
    start = new Date().getTime();
    //document.getElementById("fserver").innerHTML = event.data;
    detect_key = true
};






function getRT() {
    var end = new Date().getTime();
    var timeTaken = (end - start) / 1000;
    return timeTaken
}

function dummy(){}; 

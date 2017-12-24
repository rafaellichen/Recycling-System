$(document).ready(function() {
	 // document.getElementById("logo-png").className+= " img-fluid";

    //send the message by click
    $(".chat-send").click(sendMsg);

    //press enter to send
    $("form").keypress(function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            sendMsg();
        }
    });

    //clear the chat box
    $(".chat-clear").click(clearChatBox);

    //reset the chat box
    $(".chat-reset").click(resetChatBox);
});

//send message to chat box
function sendMsg() {
    var msg = $(".chat-message");
    var msgVal = msg.val();
    var chatBox = $(".chat-box");
    if (msgVal) {
        var msgAppend = "<p><span id='you'>You: </span>" + msgVal + "</p><hr class='you-hr'>";
        chatBox.append(msgAppend);
    } else {}

    //dialog reply
    dialog(msgVal);

    //empty input
    msg.val("");

    //keep the scroll in bottom
    chatBox.scrollTop(chatBox[0].scrollHeight);
}

//clear the chat box
function clearChatBox() {
    alert("Clean Now!!");
    $(".chat-box").html("");
}

//reset the chat box
function resetChatBox() {
    $(".chat-box").html("");  
}

//set up the AI dialog
function dialog(msg){
    var replyArr = ["Hi, this is Easy Recycle! How can I help you?(hints:how it works, how it charges)","Just login or find something in home page!","Our service is totally free!","Call us right now!", "We open Monday-Friday from 10:00AM-06:00PM","My name is Easy Recycle","You could see and leave a feedback on your profile","Sorry, I don't understand!"];
    msg = msg.toLowerCase();
    var time = new Date();
    var hour = time.getHours();
    var minute = time.getMinutes();
    var currentTime = plusZero(hour) + ":" + plusZero(minute);

    var chatBox = $(".chat-box");

    if(msg.indexOf("hi") != -1 || msg.indexOf("hello") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[0] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("work") != -1 || msg.indexOf("how it works") != -1 || msg.indexOf("where can i find recycling center") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[1] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("charge") != -1 || msg.indexOf("how it charges") != -1 || msg.indexOf("how much should i pay") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[2] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("help") != -1 || msg.indexOf("I need help") != -1 || msg.indexOf("I have other problems") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[3] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("what is your office time") != -1 || msg.indexOf("office time") != -1 || msg.indexOf("visit time") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[4] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("name") != -1 || msg.indexOf("your name") != -1 || msg.indexOf("what is your name") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[5] + "</p><hr class='ai-hr'>");
    }
     else if(msg.indexOf("feedback") != -1 || msg.indexOf("where can I see feedback") != -1 || msg.indexOf("how good is your website") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[6] + "</p><hr class='ai-hr'>");
    }
    else if(msg.indexOf("time") != -1){
        chatBox.append("<p><span id='ai'>Customer Service: </span>Current Time: " + currentTime + ". " + timeGreeting(hour) + "~ :)</p><hr class='ai-hr'>");
    }
    else {
        chatBox.append("<p><span id='ai'>Customer Service: </span>" + replyArr[7] + "</p><hr class='ai-hr'>");
    }
}

//add 0 if time number is <10
function plusZero(x){
    if(x < 10){
        x = "0" + x;
    }
    else {
        x = x;
    }
    return x;
}

//greeting by hour
function timeGreeting(h){
    var greeting = ["U need to sleep","Good morning","Lunch time now","Feel asleep? Have some coffee","Free time~Yeah","Good night"];

    if(h>=0&&h<=6){
        return greeting[0];
    }
    else if(h>=7&&h<=10){
        return greeting[1];
    }
    else if(h>=11&&h<=13){
        return greeting[2];
    }
    else if(h>=14&&h<=18){
        return greeting[3];
    }
    else if(h>=19&&h<=21){
        return greeting[4];
    }
    else if(h>=22&&h<=23){
        return greeting[5];
    }
    else {
        return "";
    }
}




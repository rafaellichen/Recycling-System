$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
});

function togglemore() {
  more='<br><img data-toggle="collapse" href="#List1" aria-expanded="false" aria-controls="List1" src="/static/img/plus.png" style="width:60px; height:60px"><br>More'
  less='<br><img data-toggle="collapse" href="#List1" aria-expanded="false" aria-controls="List1" src="/static/img/minus.png" style="width:60px; height:60px"><br>Less'
  if(document.getElementById("more").innerHTML==more) {
    document.getElementById("more").innerHTML=less
  } else {
    document.getElementById("more").innerHTML=more
  }
}
function validForm() {
    var x = document.getElementsByName("gtype")
    typeSelect=false
    for(var i=0; i<x.length; i++) {
      if(x[i].checked) {
       typeSelect=true
      }
    }
    if(typeSelect==false){
      alert("Please select at least 1 type of recyclable waste")
    }
    return (typeSelect)
  }

function time() {
       t_div = document.getElementById('showtime');
      var now = new Date();
       t_div.innerHTML = "Current Time: " + now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate() + " " + " " +now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds() + " ";
       setTimeout(time, 1000);
  }

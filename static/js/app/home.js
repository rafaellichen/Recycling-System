$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function setToggleStatus(selectedTypes, days) {
  console.log(selectedTypes);
  selectedTypes = $.map(selectedTypes, function(str) {
    return str.replace(/ /g, '_');
  })
  console.log(selectedTypes);
  for (var each in selectedTypes) {
    $("#"+selectedTypes[each]).addClass('active');
  }
  if (days) {
    for (var day in days) {
     $("#"+days[day]).addClass('active');
    }
  }
}

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

const updateBookmarkItem = (idc, param) => {
  let className = 'bookmark fa fa-3x fa-bookmark';
  let title;
  if (param == 'add')  {
     param = 'remove';
     title = 'remove from favorites';
  }
  else {
    param='add'
    className+='-o';
    title = 'add to favorites';
  }

  $(`#${idc}> i`).attr({
    'class': className,
    'title':title,
    'id':param,
  });
};

const status = (response) => {
    if (response.status >= 200 && response.status < 300) {
      return Promise.resolve(response)
    } else {
      return Promise.reject(new Error(response.statusText))
    }
};

const json = (response) => {
    return response.json();
};

const bookmarkHandler = e =>{
      let param = e.target.getAttribute('id');
      let idc = e.target.parentElement.getAttribute('id');
      let csrftoken = $("[name=csrfmiddlewaretoken]").val();
      fetch('/bookmarks', {
        "method": 'POST',
        "body": JSON.stringify({idc: idc, param: param}),
        "credentials": 'include',
        "headers": {
          "X-CSRFToken": csrftoken,
          "Accept": "application/json",
          "Content-Type": "application/json",
        }
      }).then(res => {
        return res.json();
      })
      .then(res => {
          res['result'] == 'success'?
            updateBookmarkItem(idc, param):
            console.log(res);
      })
      .catch(err=> console.log(err))
};

document.querySelectorAll('.bookmark').forEach ( el => el.addEventListener('click', bookmarkHandler));

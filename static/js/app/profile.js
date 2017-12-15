const updateBookmarks = (idc) => {
  document.querySelector(`#bookmark-${idc}`).remove()
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

const deleteBookmark = e =>{
      param = e.target.getAttribute('id');
      idc = e.target.parentElement.getAttribute('id');
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
            updateBookmarks(idc, param):
            console.log(res);
      })
      .catch(err=> console.log(err))
};

document.querySelectorAll('.bookmark').forEach ( el => el.addEventListener('click', deleteBookmark));

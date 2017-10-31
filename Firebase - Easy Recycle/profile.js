// Initialize Firebase
const config = {
    apiKey: "AIzaSyASyS2PmeJsALxQOPvH13BgrA0YuM315fM",
    authDomain: "recycling-system.firebaseapp.com",
    databaseURL: "https://recycling-system.firebaseio.com",
    projectId: "recycling-system",
    storageBucket: "recycling-system.appspot.com",
    messagingSenderId: "277884932249"
};
firebase.initializeApp(config);

// elements
const first_name = document.getElementById("First_Name")
const last_name = document.getElementById("Last_Name")
const phone = document.getElementById("Phone_Number")
const street1 = document.getElementById("Street_Address1")
const street2 = document.getElementById("Street_Address2")
const city = document.getElementById("City")
const state = document.getElementById("State")
const zip = document.getElementById("Zip_Code")
const donate = document.getElementById("donate")
const recycle = document.getElementById("recycle")

// signout
signout_Button.addEventListener("click",e=> {
    firebase.auth().signOut()
    window.location = "account.html"
})


// sync
firebase.auth().onIdTokenChanged(function(user) {
    if (user) {
        firebase.database().ref("/users/"+user.uid).on("value",function(snapshot) {
            first_name.value = snapshot.val().first_name
            last_name.value = snapshot.val().last_name
            phone.value = snapshot.val().phone
            street1.value = snapshot.val().street1
            street2.value = snapshot.val().street2
            city.value = snapshot.val().city
            state.value = snapshot.val().state
            zip.value = snapshot.val().zip
        })
        firebase.database().ref("/inventory/"+user.uid+"/donate").on("value",function(snapshot) {
            var op="<option id='' value=''>description</option>"
            var ans=""
            var count=0;
            for (key in snapshot.val()) {
                count++
                ans+=op.replace("description",snapshot.val()[key].description).replace("value=''", "value='"+snapshot.val()[key].type+"'").replace("id=''","id="+key)
            }
            donate.innerHTML = ans;
            donate.size = count>3?count:3;
        })
        firebase.database().ref("/inventory/"+user.uid+"/recycle").on("value",function(snapshot) {
            var op="<option id='' value=''>description</option>"
            var ans=""
            var count=0;
            for (key in snapshot.val()) {
                count++
                ans+=op.replace("description",snapshot.val()[key].description).replace("value=''", "value='"+snapshot.val()[key].type+"'").replace("id=''","id="+key)
            }
            recycle.innerHTML = ans;
            recycle.size = count>3?count:3;
        })
    } else {
        window.location = "account.html"
    }
});

// update
update_Button.addEventListener("click",e => {
    firebase.auth().onIdTokenChanged(function(user) {
        if (user) {
            firebase.database().ref("/users/"+user.uid).set({
                first_name: first_name.value,
                last_name: last_name.value,
                phone: phone.value,
                street1: street1.value,
                street2: street2.value,
                city: city.value,
                state: state.options[state.selectedIndex].value,
                zip: zip.value   
            }); 
        }
    }); 
})

// delete
delete_Button.addEventListener("click",e=> {
    var keys_donate=[]
    for(var i=0; i<donate.selectedOptions.length; i++) {
        keys_donate.push(donate.selectedOptions[i].id)
    }
    var keys_recycle=[]
    for(var i=0; i<recycle.selectedOptions.length; i++) {
        keys_recycle.push(recycle.selectedOptions[i].id)
    }
    firebase.auth().onIdTokenChanged(function(user) {
        if(user) {
            for(var i=0; i<keys_donate.length; i++) {
                firebase.database().ref("/inventory/"+user.uid+"/donate/"+keys_donate[i]).remove()
            }
            for(var i=0; i<keys_recycle.length; i++) {
                firebase.database().ref("/inventory/"+user.uid+"/recycle/"+keys_recycle[i]).remove()
            }
        }
    })
})
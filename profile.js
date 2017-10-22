(function() {
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
    const first_name = document.getElementById('First_Name')    
    const last_name = document.getElementById('Last_Name')
    const phone = document.getElementById('Phone_Number')
    const street1 = document.getElementById('Street_Address1')
    const street2 = document.getElementById('Street_Address2')
    const city = document.getElementById('City')
    const state = document.getElementById("State").options[document.getElementById("State").selectedIndex]
    const zip = document.getElementById('Zip_Code')

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
                    state: state,
                    zip: zip.value   
                }); 
            }
        }); 
    })
}())
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
const trash_type_select = document.getElementById('trash-type-select')
const add = document.getElementById('add')
const description = document.getElementById('description')
const bottom = document.getElementById("bottom")

firebase.auth().onAuthStateChanged(function(user) {
    if (!user) {
        trash_type_select.style.display="none";
        add.style.display="none";
        description.style.display="none";
        bottom.style.border="none";
        bottom.style.marginBottom = "-130px";
    }
});

add.addEventListener("click",e => {
    firebase.auth().onIdTokenChanged(function(user) {
        if(description.value && trash_type_select.options[trash_type_select.selectedIndex].value) {
            if (user) {
                firebase.database().ref("/inventory/"+user.uid).push().set({
                    description: description.value,
                    type: trash_type_select.options[trash_type_select.selectedIndex].value,
                });
                description.value="";
                trash_type_select.selectedIndex=0;
            }
        } else {
            if(!description.value && !trash_type_select.options[trash_type_select.selectedIndex].value) alert("Description and Type are required")
            else if(!description.value) alert("Description is required")
            else alert("Type is required")
        }
    }); 
})
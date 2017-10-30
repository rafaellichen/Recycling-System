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
const trash_for_select = document.getElementById("trash-for-select")
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
        if(description.value && trash_type_select.options[trash_type_select.selectedIndex].value && trash_for_select.options[trash_for_select.selectedIndex].value) {
            if (user) {
                if(trash_for_select.options[trash_for_select.selectedIndex].value=="Donate") {
                    firebase.database().ref("/inventory/"+user.uid+"/donate").push().set({
                        description: description.value,
                        type: trash_type_select.options[trash_type_select.selectedIndex].value,
                    });
                } else {
                    firebase.database().ref("/inventory/"+user.uid+"/recycle").push().set({
                        description: description.value,
                        type: trash_type_select.options[trash_type_select.selectedIndex].value,
                    });
                }
                description.value="";
                trash_type_select.selectedIndex=0;
                trash_for_select.selectedIndex=0;
            }
        } else {
            if(!description.value && !trash_for_select.options[trash_for_select.selectedIndex].value && !trash_type_select.options[trash_type_select.selectedIndex].value) alert("Description, For, and Type are required")
            else if(!description.value) alert("Description is required")
            else if(!trash_for_select.options[trash_for_select.selectedIndex].value) alert("For is required")
            else alert("Type is required")
        }
    }); 
})
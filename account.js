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

    // reset
    function inputClear() {
        document.getElementById('userEmail').value=""
        document.getElementById('userPassword').value=""
    }    

    // elements
    const userEmail=document.getElementById('userEmail')
    const userPassword=document.getElementById('userPassword')

    // login
    login_Button.addEventListener("click",e => {
        const email = userEmail.value
        const password = userPassword.value
        const auth = firebase.auth()
        const status = auth.signInWithEmailAndPassword(email,password)
        status.catch(e=>{ 
            alert(e.message)
        })
    })

    // signup
    signup_Button.addEventListener("click",e => {
        const email = userEmail.value
        const password = userPassword.value
        const auth = firebase.auth()
        const status = auth.createUserWithEmailAndPassword(email,password)
        status.catch(e=>{
            alert(e.message)
        })
    })

    // signout
    signout_Button.addEventListener("click",e=> {
        firebase.auth().signOut()
    })

    // listener
    firebase.auth().onAuthStateChanged(firebaseUser => {
        if(firebaseUser) {
            document.getElementById('signout_Button').style.visibility = 'visible'
            var newUser = firebase.database().ref("/users/"+firebaseUser.uid)
            newUser.on("value",function(existence) {
                if(!existence.exists()) {
                    firebase.database().ref("/users/"+firebaseUser.uid).set({
                        first_name: "",
                        last_name: "",
                        phone: "",
                        street1: "",
                        street2: "",
                        city: "",
                        state: "",
                        zip: ""    
                    }); 
                }
            })
        } else {
            document.getElementById('signout_Button').style.visibility = 'hidden'
        }
    })
}())

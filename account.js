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

    // listener
    firebase.auth().onAuthStateChanged(user => {
        if(user) {
            var newUser = firebase.database().ref("/users/"+user.uid)
            console.log(user.uid)
            newUser.on("value",function(existence) {
                if(!existence.exists()) {
                    firebase.database().ref("/users/"+user.uid).set({
                        first_name: "",
                        last_name: "",
                        phone: "",
                        street1: "",
                        street2: "",
                        city: "",
                        state: "",
                        zip: ""    
                    }); 
                    window.location = "profile.html"
                }
            })
        }
    })
}())

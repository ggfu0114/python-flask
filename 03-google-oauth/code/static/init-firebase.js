// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
  apiKey: "AIzaSyCsTwECyAOfy9RERJBg3vLzajtFHcxMKFg",
  authDomain: "fir-45c5d.firebaseapp.com",
  databaseURL: "https://fir-45c5d.firebaseio.com",
  projectId: "fir-45c5d",
  storageBucket: "fir-45c5d.appspot.com",
  messagingSenderId: "141658609829",
  appId: "1:141658609829:web:5c7cc4193fbfcc4d8fd54c",
  measurementId: "G-D1Q74J2V1Q"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// firebase.analytics();
var provider = new firebase.auth.GoogleAuthProvider();
function googleSignin() {
  firebase.auth().signInWithRedirect(provider);
}

firebase.auth().getRedirectResult().then(function (result) {
  return firebase.auth().currentUser.getIdToken(/* forceRefresh */ true)
}).then(function (idToken) {
  $.ajax({
    url: '/sessionLogin',
    data: JSON.stringify({ idToken: idToken }),
    type: "POST",
    dataType: "json",
    contentType: "application/json;charset=utf-8",
    success: function (returnData) {
      window.location.href = '/profile'
    },
    error: function (xhr, ajaxOptions, thrownError) {
      console.log(xhr);
      console.log(thrownError);
    }
  });
}).catch( (error) =>{
  console.error('Failed to login',error)
});


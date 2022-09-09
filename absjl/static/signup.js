document.getElementById("submit").addEventListener("click", function(event){
    event.preventDefault()
    var email_id =document.getElementById("email_id").value
    var password =document.getElementById("password").value
    var firstname =document.getElementById("firstname").value
    var lastname =document.getElementById("lastname").value
    submit(email_id,password,firstname,lastname)
  });
function submit(email_id,password,firstname,lastname){


    // console.log("still yeh")
    cred={
      email_id:email_id,
      password:password,
      firstname:firstname,
      lastname:lastname
    }
    console.log(cred)
  //   fetch(window.location.origin+"/signup", {
       
  //     // Adding method type
  //     method: "POST",
       
  //     // Adding body or contents to send
  //     body: JSON.stringify(cred),
       
  //     // Adding headers to the request
  //     headers: {
  //         "Content-type": "application/json; charset=UTF-8"
  //     }
  // })
  //  // Converting to JSON
  //  .then(response => response.json())
   
  //  // Displaying results to console
  //    .then(json => validateRegister(json))
 }
//  function validateRegister(json){
//    var status=document.getElementsByClassName("status")
//    if(json.status){
//      status[0].innerHTML=json.error;
//    }else{
//      status[0].innerHTML=json.message;
//    }
//  }
document.getElementById("submit").addEventListener("click", function(event){
    event.preventDefault()
    var email_id=document.getElementById("email_id").value
    var password=document.getElementById("password").value

    localStorage.setItem("email_id", email_id);
    submit(email_id,password)
  });
  function submit(email_id,password){
    // console.log("still yeh")
    cred={
      email_id:email_id,
      password:password
    }
    console.log(cred)
    fetch(window.location.origin+"/login1", {
       
      // Adding method type
      method: "POST",
       
      // Adding body or contents to send
      body: JSON.stringify(cred),
       
      // Adding headers to the request
      headers: {
          "Content-type": "application/json; charset=UTF-8"
      }
  })
   
  // Converting to JSON
    .then(response => response.json())
   
  // Displaying results to console
    .then(json=>validateLogin(json));
  }
  function validateLogin(json){
    if(json.status){
      var status=document.getElementsByClassName("status")
      status[0].innerHTML=json.error;
    }else{
      window.location= window.location.origin+"/home";
    }
  }

async function getData(){
  const response = await fetch("http://127.0.0.1:5000/get_registered_students");
  const data = await response.JSON();
  console.log(data);

}
getData()
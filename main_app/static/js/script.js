var a = document.getElementsByClassName("LostPassword")[0];

function ShowPasswordCointainer(){
  var x = document.getElementsByClassName("forgetPasswordCointainer")[0];
  var y = document.getElementsByClassName("loginFormCointainer")[0];
  if (x.style.display === "none" && y.style.display === "block"){
	  x.style.display = "block";
	  y.style.display = "none";
	  } 
  else { 
      x.style.display = "none";
	  y.style.display = "block";
  }
}
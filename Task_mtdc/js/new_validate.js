$(document).ready(function () {
  $("#register").click(function(){
    if($('#fname').val()==='' || $('fname').val()===null){
      // alert('Firstname????');
      $("#error").append("<li>Enter Firstname</li>");
    }
    if($('#lname').val()==='' || $('lname').val()===null){
      // alert('Firstname????');
      $("#error").append("<li>Enter Lastname</li>");
    }
    if($('#uname').val()==='' || $('uname').val()===null){
      // alert('Firstname????');
      $("#error").append("<li>Enter Username</li>");
    }
    // alert(msg);
  });
});
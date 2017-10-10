$(document).ready(function () {
  // Validate Registration form
  $("#form1").validate({
    rules: {
      fname: "required",
      lname: "required",
      address: "required",
      state: "required",
      mobile: {
      	required: true,
      	number:
      },
      uname: {
        required: true,
        minlength: 5
      },  
      pwd: {
        required: true,
        minlength: 6
      },
      cpwd: {
        required: true,
        minlength: 6,
        equalTo: "#pwd"
      },
      email: {
        required: true,
        email: true
      }
    },
    messages: {
      fname: "<p style='color:red;'>Please enter your Firstname</p>",
      lname: "<p style='color:red;'>Please enter your Lastname</p>",
      address: "<p style='color:red;'>Please enter your Address</p>",
      address: "<p style='color:red;'>Please enter your State</p>",
      uname: {
        required: "<p style='color:red;'>Please enter your Username</p>",
        minlength: "<p style='color:red;'>Your Username must consists of at least 5 characters</p>"
      },
      email: {
        required: "<p style='color:red;'>Please enter your Username</p>",
        email: "<p style='color:red;'>Your Username must be of type name@domain.com</p>"
      },
      pwd: {
        required: "<p style='color:red;'>Please enter your Password</p>",
        minlength: "<p style='color:red;'>Your Password must consists of at least 6 characters</p>"
      },
      cpwd: {
        required: "<p style='color:red;'>Please enter your Password</p>",
        minlength: "<p style='color:red;'>Your Password must consists of at least 6 characters</p>",
        equalTo: "<p style='color:red;'>Plese enter the same Password as above</p>"
      }
    }
  })
});
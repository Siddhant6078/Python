$(document).ready(function () {
  $("#register").click(function(){
  	var mandatory_fields = {
  		fname:'Firstname',
  		lname:'Lastname',
  		uname:'Username',
  		email:'Email',
  		address:'Address',
  		state:'State',
  		dob:'Date of Birth',
  		mobile:'Mobile Number',
  		pwd:'Password',
  		cpwd:'Confirm Password'
  	};

    var errors = [];
    var err_msg = '';
  	$.each(mandatory_fields,function(index,field){
  		// console.log(field, $('#'+field).val());
  		if($('#'+index).val()==''){
  			// errors.push(field);
  			err_msg += "<li>Please Enter "+field+"</li>";
  		}else if (index == 'email') {
  				// ValidateEmail(index);
  				if (!ValidateEmail(index)) {
  					err_msg += '<li>Email is not valid</li>'	
  				}
  		}else if (index == 'mobile') {
  				console.log(ValidateMobile(index));
  				console.log($('#'+index).val().length);
  				if (!ValidateMobile(index)) {
  					err_msg += '<li>Mobile Number is not valid</li>'
  				}
  		}

  		// console.log(index + '=' + field);
  	});
  	$("ol").html(err_msg);

	// Validate email
	function ValidateEmail(email) {
        var expr = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        return expr.test(email);
    };

    // Validate mobile number
    function ValidateMobile(mobile) {
        var a = document.getElementById(mobile).value;
	    var filter = /^[0-9-+]+$/;
	    if (filter.test(a) && a.length==10) {
	        return true;
	    }
	    else {
	        return false;
	    }
    };

  	// console.log('mandatory_fields',errors);
    
    // $.each(errors,function(index,value){
    // 	$("ol").append("<li>"+value+"</li>");
    // });
    
    // if($('#fname').val()==='' || $('fname').val()===null){
     
    //   test.push("Enter Firstname");
    // }
    // if($('#lname').val()==='' || $('lname').val()===null){
      
    //   test.push("Enter Lastname");
    // }
    // if($('#dob').val()==='' || $('dob').val()===null){
     
    //   test.push("Enter Date of Birth");
    // }
    // if($('#address').val()==='' || $('address').val()===null){
      
    //   test.push("Enter Address");
    // }
    // if($('#state').val()==='' || $('state').val()===null){
      
    //   test.push("Enter State");
    // }
    // if($('#email').val()==='' || $('email').val()===null){
      
    //   test.push("Enter Email");
    // }
    // if($('#mobile').val()==='' || $('mobile').val()===null){
      
    //   test.push("Enter Mobile");
    // }
    // if($('#uname').val()==='' || $('uname').val()===null){
      
    //   test.push("Enter Username");
    // }
    // if($('#pwd').val()==='' || $('pwd').val()===null){
      
    //   test.push("Enter Password");
    // }
    // if($('#cpwd').val()==='' || $('cpwd').val()===null){
      
    //   test.push("Enter Confirm Password");
    // }

    // for (var i = test.length - 1; i >= 0; i--) {
    //   console.log(test[i]);
    // }

  });
});
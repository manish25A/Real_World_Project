$(document).ready(function() {
    // for customer signup form
    //creating variable to store the warning message
    var name_warning = false;
    var email_warning = false;
    var mobile_warning=false;
    var password_warning = false;
    var verify_password_warning = false;
    //focusout event for input fields
    $("#FullnameS").focusout(function(){
        check_Name();
    });
    $("#EmailS").focusout(function() {
        check_email();
    });
    $("#MobileS").focusout(function() {
        check_mobile();
    });
    $("#PasswordS").focusout(function() {
        check_password();
    });
    $("#Verify_PasswordS").focusout(function() {
        check_retype_password();
    });
    //function for checking the Customer name
    function check_Name() {
        var pattern = /^[a-zA-Z]+ [a-zA-Z]+$/;
        var name = $("#FullnameS").val();
        if (pattern.test(name) && name !== '') {
            $("#NameField").html("Name");
            $("#NameField").css("color","black");
            $("#FullnameS").css("border", "none");
            $("#FullnameS").css("border-bottom","1px solid black");
        } else {
            $("#NameField").html("Enter a valid Name");
            $("#NameField").css("color","red");
            $("#FullnameS").css("border","2px solid #F90A0A");
            name_warning = true;
        }
    }
    //function for checking the Email of Customer
    function check_email() {
        var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        var email = $("#EmailS").val();
        if (pattern.test(email) && email !== '') {
            $("#EmailField").html("Email");
            $("#EmailField").css("color","black");
            $("#EmailS").css("border", "none");
            $("#EmailS").css("border-bottom","1px solid black");
        } else {
            $("#EmailField").html("Invalid Email");
            $("#EmailField").css("color","red");
            $("#EmailS").css("border","2px solid #F90A0A");
            email_warning = true;
        }
    }
    //function for checking the mobile number of Customer
    function check_mobile() {
        var pattern = /^\d{10}$/;
        var phone = $("#MobileS").val();
        if (pattern.test(phone) && phone !== '') {
            $("#MobileField").html("Phone Number");
            $("#MobileField").css("color","black");
            $("#MobileS").css("border","none");
            $("#MobileS").css("border-bottom","1px solid black");
        } else {
            $("#MobileField").html("Invalid Phone Number");
            $("#MobileField").css("color","red");
            $("#MobileS").css("border","2px solid #F90A0A");
            mobile_warning = true;
        }
    }
    //function for checking the Password length
    function check_password() {
        var password_length = $("#PasswordS").val().length;
        if (password_length < 8) {
            $("#PasswordField").html("Atleast 8 Characters");
            $("#PasswordField").css("color","red");
            $("#PasswordS").css("border","2px solid #F90A0A");
            password_warning = true;
        } else {
            $("#PasswordS").css("border","none");
            $("#PasswordS").css("border-bottom","1px solid black");
            $("#PasswordField").css("color","black");
            $("#PasswordField").html("Password");
        }
    }
    //function for checking the typed password
    function check_retype_password() {
        var password = $("#PasswordS").val();
        var retype_password = $("#Verify_PasswordS").val();
        if (password !== retype_password||retype_password=="") {
            $("#VerifyPasswordField").html("Password does not Match");
            $("#VerifyPasswordField").css("color","red");
            $("#Verify_PasswordS").css("border","2px solid #F90A0A");
            verify_password_warning = true;
        } else {
            $("#VerifyPasswordField").css("color","black");
            $("#Verify_PasswordS").css("border","none");
            $("#Verify_PasswordS").css("border-bottom","1px solid black");
            $("#VerifyPasswordField").html("Verify Password");

        }
    }
    //function for the submit button in the signup form
    $("#signup_form").submit(function() {
        name_warning = false;
        email_warning = false;
        mobile_warning= false;
        password_warning = false;
        verify_password_warning = false;
        //calling all the function that does validation
        check_Name();
        check_email();
        check_mobile();
        check_password();
        check_retype_password();
        //if clause for validation
        if (name_warning === false && email_warning === false && mobile_warning === false
            &&  password_warning === false && verify_password_warning===false) {
            alert("Your details is Registered");
            return true;
        } else {
            alert("Please fill all the fields correctly");
            return false;
        }
    });
});

$(function () {
    $("#email-error-message").hide();
    $("#pass-error-message").hide();
    $("#submit-error-message").hide();

    var error_email = false;
    var error_pass = false;

    $("#form-email").focusout(function () {
        check_email();
    });
    $("#form-email").focusin(function () {
        $("#form-email").css("border", "2px solid var(--pc)");
    });

    $("#form-pass").focusout(function () {
        check_pass();
    });
    $("#form-pass").focusin(function () {
        $("#form-pass").css("border", "2px solid var(--pc)");
    });

    function check_email() {
        var pattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
        var email = $("#form-email").val();

        if (pattern.test(email) && email !== "") {
            $("#email-error-message").hide();
            $("#form-email").css("border", "2px solid var(--pc)");
        } else if (email === "") {
            $("#email-error-message").html("E-mail Can't be Empty.");
            $("#email-error-message").hide();
            $("#form-email").css("border", "2px solid var(--bc)");
            error_email = true;
        } else {
            $("#email-error-message").html("Enter Valid E-mail.");
            $("#email-error-message").show();
            $("#form-email").css("border", "2px solid red");
            error_email = true;
        }
    }

    function check_pass() {
        var pattern = /^(?=.*?[A-Za-z])(?=.*?[0-9]).{7,}$/;
        var pass_length = $("#form-pass").val().length;
        var pass = $("#form-pass").val();

        if (pattern.test(pass) && pass_length >= 8) {
            $("#pass-error-message").hide();
            $("#form-pass").css("border", "2px solid var(--pc)");
        } else if (pass === "") {
            $("#pass-error-message").html("Password Can't be Empty.");
            $("#pass-error-message").hide();
            $("#form-pass").css("border", "2px solid var(--bc)");
            error_pass = true;
        } else {
            $("#pass-error-message").html(
                "Enter Atleast 8 Character, must include atleast one Alphabet and one Number."
            );
            $("#pass-error-message").show();
            $("#form-pass").css("border", "2px solid red");
            error_pass = true;
        }
    }

    $("#login_form").submit(function () {
        error_email = false;
        error_pass = false;

        check_email();
        check_pass();

        if (error_email === false && error_pass === false) {
            $("#submit-error-message").hide();
            return true;
        } else {
            $("#submit-error-message").html(
                "Please Enter All Field Correctly."
            );
            $("#submit-error-message").show();

            if (error_email === true) {
                $("#form-email").css("border", "2px solid red");
                $("#email-error-message").show();
            }

            if (error_pass === true) {
                $("#form-pass").css("border", "2px solid red");
                $("#pass-error-message").show();
            }

            return false;
        }
    });
});

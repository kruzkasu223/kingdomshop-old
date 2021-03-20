$(function () {
    $("#email-error-message").hide();
    $("#fname-error-message").hide();
    $("#lname-error-message").hide();
    $("#pass1-error-message").hide();
    $("#pass2-error-message").hide();
    $("#submit-error-message").hide();

    var error_email = false;
    var error_fname = false;
    var error_lname = false;
    var error_pass1 = false;
    var error_pass2 = false;

    $("#form-email").focusout(function () {
        check_email();
    });
    $("#form-email").focusin(function () {
        $("#form-email").css("border", "2px solid var(--pc)");
    });

    $("#form-fname").focusout(function () {
        check_fname();
    });
    $("#form-fname").focusin(function () {
        $("#form-fname").css("border", "2px solid var(--pc)");
    });

    $("#form-lname").focusout(function () {
        check_lname();
    });
    $("#form-lname").focusin(function () {
        $("#form-lname").css("border", "2px solid var(--pc)");
    });

    $("#form-pass1").focusout(function () {
        check_pass1();
    });
    $("#form-pass1").focusin(function () {
        $("#form-pass1").css("border", "2px solid var(--pc)");
    });

    $("#form-pass2").focusout(function () {
        check_pass2();
    });
    $("#form-pass2").focusin(function () {
        $("#form-pass2").css("border", "2px solid var(--pc)");
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

    function check_fname() {
        var pattern = /^[a-zA-Z ]*$/;
        var fname = $("#form-fname").val();

        if (pattern.test(fname) && fname !== "") {
            $("#fname-error-message").hide();
            $("#form-fname").css("border", "2px solid var(--pc)");
        } else if (fname === "") {
            $("#fname-error-message").html("First Name Can't be Empty.");
            $("#fname-error-message").hide();
            $("#form-fname").css("border", "2px solid var(--bc)");
            error_fname = true;
        } else {
            $("#fname-error-message").html("Enter Only Alphabets.");
            $("#fname-error-message").show();
            $("#form-fname").css("border", "2px solid red");
            error_fname = true;
        }
    }

    function check_lname() {
        var pattern = /^[a-zA-Z ]*$/;
        var lname = $("#form-lname").val();

        if (pattern.test(lname) && lname !== "") {
            $("#lname-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--pc)");
        } else if (lname === "") {
            $("#lname-error-message").html("Last Name Can't be Empty.");
            $("#lname-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--bc)");
            error_lname = true;
        } else {
            $("#lname-error-message").html("Enter Only Alphabets.");
            $("#lname-error-message").show();
            $("#form-lname").css("border", "2px solid red");
            error_lname = true;
        }
    }

    function check_pass1() {
        var pattern = /^(?=.*?[A-Za-z])(?=.*?[0-9]).{7,}$/;
        var pass1_length = $("#form-pass1").val().length;
        var pass1 = $("#form-pass1").val();

        if (pattern.test(pass1) && pass1_length >= 8) {
            $("#pass1-error-message").hide();
            $("#form-pass1").css("border", "2px solid var(--pc)");
        } else if (pass1 === "") {
            $("#pass1-error-message").html("Password Can't be Empty.");
            $("#pass1-error-message").hide();
            $("#form-pass1").css("border", "2px solid var(--bc)");
            error_pass1 = true;
        } else {
            $("#pass1-error-message").html(
                "Enter Atleast 8 Character, must include atleast one Alphabet and one Number."
            );
            $("#pass1-error-message").show();
            $("#form-pass1").css("border", "2px solid red");
            error_pass1 = true;
        }
    }

    function check_pass2() {
        var pattern = /^(?=.*?[A-Za-z])(?=.*?[0-9]).{7,}$/;
        var pass2_length = $("#form-pass2").val().length;
        var pass2 = $("#form-pass2").val();

        if (pattern.test(pass2) && pass2_length >= 8) {
            $("#pass2-error-message").hide();
            $("#form-pass2").css("border", "2px solid var(--pc)");
        } else if (pass2 === "") {
            $("#pass2-error-message").html("Password Can't be Empty.");
            $("#pass2-error-message").hide();
            $("#form-pass2").css("border", "2px solid var(--bc)");
            error_pass2 = true;
        } else {
            $("#pass2-error-message").html(
                "Enter Atleast 8 Character, must include atleast one Alphabet and one Number."
            );
            $("#pass2-error-message").show();
            $("#form-pass2").css("border", "2px solid red");
            error_pass2 = true;
        }
    }

    $("#signup_form").submit(function () {
        error_email = false;
        error_fname = false;
        error_lname = false;
        error_pass1 = false;
        error_pass2 = false;

        check_email();
        check_fname();
        check_lname();
        check_pass1();
        check_pass2();

        if (
            error_email === false &&
            error_fname === false &&
            error_lname === false &&
            error_pass1 === false &&
            error_pass2 === false
        ) {
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

            if (error_fname === true) {
                $("#form-fname").css("border", "2px solid red");
                $("#fname-error-message").show();
            }

            if (error_lname === true) {
                $("#form-lname").css("border", "2px solid red");
                $("#lname-error-message").show();
            }

            if (error_pass1 === true) {
                $("#form-pass1").css("border", "2px solid red");
                $("#pass1-error-message").show();
            }

            if (error_pass2 === true) {
                $("#form-pass2").css("border", "2px solid red");
                $("#pass2-error-message").show();
            }

            return false;
        }
    });
});

$(function () {
    $("#pass-error-message").hide();
    $("#pass1-error-message").hide();
    $("#pass2-error-message").hide();
    $("#submit-error-message").hide();

    var error_pass = false;
    var error_pass1 = false;
    var error_pass2 = false;

    $("#form-pass").focusout(function () {
        check_pass();
    });
    $("#form-pass").focusin(function () {
        $("#form-pass").css("border", "2px solid var(--pc)");
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

    $("#password_change").submit(function () {
        error_pass = false;
        error_pass1 = false;
        error_pass2 = false;

        check_pass();
        check_pass1();
        check_pass2();

        if (
            error_pass === false &&
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

            if (error_pass === true) {
                $("#form-pass").css("border", "2px solid red");
                $("#pass-error-message").show();
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

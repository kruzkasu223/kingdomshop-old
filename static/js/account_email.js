$(function () {
    $("#email-error-message").hide();
    $("#submit-error-message").hide();

    var error_email = false;

    $("#form-email").focusout(function () {
        check_email();
    });
    $("#form-email").focusin(function () {
        $("#form-email").css("border", "2px solid var(--pc)");
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

    $("#email_form").submit(function () {
        error_email = false;

        check_email();

        if (error_email === false) {
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

            return false;
        }
    });
});

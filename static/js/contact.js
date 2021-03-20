$(function () {
    $("#name-error-message").hide();
    $("#email-error-message").hide();
    $("#subject-error-message").hide();
    $("#msg-error-message").hide();
    $("#submit-error-message").hide();

    var error_name = false;
    var error_email = false;
    var error_subject = false;
    var error_msg = false;

    $("#form-name").focusout(function () {
        check_name();
    });
    $("#form-name").focusin(function () {
        $("#form-name").css("border", "2px solid var(--pc)");
    });

    $("#form-email").focusout(function () {
        check_email();
    });
    $("#form-email").focusin(function () {
        $("#form-email").css("border", "2px solid var(--pc)");
    });

    $("#form-subject").focusout(function () {
        check_subject();
    });
    $("#form-subject").focusin(function () {
        $("#form-subject").css("border", "2px solid var(--pc)");
    });

    $("#form-msg").focusout(function () {
        check_msg();
    });
    $("#form-msg").focusin(function () {
        $("#form-msg").css("border", "2px solid var(--pc)");
    });

    function check_name() {
        var pattern = /^[a-zA-Z ]*$/;
        var name = $("#form-name").val();

        if (pattern.test(name) && name !== "") {
            $("#name-error-message").hide();
            $("#form-name").css("border", "2px solid var(--pc)");
        } else if (name === "") {
            $("#name-error-message").html("! Name Can't be Empty.");
            $("#name-error-message").hide();
            $("#form-name").css("border", "2px solid var(--bc)");
            error_name = true;
        } else {
            $("#name-error-message").html("! Enter Only Alphabets.");
            $("#name-error-message").show();
            $("#form-name").css("border", "2px solid red");
            error_name = true;
        }
    }

    function check_email() {
        var pattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
        var email = $("#form-email").val();

        if (pattern.test(email) && email !== "") {
            $("#email-error-message").hide();
            $("#form-email").css("border", "2px solid var(--pc)");
        } else if (email === "") {
            $("#email-error-message").html("! E-mail Can't be Empty.");
            $("#email-error-message").hide();
            $("#form-email").css("border", "2px solid var(--bc)");
            error_email = true;
        } else {
            $("#email-error-message").html("! Enter Valid E-mail.");
            $("#email-error-message").show();
            $("#form-email").css("border", "2px solid red");
            error_email = true;
        }
    }

    function check_subject() {
        var subject_length = $("#form-subject").val().length;
        var subject = $("#form-subject").val();

        if (subject_length > 8) {
            $("#subject-error-message").hide();
            $("#form-subject").css("border", "2px solid var(--pc)");
        } else if (subject === "") {
            $("#subject-error-message").html("! Subject Can't be Empty.");
            $("#subject-error-message").hide();
            $("#form-subject").css("border", "2px solid var(--bc)");
            error_subject = true;
        } else {
            $("#subject-error-message").html("! Enter Atleast 10 Character.");
            $("#subject-error-message").show();
            $("#form-subject").css("border", "2px solid red");
            error_subject = true;
        }
    }

    function check_msg() {
        var msg_length = $("#form-msg").val().length;
        var msg = $("#form-msg").val();

        if (msg_length > 40) {
            $("#msg-error-message").hide();
            $("#form-msg").css("border", "2px solid var(--pc)");
        } else if (msg === "") {
            $("#msg-error-message").html("! Message Can't be Empty.");
            $("#msg-error-message").hide();
            $("#form-msg").css("border", "2px solid var(--bc)");
            error_msg = true;
        } else {
            $("#msg-error-message").html("! Enter Atleast 40 Character.");
            $("#msg-error-message").show();
            $("#form-msg").css("border", "2px solid red");
            error_msg = true;
        }
    }

    $("#contact_form").submit(function () {
        error_name = false;
        error_email = false;
        error_subject = false;
        error_msg = false;

        check_name();
        check_email();
        check_subject();
        check_msg();

        if (
            error_name === false &&
            error_email === false &&
            error_subject === false &&
            error_msg === false
        ) {
            $("#submit-error-message").hide();
            return true;
        } else {
            $("#submit-error-message").html(
                "Please Enter All Field Correctly!"
            );
            $("#submit-error-message").show();

            if (error_name === true) {
                $("#form-name").css("border", "2px solid red");
                $("#name-error-message").show();
            }
            if (error_email === true) {
                $("#form-email").css("border", "2px solid red");
                $("#email-error-message").show();
            }
            if (error_subject === true) {
                $("#form-subject").css("border", "2px solid red");
                $("#subject-error-message").show();
            }
            if (error_msg === true) {
                $("#form-msg").css("border", "2px solid red");
                $("#msg-error-message").show();
            }

            return false;
        }
    });
});

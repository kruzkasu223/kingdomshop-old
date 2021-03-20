$(function () {
    $("#subject-error-message").hide();
    $("#msg-error-message").hide();
    $("#submit-error-message").hide();

    var error_subject = false;
    var error_msg = false;

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

    function check_subject() {
        var subject_length = $("#form-subject").val().length;
        var subject = $("#form-subject").val();

        if (subject_length >= 4) {
            $("#subject-error-message").hide();
            $("#form-subject").css("border", "2px solid var(--pc)");
        } else if (subject === "") {
            $("#form-subject").css("border", "2px solid var(--bc)");
            error_subject = false;
        } else {
            $("#subject-error-message").html("! Enter Atleast 4 Character.");
            $("#subject-error-message").show();
            $("#form-subject").css("border", "2px solid red");
            error_subject = true;
        }
    }

    function check_msg() {
        var msg_length = $("#form-msg").val().length;
        var msg = $("#form-msg").val();

        if (msg_length >= 4) {
            $("#msg-error-message").hide();
            $("#form-msg").css("border", "2px solid var(--pc)");
        } else if (msg === "") {
            $("#form-msg").css("border", "2px solid var(--bc)");
            error_msg = false;
        } else {
            $("#msg-error-message").html("! Enter Atleast 4 Character.");
            $("#msg-error-message").show();
            $("#form-msg").css("border", "2px solid red");
            error_msg = true;
        }
    }

    $("#review-form").submit(function () {
        error_subject = false;
        error_msg = false;

        check_subject();
        check_msg();

        if (error_subject === false && error_msg === false) {
            $("#submit-error-message").hide();
            return true;
        } else {
            $("#submit-error-message").html(
                "Please Enter All Field Correctly!"
            );
            $("#submit-error-message").show();
            return false;
        }
    });
});

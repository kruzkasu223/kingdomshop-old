$(function () {
    $("#fname-error-message").hide();
    $("#lname-error-message").hide();
    $("#submit-error-message").hide();

    var error_fname = false;
    var error_lname = false;

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

    $("#name_form").submit(function () {
        error_fname = false;
        error_lname = false;

        check_fname();
        check_lname();

        if (error_fname === false && error_lname === false) {
            $("#submit-error-message").hide();
            return true;
        } else {
            $("#submit-error-message").html(
                "Please Enter All Field Correctly."
            );
            $("#submit-error-message").show();

            if (error_fname === true) {
                $("#form-fname").css("border", "2px solid red");
                $("#fname-error-message").show();
            }

            if (error_lname === true) {
                $("#form-lname").css("border", "2px solid red");
                $("#lname-error-message").show();
            }

            return false;
        }
    });
});

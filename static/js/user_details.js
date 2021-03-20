$(function () {
    $("#phone-error-message").hide();
    $("#age-error-message").hide();
    $("#gender-error-message").hide();
    $("#submit-error-message").hide();

    var error_phone = false;
    var error_age = false;
    var error_gender = false;

    $("#form-phone").focusout(function () {
        check_phone();
    });
    $("#form-phone").focusin(function () {
        $("#form-phone").css("border", "2px solid var(--pc)");
    });

    $("#form-age").focusout(function () {
        check_age();
    });
    $("#form-age").focusin(function () {
        $("#form-age").css("border", "2px solid var(--pc)");
    });

    $("#form-gender").focusout(function () {
        check_gender();
    });
    $("#form-gender").focusin(function () {
        $("#form-gender").css("border", "2px solid var(--pc)");
    });

    function check_phone() {
        var pattern = /^[0-9]*$/;
        var phone = $("#form-phone").val();

        if (pattern.test(phone) && phone.length === 10) {
            $("#phone-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--pc)");
        } else if (phone === "") {
            $("#phone-error-message").hide();
            $("#form-phone").css("border", "2px solid var(--bc)");
            error_phone = false;
        } else {
            $("#phone-error-message").html(
                "Enter Only Number and Exact 10 Characters."
            );
            $("#phone-error-message").show();
            $("#form-phone").css("border", "2px solid red");
            error_phone = true;
        }
    }

    function check_age() {
        var pattern = /^[0-9]*$/;
        var age = $("#form-age").val();

        if (pattern.test(age) && age.length === 2) {
            $("#age-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--pc)");
        } else if (age === "") {
            $("#age-error-message").hide();
            $("#form-age").css("border", "2px solid var(--bc)");
            error_age = false;
        } else {
            $("#age-error-message").html("Enter Valid Age.");
            $("#age-error-message").show();
            $("#form-age").css("border", "2px solid red");
            error_age = true;
        }
    }

    function check_gender() {
        var gender = $("#form-gender").val();

        if (gender !== "") {
            $("#gender-error-message").hide();
            $("#form-gender").css("border", "2px solid var(--pc)");
            $("#gender-label").css("fontSize", "0.85rem");
            $("#gender-label").css("top", "1.2rem");
        } else if (gender === "") {
            $("#gender-error-message").hide();
            $("#form-gender").css("border", "2px solid var(--bc)");
            $("#gender-label").css("fontSize", "0.85rem");
            $("#gender-label").css("top", "1.2rem");
            error_gender = false;
        } else {
            $("#gender-error-message").hide();
            $("#form-gender").css("border", "2px solid var(--pc)");
            error_gender = false;
        }
    }

    $("#details_form").submit(function () {
        error_phone = false;
        error_age = false;
        error_gender = false;

        check_phone();
        check_age();
        check_gender();

        if (
            error_phone === false &&
            error_age === false &&
            error_gender === false
        ) {
            $("#submit-error-message").hide();
            return true;
        } else {
            $("#submit-error-message").html(
                "Please Enter All Field Correctly."
            );
            $("#submit-error-message").show();

            if (error_phone === true) {
                $("#form-phone").css("border", "2px solid red");
                $("#phone-error-message").show();
            }

            if (error_age === true) {
                $("#form-age").css("border", "2px solid red");
                $("#age-error-message").show();
            }

            if (error_gender === true) {
                $("#form-gender").css("border", "2px solid red");
                $("#gender-error-message").show();
            }

            return false;
        }
    });
});

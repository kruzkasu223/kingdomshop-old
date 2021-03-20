$(function () {
    $("#fname-error-message").hide();
    $("#lname-error-message").hide();
    $("#email-error-message").hide();
    $("#phone-error-message").hide();
    $("#aline1-error-message").hide();
    $("#aline2-error-message").hide();
    $("#pincode-error-message").hide();
    $("#city-error-message").hide();
    $("#state-error-message").hide();
    $("#msg-error-message").hide();
    $("#submit-error-message").hide();

    var error_fname = false;
    var error_lname = false;
    var error_email = false;
    var error_phone = false;
    var error_aline1 = false;
    var error_aline2 = false;
    var error_pincode = false;
    var error_city = false;
    var error_state = false;
    var error_msg = false;

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

    $("#form-email").focusout(function () {
        check_email();
    });
    $("#form-email").focusin(function () {
        $("#form-email").css("border", "2px solid var(--pc)");
    });

    $("#form-phone").focusout(function () {
        check_phone();
    });
    $("#form-phone").focusin(function () {
        $("#form-phone").css("border", "2px solid var(--pc)");
    });

    $("#form-aline1").focusout(function () {
        check_aline1();
    });
    $("#form-aline1").focusin(function () {
        $("#form-aline1").css("border", "2px solid var(--pc)");
    });

    $("#form-aline2").focusout(function () {
        check_aline2();
    });
    $("#form-aline2").focusin(function () {
        $("#form-aline2").css("border", "2px solid var(--pc)");
    });

    $("#form-pincode").focusout(function () {
        check_pincode();
    });
    $("#form-pincode").focusin(function () {
        $("#form-pincode").css("border", "2px solid var(--pc)");
    });

    $("#form-city").focusout(function () {
        check_city();
    });
    $("#form-city").focusin(function () {
        $("#form-city").css("border", "2px solid var(--pc)");
    });

    $("#form-state").focusout(function () {
        check_state();
    });
    $("#form-state").focusin(function () {
        $("#form-state").css("border", "2px solid var(--pc)");
    });

    $("#form-msg").focusout(function () {
        check_msg();
    });
    $("#form-msg").focusin(function () {
        $("#form-msg").css("border", "2px solid var(--pc)");
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

    function check_phone() {
        var pattern = /^[0-9]*$/;
        var phone = $("#form-phone").val();

        if (pattern.test(phone) && phone.length === 10) {
            $("#phone-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--pc)");
        } else if (phone === "") {
            $("#phone-error-message").html("Phone Number Can't be Empty.");
            $("#phone-error-message").hide();
            $("#form-phone").css("border", "2px solid var(--bc)");
            error_phone = true;
        } else {
            $("#phone-error-message").html(
                "Enter Only Number and Exact 10 Characters."
            );
            $("#phone-error-message").show();
            $("#form-phone").css("border", "2px solid red");
            error_phone = true;
        }
    }

    function check_aline1() {
        var aline1_length = $("#form-aline1").val().length;
        var aline1 = $("#form-aline1").val();

        if (aline1_length > 9) {
            $("#aline1-error-message").hide();
            $("#form-aline1").css("border", "2px solid var(--pc)");
        } else if (aline1 === "") {
            $("#aline1-error-message").html("Address Can't be Empty.");
            $("#aline1-error-message").hide();
            $("#form-aline1").css("border", "2px solid var(--bc)");
            error_aline1 = true;
        } else {
            $("#aline1-error-message").html("! Enter Atleast 10 Character.");
            $("#aline1-error-message").show();
            $("#form-aline1").css("border", "2px solid red");
            error_aline1 = true;
        }
    }

    function check_aline2() {
        var aline2_length = $("#form-aline2").val().length;
        var aline2 = $("#form-aline2").val();

        if (aline2_length > 1) {
            $("#aline2-error-message").hide();
            $("#form-aline2").css("border", "2px solid var(--pc)");
        } else if (aline2 === "") {
            $("#aline2-error-message").hide();
            $("#form-aline2").css("border", "2px solid var(--bc)");
            error_msg = false;
        } else {
            $("#aline2-error-message").html("! Enter Atleast 2 Character.");
            $("#aline2-error-message").show();
            $("#form-aline2").css("border", "2px solid red");
            error_aline2 = true;
        }
    }

    function check_pincode() {
        var pattern = /^[0-9]*$/;
        var pincode = $("#form-pincode").val();

        if (pattern.test(pincode) && pincode.length === 6) {
            $("#pincode-error-message").hide();
            $("#form-lname").css("border", "2px solid var(--pc)");
        } else if (pincode === "") {
            $("#pincode-error-message").html("Pincode Can't be Empty.");
            $("#pincode-error-message").hide();
            $("#form-pincode").css("border", "2px solid var(--bc)");
            error_pincode = true;
        } else {
            $("#pincode-error-message").html(
                "Enter Only Number and Exact 6 Characters."
            );
            $("#pincode-error-message").show();
            $("#form-pincode").css("border", "2px solid red");
            error_pincode = true;
        }
    }

    function check_city() {
        var pattern = /^[a-zA-Z ]*$/;
        var city = $("#form-city").val();

        if (pattern.test(city) && city !== "") {
            $("#city-error-message").hide();
            $("#form-city").css("border", "2px solid var(--pc)");
        } else if (city === "") {
            $("#city-error-message").html("City Can't be Empty.");
            $("#city-error-message").hide();
            $("#form-city").css("border", "2px solid var(--bc)");
            error_city = true;
        } else {
            $("#city-error-message").html("Enter Only Alphabets.");
            $("#city-error-message").show();
            $("#form-city").css("border", "2px solid red");
            error_city = true;
        }
    }

    function check_state() {
        var state = $("#form-state").val();

        if (state !== "") {
            $("#state-error-message").hide();
            $("#form-state").css("border", "2px solid var(--pc)");
            $("#state-label").css("fontSize", "0.85rem");
            $("#state-label").css("top", "1.2rem");
        } else if (state === "") {
            $("#state-error-message").html("You Have to Select State.");
            $("#state-error-message").hide();
            $("#form-state").css("border", "2px solid var(--bc)");
            $("#state-label").css("fontSize", "0.85rem");
            $("#state-label").css("top", "1.2rem");
            error_state = true;
        } else {
            $("#state-error-message").hide();
            $("#form-state").css("border", "2px solid var(--pc)");
            error_state = false;
        }
    }

    function check_msg() {
        var msg_length = $("#form-msg").val().length;
        var msg = $("#form-msg").val();

        if (msg_length > 9) {
            $("#msg-error-message").hide();
            $("#form-msg").css("border", "2px solid var(--pc)");
        } else if (msg === "") {
            $("#msg-error-message").hide();
            $("#form-msg").css("border", "2px solid var(--bc)");
            error_msg = false;
        } else {
            $("#msg-error-message").html("! Enter Atleast 10 Character.");
            $("#msg-error-message").show();
            $("#form-msg").css("border", "2px solid red");
            error_msg = true;
        }
    }

    $("#order_form").submit(function () {
        error_fname = false;
        error_lname = false;
        error_email = false;
        error_phone = false;
        error_aline1 = false;
        error_aline2 = false;
        error_pincode = false;
        error_city = false;
        error_state = false;
        error_msg = false;

        check_fname();
        check_lname();
        check_email();
        check_phone();
        check_aline1();
        check_aline2();
        check_pincode();
        check_city();
        check_state();
        check_msg();

        if (
            error_fname === false &&
            error_lname === false &&
            error_email === false &&
            error_phone === false &&
            error_aline1 === false &&
            error_aline2 === false &&
            error_pincode === false &&
            error_city === false &&
            error_state === false &&
            error_msg === false
        ) {
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

            if (error_email === true) {
                $("#form-email").css("border", "2px solid red");
                $("#email-error-message").show();
            }

            if (error_phone === true) {
                $("#form-phone").css("border", "2px solid red");
                $("#phone-error-message").show();
            }

            if (error_aline1 === true) {
                $("#form-aline1").css("border", "2px solid red");
                $("#aline1-error-message").show();
            }

            if (error_aline2 === true) {
                $("#form-aline2").css("border", "2px solid red");
                $("#aline2-error-message").show();
            }

            if (error_pincode === true) {
                $("#form-pincode").css("border", "2px solid red");
                $("#pincode-error-message").show();
            }

            if (error_city === true) {
                $("#form-city").css("border", "2px solid red");
                $("#city-error-message").show();
            }

            if (error_state === true) {
                $("#form-state").css("border", "2px solid red");
                $("#state-error-message").show();
            }

            if (error_msg === true) {
                $("#form-msg").css("border", "2px solid red");
                $("#msg-error-message").show();
            }

            return false;
        }
    });
});

var custom = (function () {
    console.log("custom iife was called");

    var setActive = function (id) {
        console.log("custom.setActive was called");
        $(id).addClass("active");
    };

    var updateActive = function (setId, removeId) {
        console.log("custom.updateActive was called");
        $(removeId).removeClass("active");
        $(setId).addClass("active");
    };

    var setClass = function (id, className) {
        console.log("custom.setClass was called");
        $(id).addClass(className);
    };

    var addTicketValidation = function () {
        console.log("custom.addTicketValidation was called");
        $("#submit-ticket-form").validate({
            rules: {
                name: "required",
                email: {
                    required: true,
                    email: true
                },
                title: "required",
                content: "required",
            },
            submitHandler: function (form) {
                console.log("you need to submit form here");
                form.submit();
            }
        });
    };

    return {
        setActive: setActive,
        updateActive: updateActive,
        setClass: setClass,
        addTicketValidation: addTicketValidation
    };
}());

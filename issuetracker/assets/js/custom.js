var custom = (function () {
    var setActive = function (id) {
        $(id).addClass("active");
    };

    var updateActive = function (setId, removeId) {
        $(removeId).removeClass("active");
        $(setId).addClass("active");
    };

    var setClass = function (id, className) {
        $(id).addClass(className);
    };

    var addTicketValidation = function () {
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

    var addCommentValidation = function () {
        $("#submit-comment-form").validate({
            rules: {
                name: "required",
                email: {
                    required: true,
                    email: true
                },
                content: "required",
            },
            submitHandler: function (form) {
                form.submit();
            }
        });
    };

    return {
        setActive: setActive,
        updateActive: updateActive,
        setClass: setClass,
        addTicketValidation: addTicketValidation,
        addCommentValidation: addCommentValidation
    };
}());

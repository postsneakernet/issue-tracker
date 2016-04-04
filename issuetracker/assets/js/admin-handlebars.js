var admin = (function () {
    $(document).ready(function () {
        console.log("admin iife was called");
        admin.getAdminTemplate(5000);
    });
    $("#admin-home").click(function () {
        custom.updateActive("#admin-home", "#sub-nav li");
        admin.getAdminTemplate();
    });
    $("#admin-maintainers").click(function () {
        custom.updateActive("#admin-maintainers", "#sub-nav li");
        admin.getMaintainersTemplate();
    });
    $("#admin-projects").click(function () {
        custom.updateActive("#admin-projects", "#sub-nav li");
        admin.getProjectsTemplate();
    });
    $("#admin-tickets").click(function () {
        custom.updateActive("#admin-tickets", "#sub-nav li");
        admin.getTicketsTemplate();
    });
    $("#admin-comments").click(function () {
        custom.updateActive("#admin-comments", "#sub-nav li");
        admin.getCommentsTemplate();
    });

    var getMsgTemplate = function (templateId, msg) {
        console.log("admin.getMsgTemplate was called");
        var source = $(templateId).html();
        var template = Handlebars.compile(source);
        var context = {"js_msg": msg};
        var html = template(context);
        $(".js-msg-placeholder").append(html);
    };

    var checkResult = function (context, cb) {
        console.log("admin.parseContextResults was called");
        if (context.hasOwnProperty('error')) {
            getMsgTemplate("#error-template", context.error);
        } else if (context.hasOwnProperty('success')) {
            getMsgTemplate("#success-template", context.success);
            if (undefined !== cb) {
                console.log("calling callback function passed to sendFormData > checkResult");
                cb();
            }
            // move into own function
            $(".clear-on-success").trigger("reset");
        }
    };

    var clearMsg = function (t) {
        if (t === undefined) {
            t = 0;
        }
        console.log("timer value: " + t);
        setTimeout(function () {
            $(".flask-msg-placeholder").empty();
            $(".js-msg-placeholder").empty();
        }, t);
    };

    var getTemplate = function (t, pageTitle, templateId, context, url, func, cb) {
        console.log("admin.getTemplate was called with: " + arguments);
        clearMsg(t);
        $("#page-title").text(pageTitle);
        var source = $(templateId).html();
        var template = Handlebars.compile(source);
        if (func === undefined) {
            var html = template(context);
            $(".content-placeholder").html(html);
        } else {
            // for remote ajax calls
            func(url, template, cb);
        }
    };

    var remoteJSON = function (url, template, cb) {
        console.log("admin.remoteJSON was called");
        $.getJSON(url, {
        })
        .done(function (data) {
            console.log("ajax GET to " + url);
            var context = data;
            checkResult(context);
            var html = template(context);
            $(".content-placeholder").html(html);
            if (undefined !== cb) {
                console.log("calling callback function passed to remoteJSON");
                cb();
            }
        })
        .fail(function (e) {
            console.log("fail from ajax GET to " + url);
            getMsgTemplate("#error-template", "There was an issue communicating with the server.");
        });
    };

    var getAdminTemplate = function (t) {
        console.log("admin.getAdminTemplate was called");
        getTemplate(t, "Admin", "#admin-template", undefined, "/ajax/admin", remoteJSON);
    };

    var getMaintainersTemplate = function (t) {
        console.log("admin.getMaintainersTemplate was called");
        getTemplate(t, "Maintainers", "#maintainers-template", undefined, "/ajax/admin/maintainers", remoteJSON);
    };

    var getMaintainersCreateTemplate = function (t) {
        console.log("admin.getMaintainersCreateTemplate was called");
        getTemplate(t, "Maintainers", "#maintainers-create-template");
        $("#maintainers-create-form").validate({
            rules: {
                username: "required",
                email: {
                    required: true,
                    email: true
                },
                password: "required",
                "confirm-password": {
                    required: true,
                    equalTo: "#password"
                }
            },
            submitHandler: function () {
                admin.sendFormData("/ajax/admin/maintainers/create", admin.getFormData("#maintainers-create-form"));
            }
        });
    };

    var getMaintainersUpdateTemplate = function (t, path) {
        console.log("admin.getMaintainersUpdateTemplate was called");
        getTemplate(t, "Maintainers", "#maintainers-update-template", undefined, "/ajax/admin/maintainers/update/" + path, remoteJSON, function () {
                $("#maintainers-update-form").validate({
                    rules: {
                        username: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        password: "required",
                        "confirm-password": {
                            required: true,
                            equalTo: "#password"
                        }
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/maintainers/update/" + path, admin.getFormData("#maintainers-update-form"), function () {
                            getMaintainersTemplate(5000);
                        });
                    }
                });
        });
        console.log("Does it exist yet: " + $("#maintainers-update-form").length);
    };

    var getFormData = function (formId) {
        console.log("admin.getFormData was called");
        var formInputs = $(formId + ' :input').not(':input[type=button], :input[type=submit]');
        var obj = {};
        formInputs.each(function () {
            var cc = $.camelCase(this.id);
            if ($(this).is(':checkbox')) {
                console.log("I am a checkbox");
                obj[cc] = $(this).is(':checked');
            } else {
                console.log("I am not a checkbox");
                obj[cc] = $(this).val();
            }
        });
        return obj;
    };

    var sendFormData = function (url, data, cb) {
        console.log("admin.sendFormData was called");
        $.ajax({
            url: url,
            type: "POST",
            contentType: "application/json, charset=utf-8",
            data: JSON.stringify(data),
            dataType: "json"
        })
        .done(function (data) {
            console.log("ajax POST to " + url);
            checkResult(data, cb);
        })
        .fail(function (e) {
            console.log("fail from ajax POST to " + url);
            getMsgTemplate("#error-template", "There was an issue communicating with the server.");
        });
    };

    var deleteForm = function (url, formId) {
        var obj = getFormData(formId);
        obj['delete'] = true;
        sendFormData(url, obj);
        getMaintainersTemplate(5000);
    };

    return {
        getMsgTemplate: getMsgTemplate,
        checkResult: checkResult,
        clearMsg: clearMsg,
        getTemplate: getTemplate,
        remoteJSON: remoteJSON,
        getAdminTemplate: getAdminTemplate,
        getMaintainersTemplate: getMaintainersTemplate,
        getMaintainersCreateTemplate: getMaintainersCreateTemplate,
        getMaintainersUpdateTemplate: getMaintainersUpdateTemplate,
        getFormData: getFormData,
        sendFormData: sendFormData,
        deleteForm: deleteForm
    };
}());

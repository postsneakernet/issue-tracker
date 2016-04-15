var admin = (function () {
    $(document).ready(function () {
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
        var source = $(templateId).html();
        var template = Handlebars.compile(source);
        var context = {"js_msg": msg};
        var html = template(context);
        $(".js-msg-placeholder").append(html);
    };

    var checkResult = function (context, cb) {
        if (context.hasOwnProperty('error')) {
            getMsgTemplate("#error-template", context.error);
        } else if (context.hasOwnProperty('success')) {
            getMsgTemplate("#success-template", context.success);
            if (undefined !== cb) {
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
        setTimeout(function () {
            $(".flask-msg-placeholder").empty();
            $(".js-msg-placeholder").empty();
        }, t);
    };

    var getTemplate = function (t, pageTitle, templateId, context, url, func, cb) {
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
        $.getJSON(url, {
        })
        .done(function (data) {
            var context = data;
            checkResult(context);
            var html = template(context);
            $(".content-placeholder").html(html);
            if (undefined !== cb) {
                cb();
            }
        })
        .fail(function (e) {
            getMsgTemplate("#error-template", "There was an issue communicating with the server.");
        });
    };

    var getAdminTemplate = function (t) {
        getTemplate(t, "Admin", "#admin-template", undefined, "/ajax/admin/", remoteJSON);
    };

    var getMaintainersTemplate = function (t) {
        getTemplate(t, "Maintainers", "#maintainers-template", undefined,
                "/ajax/admin/maintainers/", remoteJSON);
    };

    var getMaintainersCreateTemplate = function (t) {
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
                admin.sendFormData("/ajax/admin/maintainers/create/",
                        admin.getFormData("#maintainers-create-form"));
            }
        });
    };

    var getMaintainersUpdateTemplate = function (t, path) {
        getTemplate(t, "Maintainers", "#maintainers-update-template", undefined,
                "/ajax/admin/maintainers/update/" + path, remoteJSON, function () {
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
                        admin.sendFormData("/ajax/admin/maintainers/update/" + path,
                                admin.getFormData("#maintainers-update-form"), function () {
                            getMaintainersTemplate(5000);
                        });
                    }
                });
        });
    };

    var getProjectsTemplate = function (t) {
        getTemplate(t, "Projects", "#projects-template", undefined, "/ajax/admin/projects/",
                remoteJSON, function () {
            $(function () {
                $('[data-toggle="tooltip"]').tooltip();
            });
        });
    };

    var getProjectsCreateTemplate = function (t) {
        getTemplate(t, "Projects", "#projects-create-template", undefined,
                "/ajax/admin/projects/create/", remoteJSON, function () {
                $("#projects-create-form").validate({
                    rules: {
                        title: "required",
                        description: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/projects/create/",
                                admin.getFormData("#projects-create-form"));
                    }
                });
        });
    };

    var getProjectsUpdateTemplate = function (t, path) {
        getTemplate(t, "Projects", "#projects-update-template", undefined,
                "/ajax/admin/projects/update/" + path, remoteJSON, function () {
                $("#projects-update-form").validate({
                    rules: {
                        title: "required",
                        description: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/projects/update/" + path,
                                admin.getFormData("#projects-update-form"), function () {
                            getProjectsTemplate(5000);
                        });
                    }
                });
        });
    };

    var getTicketsTemplate = function (t) {
        getTemplate(t, "Tickets", "#tickets-template", undefined, "/ajax/admin/tickets/",
                remoteJSON, function () {
            $(function () {
                $('[data-toggle="tooltip"]').tooltip();
            });
        });
    };

    var getTicketsCreateTemplate = function (t) {
        getTemplate(t, "Tickets", "#tickets-create-template", undefined,
                "/ajax/admin/tickets/create/", remoteJSON, function () {
                $("#tickets-create-form").validate({
                    rules: {
                        name: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        title: "required",
                        content: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/tickets/create/",
                                admin.getFormData("#tickets-create-form"));
                    }
                });
        });
    };

    var getTicketsUpdateTemplate = function (t, path) {
        getTemplate(t, "Tickets", "#tickets-update-template", undefined,
                "/ajax/admin/tickets/update/" + path, remoteJSON, function () {
                $("#tickets-update-form").validate({
                    rules: {
                        name: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        title: "required",
                        content: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/tickets/update/" + path,
                                admin.getFormData("#tickets-update-form"), function () {
                            getTicketsTemplate(5000);
                        });
                    }
                });
        });
    };

    var getCommentsTemplate = function (t) {
        getTemplate(t, "Comments", "#comments-template", undefined, "/ajax/admin/comments/",
                remoteJSON, function () {
            $(function () {
                $('[data-toggle="tooltip"]').tooltip();
            });
        });
    };

    var getCommentsCreateTemplate = function (t) {
        getTemplate(t, "Comments", "#comments-create-template", undefined,
                "/ajax/admin/comments/create/", remoteJSON, function () {
                $("#comments-create-form").validate({
                    rules: {
                        name: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        content: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/comments/create/",
                                admin.getFormData("#comments-create-form"));
                    }
                });
        });
    };

    var getCommentsUpdateTemplate = function (t, path) {
        getTemplate(t, "Comments", "#comments-update-template", undefined,
                "/ajax/admin/comments/update/" + path, remoteJSON, function () {
                $("#comments-update-form").validate({
                    rules: {
                        name: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        content: "required",
                    },
                    submitHandler: function () {
                        admin.sendFormData("/ajax/admin/comments/update/" + path,
                                admin.getFormData("#comments-update-form"), function () {
                            getCommentsTemplate(5000);
                        });
                    }
                });
        });
    };

    var getFormData = function (formId) {
        var formInputs = $(formId + ' :input').not(':input[type=button], :input[type=submit]');
        var obj = {};
        formInputs.each(function () {
            var cc = $.camelCase(this.id);
            if ($(this).is(':checkbox')) {
                obj[cc] = $(this).is(':checked');
            } else {
                obj[cc] = $(this).val();
            }
        });
        return obj;
    };

    var sendFormData = function (url, data, cb) {
        $.ajax({
            url: url,
            type: "POST",
            contentType: "application/json, charset=utf-8",
            data: JSON.stringify(data),
            dataType: "json"
        })
        .done(function (data) {
            checkResult(data, cb);
        })
        .fail(function (e) {
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
        getProjectsTemplate: getProjectsTemplate,
        getProjectsCreateTemplate: getProjectsCreateTemplate,
        getProjectsUpdateTemplate: getProjectsUpdateTemplate,
        getTicketsTemplate: getTicketsTemplate,
        getTicketsCreateTemplate: getTicketsCreateTemplate,
        getTicketsUpdateTemplate: getTicketsUpdateTemplate,
        getCommentsTemplate: getCommentsTemplate,
        getCommentsCreateTemplate: getCommentsCreateTemplate,
        getCommentsUpdateTemplate: getCommentsUpdateTemplate,
        getFormData: getFormData,
        sendFormData: sendFormData,
        deleteForm: deleteForm
    };
}());

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

    return {
        setActive: setActive,
        updateActive: updateActive,
        setClass: setClass
    };
}());

/* Project specific Javascript goes here. */
function notify(message, cssClass) {
    cssClass = cssClass || 'alert-info';

    var $notification = $('#js-notification')
    $notification.text(message)
    $notification.addClass(cssClass)
    $notification.show();
}

notify.success = function(message) {
    notify(message, 'alert-success');
}

notify.info = function(message) {
    notify(message, 'alert-info');
}

notify.warn = function(message) {
    notify(message, 'alert-warning');
}

notify.error = function(message) {
    notify(message, 'alert-danger');
}

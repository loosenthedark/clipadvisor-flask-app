$(document).ready(function () {
    $(".review-submit-form-field").focusin(function () {
        $(this).prev().addClass("barber-red");
        $(this).next().addClass("barber-red");
    });
    $(".review-submit-form-field").focusout(function () {
        $(this).prev().removeClass("barber-red");
        $(this).next().removeClass("barber-red");
    });
    // jQuery DateTimePicker with dark theme source code: https://github.com/xdan/datetimepicker
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();
    today = dd + '-' + mm + '-' + yyyy;
    $('#review-submit-form-date-picker').datetimepicker(
        {
            timepicker: false,
            datepicker: true,
            weeks: false,
            format: 'd-m-Y',
            maxDate: '0'
        })
    $('#review-submit-form-time-picker').datetimepicker(
        {
            timepicker: true,
            datepicker: false,
            format: 'H:i',
            hours12: false,
            step: 30,
            defaultTime: '09:00'
        })

    // Rudimentary jQuery form checkbox validation to ensure users select at least one option - adapted from https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html

    $("#review-submit-form").submit(function () {
        if ($('.payment-checkbox').filter(':checked').length < 1) {
            alert("Please list at least one payment option!");
            return false;
        }
    });

    // Move form card container(s) upwards (collapse space) if alert appears
    if ($('.flash-message-container').height() > 10) {
        $('.flash-message-container').next().addClass('pull-content-up');
    }
    if ($('.flash-message-container').height() < 10) {
        $('.flash-message-container').next().removeClass('pull-content-up');
    }
    // Undo this action when alert is dismissed
    $('#flash-message-dismiss').click(function () {
        $('.flash-message-container').next().removeClass('pull-content-up');
    })
});
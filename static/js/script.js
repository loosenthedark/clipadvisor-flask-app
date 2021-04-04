$(document).ready(function () {

    // Customised colour change on form input focus
    $(".review-submit-form-field").focusin(function () {
        $(this).prev().addClass("barber-red");
        $(this).next().addClass("barber-red");
    });
    $(".review-submit-form-field").focusout(function () {
        $(this).prev().removeClass("barber-red");
        $(this).next().removeClass("barber-red");
    });

    $("#review-submit-form select").focusin(function () {
        $(this).prev().prev().addClass("barber-red");
    });

    $("#review-submit-form select").focusout(function () {
        $(this).prev().prev().removeClass("barber-red");
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
            defaultTime: '06:00',
            allowTimes:[
            '06:00', '06:30', '07:00', '07:30','08:00', '08:30','09:00', '09:30','10:00', '10:30','11:00', '11:30','12:00', '12:30','13:00', '13:30','14:00', '14:30','15:00', '15:30','16:00', '16:30','17:00', '17:30','18:00', '18:30','19:00', '19:30','20:00', '20:30','21:00', '21:30','22:00', '22:30','23:00', '23:30'
            ]
        })

    // Rudimentary jQuery form checkbox and radio button input validation to ensure users select at least one booking and payment option, as well as providing a 'star rating' - adapted from https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html

    $("#review-submit-form").submit(function () {
        if ($('.booking-checkbox').filter(':checked').length < 1) {
            alert("Please list at least one booking option!");
            return false;
        }
    });

    $("#review-submit-form").submit(function () {
        if ($('.payment-checkbox').filter(':checked').length < 1) {
            alert("Please list at least one payment option!");
            return false;
        }
    });

    $("#review-submit-form").submit(function () {
        if(!$('input[name="review-submit-form-star-rating"]').is(':checked')) { alert("it's not checked!"); }
    });

    // Move form card container(s) upwards (collapse space) if alert appears
    if ($('.flash-message-container').height() > 10) {
        $('.flash-message-container').next().addClass('pull-content-up');
        $('.register-form-card, .review-submit-form-card, .reviews-card').removeClass('mt-3');
    }
    if ($('.flash-message-container').height() < 10) {
        $('.flash-message-container').next().removeClass('pull-content-up');
        $('.register-form-card, .review-submit-form-card, .reviews-card').addClass('mt-3');
    }

    // Undo this action when alert is dismissed
    $('#flash-message-dismiss').click(function () {
        $('.flash-message-container').next().removeClass('pull-content-up');
        $('.register-form-card, .review-submit-form-card, .reviews-card').addClass('mt-3');
    })

    // // Tooltips Initialization
    // $('[data-toggle="tooltip"]').tooltip()

});
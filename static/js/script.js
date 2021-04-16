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

  // Flexible-height textarea (adjusts up and down to accommodate user-inputted text content) as suggested here: https://stackoverflow.com/questions/454202/creating-a-textarea-with-auto-resize
  $("textarea")
    .each(function () {
      this.setAttribute(
        "style",
        "height:" + this.scrollHeight + "px;overflow-y:hidden;"
      );
    })
    .on("input", function () {
      this.setAttribute("style", "max-height: unset;")
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    });

  // jQuery DateTimePicker with dark theme source code: https://github.com/xdan/datetimepicker

  var today = new Date();
  var dd = String(today.getDate()).padStart(2, "0");
  var mm = String(today.getMonth() + 1).padStart(2, "0");
  var yyyy = today.getFullYear();
  today = dd + "-" + mm + "-" + yyyy;
  $(
    "#review-submit-form-date-picker, #review-update-form-date-picker"
  ).datetimepicker({
    timepicker: false,
    datepicker: true,
    weeks: false,
    format: "d-m-Y",
    maxDate: "0",
  });
  $(
    "#review-submit-form-time-picker, #review-update-form-time-picker"
  ).datetimepicker({
    timepicker: true,
    datepicker: false,
    format: "H:i",
    hours12: false,
    step: 30,
    defaultTime: "06:00",
    allowTimes: [
      "06:00",
      "06:30",
      "07:00",
      "07:30",
      "08:00",
      "08:30",
      "09:00",
      "09:30",
      "10:00",
      "10:30",
      "11:00",
      "11:30",
      "12:00",
      "12:30",
      "13:00",
      "13:30",
      "14:00",
      "14:30",
      "15:00",
      "15:30",
      "16:00",
      "16:30",
      "17:00",
      "17:30",
      "18:00",
      "18:30",
      "19:00",
      "19:30",
      "20:00",
      "20:30",
      "21:00",
      "21:30",
      "22:00",
      "22:30",
      "23:00",
      "23:30",
    ],
  });

  // Rudimentary jQuery form checkbox and radio button input validation to ensure users select at least one booking and payment option, as well as providing a 'star rating' - adapted from https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html

  $("#review-submit-form").submit(function () {
    if (
      $("#review-submit-form-customer-name").val().length >= 4 &&
      $("#review-submit-form-customer-name").val().length <= 50 &&
      $("#review-submit-form-barbershop-name").val().length >= 3 &&
      $("#review-submit-form-barbershop-name").val().length <= 50 &&
      $("#review-submit-form-date-picker").val() != "" &&
      $("#review-submit-form-time-picker").val() != "" &&
      $("#review-submit-form-comments").val().length >= 10 &&
      $("#review-submit-form-comments").val().length <= 1000 &&
      $(".booking-checkbox").filter(":checked").length < 1
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>Please provide at least one booking option <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Submit A Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $(".review-submit-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
    if (
      $("#review-submit-form-customer-name").val().length >= 4 &&
      $("#review-submit-form-customer-name").val().length <= 50 &&
      $("#review-submit-form-barbershop-name").val().length >= 3 &&
      $("#review-submit-form-barbershop-name").val().length <= 50 &&
      $("#review-submit-form-date-picker").val() != "" &&
      $("#review-submit-form-time-picker").val() != "" &&
      $("#review-submit-form-comments").val().length >= 10 &&
      $("#review-submit-form-comments").val().length <= 1000 &&
      $(".payment-checkbox").filter(":checked").length < 1
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>Please provide at least one payment option <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Submit A Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $(".review-submit-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
    if (
      $("#review-submit-form-customer-name").val().length >= 4 &&
      $("#review-submit-form-customer-name").val().length <= 50 &&
      $("#review-submit-form-barbershop-name").val().length >= 3 &&
      $("#review-submit-form-barbershop-name").val().length <= 50 &&
      $("#review-submit-form-date-picker").val() != "" &&
      $("#review-submit-form-time-picker").val() != "" &&
      $("#review-submit-form-comments").val().length >= 10 &&
      $("#review-submit-form-comments").val().length <= 1000 &&
      !$('input[name="review-submit-form-star-rating"]').is(":checked")
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>You forgot to give your barber a star rating!</br>Please try again <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Submit A Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $(".review-submit-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
  });

  $("#review-update-form").submit(function () {
    if (
      $("#review-update-form-customer-name").val().length >= 4 &&
      $("#review-update-form-customer-name").val().length <= 50 &&
      $("#review-update-form-barbershop-name").val().length >= 3 &&
      $("#review-update-form-barbershop-name").val().length <= 50 &&
      $("#review-update-form-date-picker").val() != "" &&
      $("#review-update-form-time-picker").val() != "" &&
      $("#review-update-form-comments").val().length >= 10 &&
      $("#review-update-form-comments").val().length <= 1000 &&
      $(".booking-checkbox").filter(":checked").length < 1
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>Please provide at least one booking option <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Update Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $("#alert-info-review-update").removeClass("mt-3 mt-md-4 mt-xl-3");
      $("#alert-info-review-update-container").addClass("push-down");
      $(".review-update-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
    if (
      $("#review-update-form-customer-name").val().length >= 4 &&
      $("#review-update-form-customer-name").val().length <= 50 &&
      $("#review-update-form-barbershop-name").val().length >= 3 &&
      $("#review-update-form-barbershop-name").val().length <= 50 &&
      $("#review-update-form-date-picker").val() != "" &&
      $("#review-update-form-time-picker").val() != "" &&
      $("#review-update-form-comments").val().length >= 10 &&
      $("#review-update-form-comments").val().length <= 1000 &&
      $(".payment-checkbox").filter(":checked").length < 1
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>Please provide at least one payment option <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Update Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $("#alert-info-review-update").removeClass("mt-3 mt-md-4 mt-xl-3");
      $("#alert-info-review-update-container").addClass("push-down");
      $(".review-update-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
    if (
      $("#review-update-form-customer-name").val().length >= 4 &&
      $("#review-update-form-customer-name").val().length <= 50 &&
      $("#review-update-form-barbershop-name").val().length >= 3 &&
      $("#review-update-form-barbershop-name").val().length <= 50 &&
      $("#review-update-form-date-picker").val() != "" &&
      $("#review-update-form-time-picker").val() != "" &&
      $("#review-update-form-comments").val().length >= 10 &&
      $("#review-update-form-comments").val().length <= 1000 &&
      !$('input[name="review-update-form-star-rating"]').is(":checked")
    ) {
      // customised Flash message
      $(".flash-message-container").html(
        '<div class="alert alert-warning py-2_5 pl-3 pr-4 my-3 mb-0 my-md-4 my-xl-3 text-center fade show alert-dismissible flash-msg-box-top" role="alert"><strong>You forgot to give your barber a star rating!</br>Please try again <i class="fas fa-cut"></i></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close" id="flash-message-dismiss"><span aria-hidden="true">&times;</span></button></div>'
      ).css({
        width: $(".main-container > div:first-child").width() + "px",
      });

      // reposition Update Review form container
      $(".flash-message-container").next().addClass("pull-content-up");
      $("#alert-info-review-update").removeClass("mt-3 mt-md-4 mt-xl-3");
      $("#alert-info-review-update-container").addClass("push-down");
      $(".review-update-form-card")
        .removeClass("mt-3 mt-md-4 mt-xl-3")
        .addClass("push-down");
      return false;
    }
  });

  // Move form card container(s) upwards (collapse space) if alert appears

  if ($(".flash-message-container").height() > 10) {
    $(
      ".register-form-card, .review-submit-form-card, .review-update-form-card, .reviews-card, #alert-info-review-update"
    ).removeClass("mt-3 mt-md-4 mt-xl-3");
    $(".flash-message-container").next().addClass("pull-content-up");
    $(
      ".reviews-card, .review-submit-form-card, .review-update-form-card"
    ).addClass("push-down");
  }

  if ($("#alert-info-review-update-container").height() > 10) {
    $(".review-update-form-card").removeClass("mt-3 mt-md-4 mt-xl-3");
    $(".main-container").addClass("pull-content-up");
    $(".review-update-form-card, #alert-info-review-update-container").addClass("push-down");
  }

  if ($(".review-submit-form-card").parent().hasClass("pull-content-up")) {
    $(".review-submit-form-card").parent().addClass("justify-content-xl-start");
  }

  if ($(".review-update-form-card").parent().hasClass("pull-content-up")) {
    $(".review-update-form-card").parent().addClass("justify-content-xl-start");
  }

  // Undo this action when alert is dismissed

  $(".flash-message-container").on(
    "click",
    "#flash-message-dismiss",
    function () {
      $(".flash-message-container").next().removeClass("pull-content-up");
      $(
        ".review-submit-form-card, .register-form-card, .reviews-card, #alert-info-review-update"
      ).addClass("mt-3 mt-md-4 mt-xl-3");
      if ($("#alert-info-review-update-container").height() < 10) {
        $(".review-update-form-card").addClass("mt-3 mt-md-4 mt-xl-3");
      }
      $(
        ".reviews-card, .review-submit-form-card, .review-update-form-card, #alert-info-review-update-container"
      ).removeClass("push-down");
    }
  );

  // Keep review update form from pressing up against navbar when alert is dismissed

  $("#flash-message-review-update-dismiss").click(function () {
    if ($(".flash-message-container").height() < 10) {
      $(".review-update-form-card").addClass("mt-3 mt-md-4 mt-xl-3");
    }
  });

  // Darken vibe select menu text on Review Update page once user clicks to change selected value
  $(".review-update-form-field").focus(function () {
    $(this).removeClass("text-very-muted").addClass("barber-blue-text");
  });

  // Dynamic-width Flash message alert
  $(".flash-message-container > .alert").css({
    width: $(".main-container > div:first-child").width() + "px",
  });
  // augmented by alert resize on screen resize
  $(window).resize(function () {
    $(".flash-message-container > .alert").css({
      width: $(".main-container > div:first-child").width() + "px",
    });
  });

  // // Tooltips Initialization
  // $('[data-toggle="tooltip"]').tooltip()
});




/****** Popup Close *****/
function div_hide() {
    $('.form-info-box-green').fadeOut();
}

/****** Save function *****/
function submitHandle() {
    $('.form-info-box-green').fadeIn();
}





$(document).ready(function () {
    $('.slidewindow-hidden').hide()
});

$(".close-div").click(function(){
    $('#schedule, #new_appointment ,#available, #info,#update-info').animate({
        width: 'hide'
    }, "1000")
});

//$('.refused-link').click(function () {
//    $('#refused').animate({
//        width: 'show'
//    }, "1000")
//});

$('.schedule-link-notimeout').click(function () {
    $("#schedule").show();
});
$('.available-link-notimeout').click(function () {
    $("#available").show();
});
$('.refused-link-notimeout').click(function () {
    $("#refused").show();
});
$('.info-link-notimeout').click(function () {
    $("#update-info").show();
});


$('.schedule-link').click(function () {
    $('#schedule').animate({
        width: 'show'
    }, "1000")
});

$('.available-link').click(function () {
    $('#available').animate({
        width: 'show'
    }, "1000")
});

$('.update-info-link').click(function () {
    $('#update-info').animate({
        width: 'show'
    }, "1000")
});


$('.info-link').click(function () {
    $('#schedule, #refused ,#available, #update-info').hide();
    $('#info').animate({
        width: 'show'
    }, "1000")
});

$(document).ready(function() {
    $('.show-search').click(function() {
      $(this).next().delay(5000).toggleClass('toggle');
    });
  });
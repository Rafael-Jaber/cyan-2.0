$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
         theme: "minimal"
    });
    $("#sidemod").mCustomScrollbar({
        theme: "minimal"
    });

});

function menuHide() {
        $('#sidebar').toggleClass('deactive-menu', 'active-menu');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
}

function moduleHide() {
    $('#sidemod').toggleClass('active-mod');
    $('.overlay').toggleClass('active');
}
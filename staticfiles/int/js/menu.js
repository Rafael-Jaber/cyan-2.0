$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
         theme: "minimal"
    });
    $("#sidemod").mCustomScrollbar({
        theme: "minimal"
    });

    let mediaQueryList = window.matchMedia('print');
    mediaQueryList.addListener(function(mql) {
      if(mql.matches) {
        console.log('webkit equivalent of onbeforeprint');
      }
    });
});

function menuHide() {
        $('#sidebar').toggleClass('deactive-menu', 'active-menu');
        $('#sidebar2').toggleClass('deactive-menu', 'active-menu');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
}

function moduleHide() {
    $('#sidemod').toggleClass('active-mod');
    $('.overlay').toggleClass('active');
}


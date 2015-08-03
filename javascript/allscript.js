$(document).ready(function() {
    $("body").css("display", "none");

    $("body").fadeIn(2000);

    $("a.transition").click(function(event){
        event.preventDefault();
        linkLocation = this.href;
        $("body").fadeOut(1000, redirectPage);
    });

    function redirectPage() {
        window.location = linkLocation;
    }
});
$(function(){
  function fade() {
    $("#MainIsmsageB1").fadeOut(6000);
  }
    $("#MainImsageB1").hover(fade);
});

$(function() {

    $("#Math").click(function () {
      $(".subj").css("display", "none")

      $(".mathbubbles")
          .css("display", "block")
          .animate({ opacity: 1 }, 500)
     });

     $("#Science").click(function () {
       $(".subj").css("display", "none")

       $(".sciencebubbles")
           .css("display", "block")
           .animate({ opacity: 1 }, 500)
      });

      $("#History").click(function () {
        $(".subj").css("display", "none")

        $(".historybubbles")
            .css("display", "block")
            .animate({ opacity: 1 }, 500)
       });

       $("#Comp").click(function () {
         $(".subj").css("display", "none")

         $(".csbubbles")
             .css("display", "block")
             .animate({ opacity: 1 }, 500)
        });

    $("body")
        .css("opacity", 0)
        .animate({ opacity: 1 }, 1000);

    // $("a.transition").click(function(event){
    //     event.preventDefault();
    //     linkLocation = this.href;
    //     $("body").fadeOut(1000, redirectPage);
    // });


    // $(function(){
    //   function fade() {
    //     $("#MainIsmsageB1").fadeOut(6000);
    //   }
    //     $("#MainImsageB1").hover(fade);




});

function redirectPage() {
    window.location = linkLocation;
}

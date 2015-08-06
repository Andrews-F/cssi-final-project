$(function() {

    $("#Math").click(function () {
      $(".subj").animate({ opacity: 0 }, 250);

      $(".mathbubbles")
          .css("display", "block")
          .animate({ opacity: 1 }, 500);
     });

     $("#Science").click(function () {
       $(".subj").animate({ opacity: 0 }, 250);

       $(".sciencebubbles")
           .css("display", "block")
           .animate({ opacity: 1 }, 500);
      });

      $("#History").click(function () {
        $(".subj").animate({ opacity: 0 }, 250);

        $(".historybubbles")
            .css("display", "block")
            .animate({ opacity: 1 }, 500);
       });

       $("#Comp").click(function () {
         $(".subj").animate({ opacity: 0 }, 250);

         $(".csbubbles")
             .css("display", "block")
             .animate({ opacity: 1 }, 500);
        });

    $("html")
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

// function redirectPage() {
//     window.location = linkLocation;
// }

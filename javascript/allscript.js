$(function() {

    $("#Math").click(function () {
      // fades out all other subject bubbles
      $(".subj").animate({ opacity: 0 }, 150);
      // fades in math bubbles
      $(".mathbubbles")
          .css("display", "block")
          .animate({ opacity: 1 }, 300);
     });

     $("#Science").click(function () {
       $(".subj").animate({ opacity: 0 }, 150);

       $(".sciencebubbles")
           .css("display", "block")
           .animate({ opacity: 1 }, 300);
      });

      $("#History").click(function () {
        $(".subj").animate({ opacity: 0 }, 150);

        $(".historybubbles")
            .css("display", "block")
            .animate({ opacity: 1 }, 300);
       });

       $("#Comp").click(function () {
         $(".subj").animate({ opacity: 0 }, 150);

         $(".csbubbles")
             .css("display", "block")
             .animate({ opacity: 1 }, 300);
        });

    $("html")
        .css("opacity", 0)
        .animate({ opacity: 1 }, 500);

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

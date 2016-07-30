
$(document).ready(function() {

    var x = 0;

	$("#owl-demo").owlCarousel({
   

        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true,
        autoPlay : 5000
   
    });


    $("#owl-demo2").owlCarousel({
      items : 3,
      mouseDrag: true,
      itemsDesktop : [1299,4],
      itemsDesktopSmall : [979,4]
 
    });


    $(".searchbar-open").click(function(){
          $(".menu").hide();
          //$(".searchbar").css({"display","none"});
          $(".searchbar-container").show(1000);
          
    });


     $(".glyphicon-remove").click(function(){
          $(".menu").show();
          //$(".searchbar").css({"display","none"});
          $(".searchbar-container").hide();
          $(".account-container").hide();
          
    });


    $(".account-open").click(function(){
          $(".menu").hide();
         // $(".account-container").show();
          
    });

    $(".bars").click(function(){

            $(".mobile-menu").toggle(1000);

    });

     $('.catalogue').click(function(){$('.main-menu-dropdown-panel').toggle(1000);});

    $("#clickable-dropdown").click(function(){

            $("#mobile-nav").toggle(1000);


    });

     $('.headings li').click(function(){
        var tab_id = $(this).index()+1;
        $('.headings li').removeClass('active');
        $('.content li').removeClass('active');
        $(this).addClass('active');
        //$('.content li:'+'nth-child('+tab_id+')').addClass('active');
        $('.content li:nth-child('+tab_id+')').addClass('active');
     });


     // if($(document).width()<768){
     //  console.log('hello');
     // }

    //  $(window).resize(function(){

    //    if ($(window).width() <= 768) {
    //     $('.positions').removeClass('js');
    //     $('.positions').addClass('show-for-small');
    //    } 

    //    else if($(window).width() <= 1280){
    //     $('.positions').removeClass('js');
    //     $('.positions').addClass('show-for-medium-only');
    //     // $('.div').removeClass('positions show-for-medium-only');
    //     // $('.positions').addClass('show-for-large-up');
    //    }

    //    else{

    //     $('.positions').removeClass('js');
    //     $('.positions').addClass('positions show-for-large-up');
    //     // $('.positions').removeClass('positions show-for-small');
    //     // $('.positions').addClass('show-for-medium-only');
    //    }

    // });

});

 

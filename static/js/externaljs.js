
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
         $(".account-container").show();
          
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

    $('#my-image').imageTooltip();
    

    // cart js

    $(".cart-form").submit(function(e) {

        var product_id = $('#id').val();
        var quantity = $('#quantity').val();
        var url = "http://127.0.0.1:8000/shopping-cart/add/"; // the script where you handle the form input.
        $.ajax({
               type: "POST",
               url: url,
               // data: $(".cart-form").serialize(), // serializes the form's elements.
               data: {id: product_id, qty: parseInt(quantity)}


               // success: function(data)
               // {
               //     alert(data); // show response from the php script.
               // }
             });

        e.preventDefault(); // avoid to execute the actual submit of the form.
    });


    $(".selectAnchor").click(function(event){
        event.preventDefault();
        var product_id = $(this).data("value");
        var $row = $(this).closest("tr");
        var url = "http://127.0.0.1:8000/shopping-cart/remove/"; // the script where you handle the form input.
        $.ajax({
          type: 'GET',
          url: url,
          data: { product_id: product_id },
          success: function(data){
                $row.find('td').fadeOut(1000,function(){
                    $row.remove();
                });
          }
        });
    });

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

 /* set Cookie to hide menu */
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

/* get Cookie to check hide menu */
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}


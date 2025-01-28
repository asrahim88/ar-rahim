/** 
 * ===================================================================
 * main js
 *
 * ------------------------------------------------------------------- 
 */ 

(function($) {

	"use strict";

	/*---------------------------------------------------- */
	/* Preloader
	------------------------------------------------------ */ 
   $(window).load(function() {

      // will first fade out the loading animation 
    	$("#loader").fadeOut("slow", function(){

        // will fade out the whole DIV that covers the website.
        $("#preloader").delay(300).fadeOut("slow");

      });       

  	})


  	/*---------------------------------------------------- */
  	/* FitText Settings
  	------------------------------------------------------ */
  	setTimeout(function() {

   	$('#intro h1').fitText(1, { minFontSize: '42px', maxFontSize: '84px' });

  	}, 100);


	/*---------------------------------------------------- */
	/* FitVids
	------------------------------------------------------ */ 
  	$(".fluid-video-wrapper").fitVids();


	/*---------------------------------------------------- */
	/* Owl Carousel
	------------------------------------------------------ */ 
	$("#owl-slider").owlCarousel({
        navigation: false,
        pagination: true,
        itemsCustom : [
	        [0, 1],
	        [700, 2],
	        [960, 3]
	     ],
        navigationText: false
    });


	/*----------------------------------------------------- */
	/* Alert Boxes
  	------------------------------------------------------- */
	$('.alert-box').on('click', '.close', function() {
	  $(this).parent().fadeOut(500);
	});	


	/*----------------------------------------------------- */
	/* Stat Counter
  	------------------------------------------------------- */
   var statSection = $("#stats"),
       stats = $(".stat-count");

   statSection.waypoint({

   	handler: function(direction) {

      	if (direction === "down") {       		

			   stats.each(function () {
				   var $this = $(this);

				   $({ Counter: 0 }).animate({ Counter: $this.text() }, {
				   	duration: 4000,
				   	easing: 'swing',
				   	step: function (curValue) {
				      	$this.text(Math.ceil(curValue));
				    	}
				  	});
				});

       	} 

       	// trigger once only
       	this.destroy();      	

		},
			
		offset: "90%"
	
	});	


	/*---------------------------------------------------- */
	/*	Masonry
	------------------------------------------------------ */
	var containerProjects = $('#folio-wrapper');

	containerProjects.imagesLoaded( function() {

		containerProjects.masonry( {		  
		  	itemSelector: '.folio-item',
		  	resize: true 
		});

	});


	/*----------------------------------------------------*/
	/*	Modal Popup
	------------------------------------------------------*/
   $('.item-wrap a').magnificPopup({

      type:'inline',
      fixedContentPos: false,
      removalDelay: 300,
      showCloseBtn: false,
      mainClass: 'mfp-fade'

   });

   $(document).on('click', '.popup-modal-dismiss', function (e) {
   	e.preventDefault();
   	$.magnificPopup.close();
   });

	
	/*-----------------------------------------------------*/
  	/* Navigation Menu
   ------------------------------------------------------ */  
   var toggleButton = $('.menu-toggle'),
       nav = $('.main-navigation');

   // toggle button
   toggleButton.on('click', function(e) {

		e.preventDefault();
		toggleButton.toggleClass('is-clicked');
		nav.slideToggle();

	});

   // nav items
  	nav.find('li a').on("click", function() {   

   	// update the toggle button 		
   	toggleButton.toggleClass('is-clicked'); 
   	// fadeout the navigation panel
   	nav.fadeOut();   		
   	     
  	});


   /*---------------------------------------------------- */
  	/* Highlight the current section in the navigation bar
  	------------------------------------------------------ */
	var sections = $("section"),
	navigation_links = $("#main-nav-wrap li a");	

	sections.waypoint( {

       handler: function(direction) {

		   var active_section;

			active_section = $('section#' + this.element.id);

			if (direction === "up") active_section = active_section.prev();

			var active_link = $('#main-nav-wrap a[href="#' + active_section.attr("id") + '"]');			

         navigation_links.parent().removeClass("current");
			active_link.parent().addClass("current");

		}, 

		offset: '25%'
	});


	/*---------------------------------------------------- */
  	/* Smooth Scrolling
  	------------------------------------------------------ */
  	$('.smoothscroll').on('click', function (e) {
	 	
	 	e.preventDefault();

   	var target = this.hash,
    	$target = $(target);

    	$('html, body').stop().animate({
       	'scrollTop': $target.offset().top
      }, 800, 'swing', function () {
      	window.location.hash = target;
      });

  	});  
  

   /*---------------------------------------------------- */
	/*  Placeholder Plugin Settings
	------------------------------------------------------ */ 
	$('input, textarea, select').placeholder()  


  	/*---------------------------------------------------- */
	/*	contact form
	------------------------------------------------------ */

	/* local validation */
	// $('#contactForm').validate({

	// 	/* submit via ajax */
	// 	submitHandler: function(form) {

	// 		var sLoader = $('#submit-loader');

	// 		$.ajax({      	

	// 	      type: "POST",
	// 	      url: "inc/sendEmail.php",
	// 	      data: $(form).serialize(),
	// 	      beforeSend: function() { 

	// 	      	sLoader.fadeIn(); 

	// 	      },
	// 	      success: function(msg) {

	//             // Message was sent
	//             if (msg == 'OK') {
	//             	sLoader.fadeOut(); 
	//                $('#message-warning').hide();
	//                $('#contactForm').fadeOut();
	//                $('#message-success').fadeIn();   
	//             }
	//             // There was an error
	//             else {
	//             	sLoader.fadeOut(); 
	//                $('#message-warning').html(msg);
	// 	            $('#message-warning').fadeIn();
	//             }

	// 	      },
	// 	      error: function() {

	// 	      	sLoader.fadeOut(); 
	// 	      	$('#message-warning').html("Something went wrong. Please try again.");
	// 	         $('#message-warning').fadeIn();

	// 	      }

	//       });     		
  	// 	}

	// });


 	/*----------------------------------------------------- */
  	/* Back to top
   ------------------------------------------------------- */ 
	var pxShow = 300; // height on which the button will show
	var fadeInTime = 400; // how slow/fast you want the button to show
	var fadeOutTime = 400; // how slow/fast you want the button to hide
	var scrollSpeed = 300; // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'

   // Show or hide the sticky footer button
	jQuery(window).scroll(function() {

		if (!( $("#header-search").hasClass('is-visible'))) {

			if (jQuery(window).scrollTop() >= pxShow) {
				jQuery("#go-top").fadeIn(fadeInTime);
			} else {
				jQuery("#go-top").fadeOut(fadeOutTime);
			}

		}		

	});		

})(jQuery);

// ------------------: custom js :---------------------
// Get the current year
const currentYear = new Date().getFullYear();

// Set the copyright text dynamically
document.getElementById('copyright').textContent = `© Copyright ${currentYear}`;

const skills = document.querySelectorAll('.s-skill');

skills.forEach(skill => {
    skill.addEventListener('click', () => {
        alert(skill.getAttribute('data-tooltip'));
    });
});

// <--------------: custom js start :----------------->

// <-------: bounce ball of Contact Form Start :----->

// <-------: bounce ball of Contact Form end :----->


// <--------------: form reload start :------------->
const contactForm = document.getElementById('contactForm');
const responseMessage = document.getElementById('responseMessage');
const submitLoader = document.getElementById('submit-loader');

contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // ফর্ম রিলোড বন্ধ করা

    // লোডার দেখান
    submitLoader.style.display = 'block';

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        // লোডার hide করুন
        submitLoader.style.display = 'none';

        if (data.success) {
            responseMessage.innerHTML = `<p style="color: #FF0077; text-align: center;">${data.message}</p>`; // সফল মেসেজ
            contactForm.reset(); // ফর্ম রিসেট

            // **৫ সেকেন্ড পর মেসেজ ভ্যানিশ**
            setTimeout(() => {
                responseMessage.innerHTML = '';
            }, 5000); // ৫০০০ মিলিসেকেন্ড = ৫ সেকেন্ড
        } else {
            let errorMessages = '';
            for (const [field, messages] of Object.entries(data.errors)) {
                errorMessages += `<p style="color: red;">${field}: ${messages.join(', ')}</p>`;
            }
            responseMessage.innerHTML = errorMessages; // এরর মেসেজ দেখানো
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // লোডার hide করুন
        submitLoader.style.display = 'none';
        responseMessage.innerHTML = `<p style="color: red;">An unexpected error occurred. Please try again.</p>`;
    });
});

// <--------------: form reload end :------------->


// <--------------: auto type start :------------->
// Django থেকে পাঠানো ডাটা

const titleElement = document.getElementById('dynamic-title');

let currentIndex = 0; // কোন টাইটেল দেখানো হচ্ছে তা ট্র্যাক করে
let charIndex = 0;    // টাইটেলের কোন ক্যারেক্টার টাইপ হচ্ছে তা ট্র্যাক করে

function typeTitle() {
	titleElement.classList.add('typing'); // টাইপিং শুরু হলে আন্ডারলাইন দেখাও

	if (charIndex < titles[currentIndex].length) {
		// একটি একটি করে ক্যারেক্টার যোগ করা
		titleElement.textContent += titles[currentIndex][charIndex];
		charIndex++;
		setTimeout(typeTitle, 100); // প্রতি ক্যারেক্টারের মধ্যে ১০০ms
	} else {
		// পুরো টাইটেল টাইপ হয়ে গেলে আন্ডারলাইন রাখো এবং ২ সেকেন্ড অপেক্ষা করো
		setTimeout(() => {
			titleElement.classList.remove('typing'); // আন্ডারলাইন সরাও
			setTimeout(eraseTitle, 500); // মুছার আগে সামান্য বিরতি
		}, 2000);
	}
}

function eraseTitle() {
	if (charIndex > 0) {
		// একটি একটি করে ক্যারেক্টার মুছে ফেলা
		titleElement.textContent = titles[currentIndex].slice(0, charIndex - 1);
		charIndex--;
		setTimeout(eraseTitle, 50); // প্রতি মুছে ফেলার মধ্যে ৫০ms
	} else {
		// পরবর্তী টাইটেলে যাও
		currentIndex = (currentIndex + 1) % titles.length;
		typeTitle(); // নতুন টাইটেল টাইপ করা শুরু
	}
}

// টাইপিং ইফেক্ট শুরু
typeTitle();
// <--------------: auto type end :------------->



// <--------------: custom js end :----------------->



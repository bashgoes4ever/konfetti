$(document).ready(function(){


	// $('.block5__slider').owlCarousel({
	// 	responsiveClass:true,
	// 	items: 1,
	// 	addClassActive: true,
	// 	nav: true,
	// 	navText: ["<img src='img/icons/prev.png'/>", 
	// 			"<img src='img/icons/next.png'/>"],
 //    })

	// $('.block7__slider').owlCarousel({
	// 	responsiveClass:true,
	// 	margin: 30,
	// 	addClassActive: true,
	// 	nav: true,
	// 	navText: ["<img src='img/icons/prev.png'/>", 
	// 			"<img src='img/icons/next.png'/>"],
	// 	responsive:{
	//         0:{
	//             items:1
	//         },
	//         750:{
	//             items:2
	//         },
	//         1170:{
	//             items:4
	//         }
	//     },
 //    })

    $('.nav__button').click(function(){
		$('.nav__flex').addClass('nav__flex-active')
	})
	$('.close-nav').click(function(){
		$('.nav__flex').removeClass('nav__flex-active')
	})

	$('.block10__menu__item').click(function(){
		$(this).toggleClass('block10__menu__item-active')
	})

	function slide_down(select) {
		var destination = select.offset().top;
		$('html, body').animate({ scrollTop: destination}, 500);
		return false; 
	}

	// $('.block9__button').click(function(){
	// 	slide_down($('.block10'))
	// })

	$(document).on('click', '.nav__flex a', function(){
		if ($('.nav__flex').hasClass('nav__flex-active')) {
			$('.nav__flex').removeClass('nav__flex-active')
		}
	})

	$('.contacts-btn').click(function(e){
		e.preventDefault()
		slide_down($('.block8'))
		if ($('.nav__flex').hasClass('nav__flex-active')) {
			$('.nav__flex').removeClass('nav__flex-active')
		}
	})

	$('.phone__callback').click(function(){
		document.body.style.overflow = 'hidden';
		$('.callback-popup input[name="type"]').val($(this).data('type'))
		$('.layer').fadeIn(300)
		$('.callback-popup').fadeIn(500)
	})

	$(document).on('click', '.block7__item .link', function(){
		document.body.style.overflow = 'hidden';
		$('.callback-popup input[name="type"]').val($(this).data('type'))
		$('.layer').fadeIn(300)
		$('.callback-popup').fadeIn(500)
	})

	$(document).on('click', '.block6__item', function(e){
		e.preventDefault(e)
		document.body.style.overflow = 'hidden';
		$('.layer').fadeIn(300)
		$('.ideas-popup').fadeIn(500)	
		$('.ideas-popup .title').text($(this).data('title'))	
		$('.ideas-popup .text').text($(this).data('text'))	
		$('.ideas-popup img').attr('src', $(this).data('image'))	
	})

	$('.layer').click(function(e){
		if ($(this).has(e.target).length === 0) {
			document.body.style.overflow = 'scroll';
			$('.layer').fadeOut(300)
			$('.popup').fadeOut(300)
			$('.thank').fadeOut(300)
		}
	})

	$(document).on('submit', 'form', function(e){
		e.preventDefault(e)
		$.ajax({
			type: "POST",
			url: "http://127.0.0.1:8000/api/v1/order/",
			data: {
				'name': $(this).children('input[name="name"]').val(),
				'phone': $(this).children('input[name="phone"]').val(),
				'text': $(this).children('textarea[name="text"]').val(),
				't': $(this).children('input[name="type"]').val()
			},
		}).done(function() {
			$('.layer').fadeIn(300)
			$('.popup').fadeOut(200)
			$('.thank').fadeIn(300)
		});
		return false;
	})

	// $(document).on('load', function(e){
	// 	$('.block10__menu-mobile').select2()
	// })
	//$('.block10__menu-mobile').select2()


	

})
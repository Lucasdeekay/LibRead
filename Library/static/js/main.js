$(function(){

	/*============= Admin Tab =============*/
	$('#ebook-section').hide();
	$('#blog-section').hide();
	$('#user-auth-section').hide();
	$('#journal-auth-section').hide();

	$('#ebook-button').click(function(){
	    $('#ebook-section').show();
	    $('#ebook-button').addClass('is-active');
	    $('#journal-section').hide();
	    $('#journal-button').removeClass('is-active');
	    $('#blog-section').hide();
	    $('#blog-button').removeClass('is-active');
	    $('#user-auth-section').hide();
	    $('#user-auth-button').removeClass('is-active');
	    $('#journal-auth-section').hide();
	    $('#journal-auth-button').removeClass('is-active');
	});
	$('#journal-button').click(function(){
	    $('#ebook-section').hide();
	    $('li').removeClass('is-active');
	    $('#journal-section').show();
	    $('#journal-button').addClass('is-active');
	    $('#blog-section').hide();
	    $('#blog-button').removeClass('is-active');
	    $('#user-auth-section').hide();
	    $('#user-auth-button').removeClass('is-active');
	    $('#journal-auth-section').hide();
	    $('#journal-auth-button').removeClass('is-active');
	});
	$('#blog-button').click(function(){
	    $('#ebook-section').hide();
	    $('#ebook-button').removeClass('is-active');
	    $('#journal-section').hide();
	    $('#journal-button').removeClass('is-active');
	    $('#blog-section').show();
	    $('#blog-button').addClass('is-active');
	    $('#user-auth-section').hide();
	    $('#user-auth-button').removeClass('is-active');
	    $('#journal-auth-section').hide();
	    $('#journal-auth-button').removeClass('is-active');
	});
	$('#user-auth-button').click(function(){
	    $('#ebook-section').hide();
	    $('#ebook-button').removeClass('is-active');
	    $('#journal-section').hide();
	    $('#journal-button').removeClass('is-active');
	    $('#blog-section').hide();
	    $('#blog-button').removeClass('is-active');
	    $('#user-auth-section').show();
	    $('#user-auth-button').addClass('is-active');
	    $('#journal-auth-section').hide();
	    $('#journal-auth-button').removeClass('is-active');
	});
	$('#journal-auth-button').click(function(){
	    $('#ebook-section').hide();
	    $('#ebook-button').removeClass('is-active');
	    $('#journal-section').hide();
	    $('#journal-button').removeClass('is-active');
	    $('#blog-section').hide();
	    $('#blog-button').removeClass('is-active');
	    $('#user-auth-section').hide();
	    $('#user-auth-button').removeClass('is-active');
	    $('#journal-auth-section').show();
	    $('#journal-auth-button').addClass('is-active');
	});

	/*============= Admin Tab =============*/
	$('#journal-sec').hide();
	$('#journal-nav').hide();

	$('#ebook-btn').click(function(){
	    $('#ebook-sec').show();
	    $('#ebook-btn').addClass('is-active');
	    $('#ebook-nav').show();
	    $('#journal-sec').hide();
	    $('#journal-nav').hide();
	    $('#journal-btn').removeClass('is-active');
	});
	$('#journal-btn').click(function(){
	    $('#journal-sec').show();
	    $('#journal-btn').addClass('is-active');
	    $('#journal-nav').show();
	    $('#ebook-sec').hide();
	    $('#ebook-nav').hide();
	    $('#ebook-btn').removeClass('is-active');
	});

	/*============= Message Tab =============*/
	$('.delete').click(function(){
	    $('#suc-sec').hide();
	    $('#err-sec').hide();
	});

	/*============= E-Resources =============*/
	$('#nig-news-sec').hide();

	$('#nig-news-btn').hover(function(){
	    $('#nig-news-sec').show();
	    $('#nig-news-sec').hover(function(){
	        $('#nig-news-sec').show();
	    },
	    function(){
	        $('#nig-news-sec').show();
	    })
	},
	function(){
	    $('#nig-news-sec').hide();
	});
	/*============= Image Lazy Loading =============*/
	new LazyLoad({
	    elements_selector: ".lazy", // class to apply to
	    threshold: 300 // pixel threshold
	});
});
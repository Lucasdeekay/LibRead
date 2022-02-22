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
	$('#news-sec').hide();
	$('#nig-news-sec').hide();

	$('#news-btn').click(function(){
	    $('#news-sec').slideToggle();
	    $('#news-btn').toggleClass('is-yellow');
	});
	$('#nig-news-btn').click(function(){
	    $('#nig-news-sec').slideToggle();
	    $('#nig-news-btn').toggleClass('is-yellow');
	});

	$('#ebooks-sec').hide();

	$('#ebooks-btn').click(function(){
	    $('#ebooks-sec').slideToggle();
	    $('#ebooks-btn').toggleClass('is-yellow');
	});

	$('#ejournals-sec').hide();

	$('#ejournals-btn').click(function(){
	    $('#ejournals-sec').slideToggle();
	    $('#ejournals-btn').toggleClass('is-yellow');
	});

	$('#erefs-sec').hide();

	$('#erefs-btn').click(function(){
	    $('#erefs-sec').slideToggle();
	    $('#erefs-btn').toggleClass('is-yellow');
	});

	$('#res-sec').hide();

	$('#res-btn').click(function(){
	    $('#res-sec').slideToggle();
	    $('#res-btn').toggleClass('is-yellow');
	});

	$('#fd-sec').hide();

	$('#fd-btn').click(function(){
	    $('#fd-sec').slideToggle();
	    $('#fd-btn').toggleClass('is-yellow');
	});

	/*============= Image Lazy Loading =============*/
	new LazyLoad({
	    elements_selector: ".lazy", // class to apply to
	    threshold: 300 // pixel threshold
	});
});
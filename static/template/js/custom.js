$(window).load(function(){
			
		$('span.load').fadeTo(600,1);
		$('.fill').animate({width:'50%'},5000,function(){});
		$('.load').delay(5000).fadeOut(600);
				
				
			});
		$(document).ready( function() {
			$('#bg').blurjs({
				source: 'div.avatar-holder',
				radius: 30,
				overlay: 'rgba(0, 0, 0, .2)'
			});
			
			if ($(window).width() < 1000){
				$('div.post').css('float','none');
			}
			$('.navbar').on('mouseenter',function(){
				$(this).fadeTo(600,1);
				});
			
			$('.navbar').on('mouseleave',function(){
				$(this).fadeTo(600,0.6);
				});	
		});
		$('div.flows').load(function(){
				alert('loading');
			});
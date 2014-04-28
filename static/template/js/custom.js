$(window).load(function(){
			
		$('span.load').fadeTo(600,1);
		$('.fill').animate({width:'50%'},2000,function(){});
		$('.load').delay(2000).fadeOut(600);
				
				
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
			var show = 0;
			$('.slide').click(function(){
				
				if (show == 0){
				$('div.falow').animate({width:'25%'},600);
				$(this).animate({'right':'28%'},600,function(){ show = 1 ; });
				$('.slide span').removeClass('glyphicon-chevron-left');
				$('.slide span').addClass('glyphicon-chevron-right');
				}
				if (show == 1){
					$('div.falow').animate({width:'0%'},600);
					$(this).animate({'right':'2%'},600,function(){ show = 0 ; });
					$('.slide span').removeClass('glyphicon-chevron-right');
					$('.slide span').addClass('glyphicon-chevron-left');
				}
			$('#slide_cm').on('click',function(){$('div#cm').hide();});

			});
			var end = 5;
			$('#seemore').on('click',function(){
				end = end +5 ;
				});
		});
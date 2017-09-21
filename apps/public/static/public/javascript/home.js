$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();

    $(document).on('submit', '#login-form', function(e){
		e.preventDefault();

		$.ajax({
			type: 'POST',
			url: "/login",
			data: {
				password: $('#input').val(),
				here: $('#here').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(data){
				if (data.logged_in) {
					window.location.href = "/home_2";
				}
				else {
					$('#login_errors').html("<p>" + data.error.message + "</p>");
				}
			}
		})
	})
  });



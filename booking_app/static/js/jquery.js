setTimeout(function() {
	let messages = document.getElementById("msg");
	let alert = new bootstrap.Alert(messages);
	alert.close();
}, 3000);

var confirmBox = '<div class="modal fade confirm-modal">' +
	'<div class="modal-dialog modal-sm" role="document">' +
	'<div class="modal-content">' +
	'</button>' +
	'<div class="modal-body pb-5 modal-title"></div>' +
	'<div class="modal-footer pt-3 pb-3">' +
	'<a href="" class="btn btn-danger yesBtn btn-sm">Confirm</a>' +
	'<button type="button" class="btn btn-secondary abortBtn btn-sm" data-dismiss="modal">Cancel</button>' +
	'</div>' +
	'</div>' +
	'</div>' +
	'</div>';

var dialog = function(el, text, trueCallback, abortCallback) {

	el.click(function(e) {

		var thisConfirm = $(confirmBox).clone();

		thisConfirm.find('.modal-body').text(text);

		e.preventDefault();
		$('body').append(thisConfirm);
		$(thisConfirm).modal('show');

		if (abortCallback) {
			$(thisConfirm).find('.abortBtn').click(function(e) {
				e.preventDefault();
				abortCallback();
				$(thisConfirm).modal('hide');
			});
		}

		if (trueCallback) {
			$(thisConfirm).find('.yesBtn').click(function(e) {
				e.preventDefault();
				trueCallback();
				$(thisConfirm).modal('hide');
			});
		} else {

			if (el.prop('nodeName') == 'A') {
				$(thisConfirm).find('.yesBtn').attr('href', el.attr('href'));
			}

			if (el.attr('type') == 'submit') {
				$(thisConfirm).find('.yesBtn').click(function(e) {
					e.preventDefault();
					el.off().click();
				});
			}
		}

		$(thisConfirm).on('hidden.bs.modal', function(e) {
			$(this).remove();
		});

	});
}

$(function() {
	$('[data-confirm]').each(function() {
		dialog($(this), $(this).attr('data-confirm'));
	});

	dialog($('#customCallback'), "dialog with custom callback", function() {

		alert("hi there");

	});

});
$('form').submit(function (e) {
    var $form = $(this);
    var $modal = $form.closest('.modal');
    e.preventDefault();
    $.ajax({
        type: '{{ helper.form_method }}',
        url: '{{ helper.form_action }}',
        data: $form.serialize(),
        success: function (data, statusText, thrownError) {
            if ($(data).find('.has-error').length > 0) {
                $modal.find('.modal-body').html(data);
            } else {
                $modal.modal('toggle');
                alert(`Successfully submitted: ${data.email}`);
            }
        },
        error: function (data, statusText, thrownError) {
            $modal.modal('toggle');
            alert(`Email submission failed ${thrownError}`);
        }
    });
});

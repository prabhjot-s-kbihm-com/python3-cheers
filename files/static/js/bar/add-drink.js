 $('form.drink-form').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting via the browser
     var form = $('form').get(0);
     var formData = new FormData(form);
     formData.append('image', $('#image')[0].files[0]);
     $.blockUI({ message: 'Adding Drink...</h1>' });
    $.ajax({
      type: 'post',
      url: '/api/v0.1/bar/products/',
      data: formData,
      contentType: false,
      processData: false,
    }).done(function(data) {
      // Optionally alert the user of success here...
      $(".multiple-drinks ul").append('<li><img src = "'+data.image+'" alt = "image" ><div class ="custom-control custom-checkbox mt-5" > <input type = "checkbox" class ="custom-control-input" id="'+data.id+'" name="example1" ><label class ="custom-control-label" for ="'+data.id+'"> '+data.name+' </label></div></li>');
      $.unblockUI();

    }).fail(function(data) {
      alert("Something went wrong in your form data", data)
    });

  });
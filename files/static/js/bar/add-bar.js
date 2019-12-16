////////////// Autocomplete address
    function initAutocomplete() {
    // Create the autocomplete object, restricting the search predictions to
    // geographical location types.
    autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_addresss'), {types: ['geocode']});
    // address fields in the form.
    autocomplete.addListener('place_changed', fillInAddress);
    }

    function fillInAddress() {
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();
    var lat = place.geometry.location.lat();
    var lng = place.geometry.location.lng();
    $('#id_latitude').val(lat);
    $('#id_longitude').val(lng);
    }

    /////// open Model

    $('#id_address').focus(function(){
    //open bootsrap modal
    $('#myModal').modal({
    show: true
    });
    });


    ///////////Image Preview
    // Image Preview Function
    function readURLL(input) {

    if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
        $('#preview-background').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
    }
    }

    $("#bar_photography").change(function() {
    readURLL(this);
    });


    ////////  Google Adress Map


    function initialize() {
    var latlng = new google.maps.LatLng(13.756331,100.501762);
    var map = new google.maps.Map(document.getElementById('map'), {
    center: latlng,
    zoom: 13
    });
    var marker = new google.maps.Marker({
    map: map,
    position: latlng,
    draggable: true,
    anchorPoint: new google.maps.Point(0, -29)
    });
    var input = document.getElementById('id_address');
//    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    var geocoder = new google.maps.Geocoder();
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    var infowindow = new google.maps.InfoWindow();
    autocomplete.addListener('place_changed', function() {
    infowindow.close();
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    if (!place.geometry) {
        window.alert("Autocomplete's returned place contains no geometry");
        return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
    } else {
    map.setCenter(place.geometry.location);
    map.setZoom(17);
    }

    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

    bindDataToForm(place.formatted_address,place.geometry.location.lat(),place.geometry.location.lng());
    infowindow.setContent(place.formatted_address);
    infowindow.open(map, marker);

    });

    // this function will work on when click on map and set marker in that location.
    google.maps.event.addListener(map,"click",function (event) {
        placeMarker(event.latLng);
        geocoder.geocode({'latLng': marker.getPosition()}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
        if (results[0]) {
            bindDataToForm(results[0].formatted_address,marker.getPosition().lat(),marker.getPosition().lng());
            infowindow.setContent(results[0].formatted_address);
            infowindow.open(map, marker);
          }
        }
   });

   });

    //funtion used to update the marker position
     function placeMarker(location) {
            if (marker == undefined){
                marker = new google.maps.Marker({
                    position: location,
                    map: map,
                    animation: google.maps.Animation.DROP,
                });
            }
            else{
                marker.setPosition(location);
            }
            map.setCenter(location);

        }
    // this function will work on marker move event into map
    google.maps.event.addListener(marker, 'dragend', function() {
    geocoder.geocode({'latLng': marker.getPosition()}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
        if (results[0]) {
            bindDataToForm(results[0].formatted_address,marker.getPosition().lat(),marker.getPosition().lng());
            infowindow.setContent(results[0].formatted_address);
            infowindow.open(map, marker);
          }
        }
   });
});
    }
    function bindDataToForm(address,lat,lng){
        document.getElementById('id_address').value = address;
        document.getElementById('id_latitude').value = lat;
        document.getElementById('id_longitude').value = lng;
    }
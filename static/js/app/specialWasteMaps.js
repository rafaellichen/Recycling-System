function initMap () {
  var map;
  var locations = $('#specialWasteSite_meta').data('locations');
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: new google.maps.LatLng(locations[0].longitude, locations[0].latitude)
  });

  var infoWindow = new google.maps.InfoWindow();
  var marker; 
  for (var i = 0; i < locations.length; i++) {
    var latlong = new google.maps.LatLng(locations[i].longitude, locations[i].latitude);
    console.log(locations[i].latitude);
    marker = new google.maps.Marker({
      position: latlong,
      map: map,
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infoWindow.setContent('<p>' + locations[i].name + '</p>' + '<p>' + locations[i].hours + '</p>');
        infoWindow.open(map, marker);
      }
    })(marker, i));

  }
}
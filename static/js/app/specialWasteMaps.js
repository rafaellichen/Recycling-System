function initMap () {
  var map;
  var map2;
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
  
  var locations2 = $('#publicRecycleBins_meta').data('locations');

  var infoWindow2 = new google.maps.InfoWindow();
  var marker2; 

  map2 = new google.maps.Map(document.getElementById("map2"), {
    zoom: 15,
    center: new google.maps.LatLng(locations2[0].latitude, locations2[0].longitude)
  });

  for (var i = 0; i < locations2.length; i++) {
    var latlong2 = new google.maps.LatLng(locations2[i].latitude, locations2[i].longitude);
    console.log(locations2[i].latitude);
    marker2 = new google.maps.Marker({
      position: latlong2,
      map: map2,
    });

    google.maps.event.addListener(marker2, 'click', (function(marker2, i) {
      return function() {
        infoWindow2.setContent('<p>' + locations2[i].name + '</p>' + '<p>' + locations2[i].hours + '</p>');
        infoWindow2.open(map2, marker2);
      }
    })(marker2, i));
  }

  // Added a datatoggle event handler to resize both maps to avoid grey map error
  $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {                 
    google.maps.event.trigger(map, 'resize');
    google.maps.event.trigger(map2, 'resize');

  })
}
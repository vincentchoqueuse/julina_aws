var map;

function initialize() {
    var mapOptions = {
    center: new google.maps.LatLng({{object.gps_lat}},{{object.gps_long}}),
    zoom: 9,
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
    
    marker= new google.maps.Marker({position: new google.maps.LatLng({{object.gps_lat}},{{object.gps_long}}), map: map,title: '{{objet.nom}}'});

    
}



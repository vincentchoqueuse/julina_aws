var map;

function initialize() {
    var mapOptions = {
    center: new google.maps.LatLng(48.06665719999999,-1.6948267000000214),
    zoom: 6,
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
    
    {%for contrat in object_list %}
    contentString ='<div id="content"><h5>{{contrat.entreprise.nom}}</h5><p>Adresse: {{contrat.entreprise.adresse_rue}}, {{contrat.entreprise.adresse_zip}} {{contrat.entreprise.adresse_ville}}</p><p>Etudiant: {{contrat.affectation.etudiant}}</p><p>Tuteur Formation: {{contrat.tuteur_formation}}</p></div>';
    
    infowindow_1_{{forloop.counter0}} = new google.maps.InfoWindow({content: contentString});
    
    type="{{contrat.type}}";
    switch (type) {
        case "CP":
            icon_marker = "http://maps.google.com/mapfiles/ms/icons/red-dot.png";
            break;
        case "CA":
            icon_marker = "http://maps.google.com/mapfiles/ms/icons/green-dot.png";
            break;
        case "S":
            icon_marker = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png";
            break;
        case "Autre":
            icon_marker = "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png";
            break;
    }
    
    marker_1_{{forloop.counter0}} = new google.maps.Marker({position: new google.maps.LatLng({{contrat.entreprise.gps_lat}},{{contrat.entreprise.gps_long}}), map: map,title: '{{contrat.entreprise.nom}}',  icon: icon_marker});

    
    google.maps.event.addListener(marker_1_{{forloop.counter0}}, 'click', function() {infowindow_1_{{forloop.counter0}}.open(map,marker_1_{{forloop.counter0}});});
    {% endfor %}
    
}

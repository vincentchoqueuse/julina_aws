var map;

function initialize() {
    var mapOptions = {
    center: new google.maps.LatLng(48.06665719999999,-1.6948267000000214),
    zoom: 6,
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
    
    {%for entreprise in object_list.all %}
    contentString ='<div id="content"><h5>{{entreprise.nom}}</h5><p>Adresse: {{entreprise.adresse_rue}}, {{entreprise.adresse_zip}} {{entreprise.adresse_ville}}</p></div><h6>Contrats</h6><ul>';
    
        {% for contrat in entreprise.contrat_set.all %}
            contentString=contentString+"<li>Etudiant: {{contrat.affectation.etudiant}} ({{contrat.affectation.promotion}}) / Tuteur Formation: {{contrat.tuteur_formation}}</li>";
    
        {% endfor %}
    
    contentString=contentString+"</ul>";
    
    infowindow_1_{{forloop.counter0}} = new google.maps.InfoWindow({content: contentString});

    marker_1_{{forloop.counter0}} = new google.maps.Marker({position: new google.maps.LatLng({{entreprise.gps_lat}},{{entreprise.gps_long}}), map: map,title: '{{entreprise.nom}}'});

    
    google.maps.event.addListener(marker_1_{{forloop.counter0}}, 'click', function() {infowindow_1_{{forloop.counter0}}.open(map,marker_1_{{forloop.counter0}});});
    {% endfor %}
    
}

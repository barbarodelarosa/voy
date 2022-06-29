// Hacer Seguimiento 


var map_init = L.map('map').
setView([41.66, -4.72],
15);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© ArteCriollo'
}).addTo(map_init);

L.control.scale().addTo(map_init);

if (!navigator.geolocation) {
    console.log("Su navegador no soporta geolocalización!");
  } else {
    navigator.geolocation.getCurrentPosition(getPosition);
  }





  var marker, circle, lat, long, accuracy;

  function getPosition(position) {
    // console.log(position)
    lat = position.coords.latitude;
    long = position.coords.longitude;
    accuracy = position.coords.accuracy;
  
    if (marker) {
        map_init.removeLayer(marker);
    }
  
    if (circle) {
        map_init.removeLayer(circle);
    }
  
    marker = L.marker([lat, long]);
    circle = L.circle([lat, long], { radius: accuracy });
  
    var featureGroup = L.featureGroup([marker, circle]).addTo(map_init);
  
    map_init.fitBounds(featureGroup.getBounds());
  
    console.log(
      "Su coordenada es: Lat: " +
        lat +
        " Long: " +
        long +
        " Accuracy: " +
        accuracy
    );
  }


// L.Control.geocoder().addTo(map_init);

if (!navigator.geolocation) {
    console.log("Su navegador no soporta geolocalización!");
  } else {
    setInterval(() => {
      navigator.geolocation.getCurrentPosition(getPosition);
    }, 5000);
  }
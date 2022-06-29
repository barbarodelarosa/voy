var browserLat = 23.13302;
var browserLong = -82.38304;  


var map_init = L.map('seguimiento_map', {
    center: [browserLat, browserLong],
    zoom: 10
});


var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© Voy Express'
}).addTo(map_init);
L.Control.geocoder().addTo(map_init);



if (!navigator.geolocation) {
    alert("Su navegador no acepta gelocalizacion");
} else {
    setInterval(() => {
        navigator.geolocation.getCurrentPosition(getPosition);
        // routeControl
      }, 5000);
}


var marker, circle, lat, long, accuracy;

function getPosition(position) {
  console.log(position.coords.accuracy)
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
    "Your coordinate is: Lat: " +
      lat +
      " Long: " +
      long +
      " Accuracy: " +
      accuracy
  );
}







// // /*****************OBTENER DISTANCIA DEL RECORRIDO********** */


// var routeControl = L.Routing.control({
//     show: false,
//     collapsible:true,
//     lineOptions: {
//         styles: [
//             {color: 'white', opacity: 0.9, weight: 9},
//             {color: '#FC8428', opacity: 1, weight: 3}
//         ]
//         },
//   waypoints: [
//     L.latLng(browserLat , browserLong),
//     L.latLng(browserLat +0.5, browserLong+0.2 )

//   ],
//   router: L.Routing.mapbox('pk.eyJ1IjoiYXJ0ZWNyaW9sbG8iLCJhIjoiY2wzd2gyZHZyMDI1ZjNjbXkzNmduNmdydiJ9.eJ7_JqzaIEHZ4rGFBA0Ung',{language: 'es'}),
//   language:'es',
//   geocoder: L.Control.Geocoder.nominatim(),
// }).addTo(map_init);








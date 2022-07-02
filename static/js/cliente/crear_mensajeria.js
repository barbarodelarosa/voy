var browserLat = 23.13302;
var browserLong = -82.38304;  
var map = L.map('map');


navigator.geolocation.getCurrentPosition(function(position) {
    browserLat =  position.coords.latitude;
    browserLong = position.coords.longitude;

 
    marker_actual = L.marker([browserLat,browserLong]).addTo(map);
   
    map.setView([browserLat,browserLong], 15);  
  
    
    console.log(browserLat);
    console.log(browserLong);
}, function(err) {
    console.error(err);
    //AUI SI DA ERROR ES PORQUE NO SE HA ENCONTRADO POSICIAN Y DEBE SOLICARLE UN POSICIAN AL USUARIO
    alert('No es se encuantra su localización, por favor active su GPS');
});


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© Voy Express'
}).addTo(map);

L.control.scale().addTo(map);


// /*****************OBTENER DISTANCIA DEL RECORRIDO********** */


var routeControl = L.Routing.control({
    show: false,
    collapsible:true,
    lineOptions: {
        styles: [
            {color: 'white', opacity: 0.9, weight: 9},
            {color: '#FC8428', opacity: 1, weight: 3}
        ]
        },
  waypoints: [
    L.latLng(),
    // L.latLng(browserLat, browserLong)
    L.latLng()
  ],
  router: L.Routing.mapbox('pk.eyJ1IjoiYXJ0ZWNyaW9sbG8iLCJhIjoiY2wzd2gyZHZyMDI1ZjNjbXkzNmduNmdydiJ9.eJ7_JqzaIEHZ4rGFBA0Ung',{language: 'es'}),
  language:'es',
  geocoder: L.Control.Geocoder.nominatim()
}).addTo(map);


calculoRuta = routeControl.on('routesfound', function(e) {
    var routes = e.routes;
    var summary = routes[0].summary;
    routeArray = routeControl.getWaypoints();
    // alert('Total distance is ' + summary.totalDistance / 1000 + ' km and total time is ' + Math.round(summary.totalTime % 3600 / 60) + ' minutes');
  });






// // FUNCION PARA MARCAR EL ORIGEN Y DESTINO
// // Se crea el boton
function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.setAttribute('class', 'btn btn-primary');
    btn.innerHTML = label;
    
    return btn;
}

// Se ejecuta el boton
map.on('click', function(e) {


    var container = L.DomUtil.create('div'),
        startBtn = createButton('Marcar origen', container),
        destBtn = createButton('Marcar destino', container);

    L.popup()
        .setContent(container)
        .setLatLng(e.latlng)
        .openOn(map);

        L.DomEvent.on(startBtn, 'click', function() {
            routeControl.spliceWaypoints(0, 1, e.latlng);
            map.closePopup();
            idLatLngOrigen( e.latlng)
        });
        
        
        L.DomEvent.on(destBtn, 'click', function() {
            routeControl.spliceWaypoints(routeControl.getWaypoints().length - 1, 1, e.latlng);
            map.closePopup();
            idLatLngDestino(e.latlng)
        });

});


//CALCULAR RUTA
calculoRuta = routeControl.on('routesfound', function(e) {
    var routes = e.routes;
    var summary = routes[0].summary;
    routeArray = routeControl.getWaypoints();
    km_distancia = summary.totalDistance / 1000 
    tarifa = 20.00
    precio_parcial = tarifa * km_distancia
    precio_total = Math.round(precio_parcial * 100) / 100
    km_distancia = Math.round(km_distancia * 100) / 100
    $('#id_distancia').val(km_distancia)
    $('#id_tarifa').val(tarifa)
    $('#id_precio').val(precio_total)
    $('#id_direccion_origen_map').val(routes[0].name)
    $('#id_direccion_destino_map').val(routes[1].name)

    // alert('La distancia es ' +  km_distancia  + ' km aproximadamente para una tarifa de ' + precio_total + ' CUP');
    // alert('La distancia es ' +  km_distancia  + ' km and total time is ' + Math.round(summary.totalTime % 3600 / 60) + ' minutes');
  });

// 5 km/h como promedio caminando
// 15-20 km/h como promedio bicicleta
// puede que 30-40 km/h como promedio carro o moto




// Agrega Latitud y Longitud al formulario
function idLatLngOrigen(origen){
    $('#id_latitud_origen').val(origen.lat)
    $('#id_longitud_origen').val(origen.lng)
}
function idLatLngDestino(destino){
    $('#id_latitud_destino').val(destino.lat)
    $('#id_longitud_destino').val(destino.lng)
}

// $( function() {
//     $( "#id_hora_recogida" ).datetimepicker();
//   } );
// $( function() {
//     $( "#id_hora_entrega" ).datepicker();
//   } );

//   $(function () {  
//     $("#id_hora_recogida").datetimepicker({  
//         // format: 'd/m/Y',  
//         format: 'MM/dd/yy H:mm',  
//         timepicker:false  
//     });  
//    });  
// if (!navigator.geolocation) {
//     console.log("Su navegador no soporta geolocalización!");
//   } else {
//     navigator.geolocation.getCurrentPosition(getPosition);
//   }



//   var marker, circle, lat, long, accuracy;

//   function getPosition(position) {
//     lat = position.coords.latitude;
//     long = position.coords.longitude;
//     accuracy = position.coords.accuracy;
  
//     if (marker) {
//         map_init.removeLayer(marker);
//     }
  
//     if (circle) {
//         map_init.removeLayer(circle);
//     }
  
//     marker = L.marker([lat, long]);
//     circle = L.circle([lat, long], { radius: accuracy });
  
//     var featureGroup = L.featureGroup([marker, circle]).addTo(map_init);
  
//     map_init.fitBounds(featureGroup.getBounds());
//   }



// // Centrar mapa
// map.locate({setView: true, maxZoom: 16});

// function onLocationFound(e) {
//  var radius = e.accuracy / 3;

// L.marker(e.latlng,{draggable: true}).addTo(map)
// //  .bindPopup("Tu estas aqui, con " + radius + " metros de aproximacion").openPopup();

// L.circle(e.latlng, radius).addTo(map);
//  }
//  function onLocationError(e) {
// //  alert(e.message);
//  alert("No fue posible obtener su localizacion");
// }
//  map.on('locationfound', onLocationFound);
//  map.on('locationerror', onLocationError);



// console.log(getPosition())







// /*****************OBTENER DISTANCIA DEL RECORRIDO********** */


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
//     L.latLng(57.74, 11.94),
//     L.latLng(57.6792, 11.949)
//   ],
//   router: L.Routing.mapbox('pk.eyJ1IjoiYXJ0ZWNyaW9sbG8iLCJhIjoiY2wzd2gyZHZyMDI1ZjNjbXkzNmduNmdydiJ9.eJ7_JqzaIEHZ4rGFBA0Ung',{language: 'es'}),
//   language:'es',
//   geocoder: L.Control.Geocoder.nominatim()
// }).addTo(map);


// calculoRuta = routeControl.on('routesfound', function(e) {
//     var routes = e.routes;
//     var summary = routes[0].summary;
//     routeArray = routeControl.getWaypoints();
//     // alert('Total distance is ' + summary.totalDistance / 1000 + ' km and total time is ' + Math.round(summary.totalTime % 3600 / 60) + ' minutes');
//   });



// // FUNCION PARA MARCAR EL ORIGEN Y DESTINO
// // Se crea el boton
// function createButton(label, container) {
//     var btn = L.DomUtil.create('button', '', container);
//     btn.setAttribute('type', 'button');
//     btn.setAttribute('class', 'btn btn-primary');
//     btn.innerHTML = label;
    
//     return btn;
// }

// // Se ejecuta el boton
// map.on('click', function(e) {


//     var container = L.DomUtil.create('div'),
//         startBtn = createButton('Marcar origen', container),
//         destBtn = createButton('Marcar destino', container);

//     L.popup()
//         .setContent(container)
//         .setLatLng(e.latlng)
//         .openOn(map);

//         L.DomEvent.on(startBtn, 'click', function() {
//             routeControl.spliceWaypoints(0, 1, e.latlng);
//             map.closePopup();
//         });
        
        
//         L.DomEvent.on(destBtn, 'click', function() {
//             routeControl.spliceWaypoints(routeControl.getWaypoints().length - 1, 1, e.latlng);
//             map.closePopup();
//         });

// });











// // var track_map = L.map('map', {
// //     center: [9.0820, 8.6753],
// //     zoom: 8
// // });
// // var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
// //     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// // }).addTo(track_map);
// // L.Control.geocoder().addTo(track_map);



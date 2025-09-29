var map = L.map('map').setView([-34.6037, -58.3816], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OSM</a> contributors'
}).addTo(map);

var ruta1 = L.Routing.control({
  waypoints: [
    L.latLng(-37.340178071091856, -59.13643712952644),
    L.latLng(-37.25598097698842, -58.57359980199977)  
  ],
  routeWhileDragging: false,
  language: 'es',
  lineOptions: { styles: [{ color: 'blue', opacity: 0.7, weight: 5 }] },
  createMarker: function() { return null; }
});
var inicio = L.marker([-37.340178071091856, -59.13643712952644]).bindPopup("Inicio").addTo(map);
var llegada = L.marker([-37.25598097698842, -58.57359980199977]).bindPopup("Llegada").addTo(map);

var hidratacion1 = L.marker([-37.330, -59.000]).bindPopup("Hidratación 1").addTo(map);
var hidratacion2 = L.marker([-37.320, -58.900]).bindPopup("Hidratación 2").addTo(map);
var hidratacion3 = L.marker([-37.300, -58.800]).bindPopup("Hidratación 3").addTo(map);
var hidratacion4 = L.marker([-37.280, -58.700]).bindPopup("Hidratación 4").addTo(map);

ruta1.addTo(map);

var ruta2 = L.Routing.control({
  waypoints: [
    L.latLng(-37.340178071091856,-59.13643712952644), 
    
    L.latLng(-37.36070535090289, -59.01624220295415)  
  ],
  routeWhileDragging: false,
  language: 'es',
  lineOptions: { styles: [{ color: 'red', opacity: 0.8, weight: 5, dashArray: '6, 6' }] },
  createMarker: function() { return null; }
});


var rutasActivas = {
  1: false,
  2: false
};


function toggleRuta(num) {
  if (num === 1) {
    if (rutasActivas[1]) {
      map.removeControl(ruta1);
      rutasActivas[1] = false;
    } else {
      ruta1.addTo(map);
      rutasActivas[1] = true;
    }
  } else if (num === 2) {
    if (rutasActivas[2]) {
      map.removeControl(ruta2);
      rutasActivas[2] = false;
    } else {
      ruta2.addTo(map);
      rutasActivas[2] = true;
    }
  }
}

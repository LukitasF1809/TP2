var map = L.map('map').setView([-37.33447788835374, -58.803580360176994], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OSM</a> contributors'
}).addTo(map);

var ruta1 = L.Routing.control({
  waypoints: [
    L.latLng(-37.340178071091856, -59.13643712952644),
    L.latLng(-37.25523348138248, -58.56075909634787)  
  ],
  routeWhileDragging: false,
  language: 'es',
  lineOptions: { styles: [{ color: 'blue', opacity: 0.7, weight: 5 }] },
  createMarker: function() { return null; }
});


var marcadoresRuta1 = L.layerGroup([
    L.marker([-37.36751805679175, -59.02781534980269]).bindPopup("Primer punto de hidratación").addTo(map),
    L.marker([-37.35578118363171, -58.872450500152425]).bindPopup("Segundo punto de hidratación 2").addTo(map),
    L.marker([-37.30609668601033, -58.71761193753619]).bindPopup("Tercer punto de hidratación 3").addTo(map),
    L.marker([-37.340178071091856, -59.13643712952644]).bindPopup("Inicio").addTo(map),
    L.marker([-37.25523348138248, -58.56075909634787]).bindPopup("Llegada").addTo(map),
]);

ruta1.addTo(map);
var marcadoresRuta2 = L.layerGroup([
  L.marker([-37.36751805679175, -59.02781534980269]).bindPopup("Primer punto de hidratación").addTo(map), 
  L.marker([-37.340178071091856, -59.13643712952644]).bindPopup("Inicio").addTo(map),
  L.marker([-37.35578118363171, -58.872450500152425]).bindPopup("Llegada").addTo(map),

]);
var ruta2 = L.Routing.control({
  waypoints: [
    L.latLng(-37.340178071091856,-59.13643712952644), 
    L.latLng(-37.3567393596012, -58.872805112371836),  
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
      map.removeLayer(marcadoresRuta1);
      rutasActivas[1] = false;
    } else {
      ruta1.addTo(map);
      marcadoresRuta1.addTo(map);
      rutasActivas[1] = true;
    }
  } else if (num === 2) {
    if (rutasActivas[2]) {
      map.removeControl(ruta2);
      map.removeLayer(marcadoresRuta2);
      rutasActivas[2] = false;
    } else {
      ruta2.addTo(map);
      marcadoresRuta2.addTo(map);
      rutasActivas[2] = true;
    }
  }
}

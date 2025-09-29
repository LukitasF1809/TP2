// Inicializar mapa
var map = L.map('map').setView([-34.6037, -58.3816], 13);

// Tiles de OSM
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OSM</a> contributors'
}).addTo(map);

// === Definir las rutas sin agregarlas de entrada ===
var ruta1 = L.Routing.control({
  waypoints: [
    L.latLng(-37.340178071091856, -59.13643712952644),
    L.latLng(-37.25598097698842, -58.57359980199977)  
  ],
  routeWhileDragging: true,
  language: 'es',
  lineOptions: { styles: [{ color: 'blue', opacity: 0.7, weight: 5 }] },
  createMarker: function() { return null; }
});

ruta1.addTo(map);

var ruta2 = L.Routing.control({
  waypoints: [
    L.latLng(-34.5675, -58.4116), // Planetario
    L.latLng(-34.5714, -58.4222), // Parque Tres de Febrero
    L.latLng(-34.5453, -58.4490)  // Monumental
  ],
  routeWhileDragging: true,
  language: 'es',
  lineOptions: { styles: [{ color: 'red', opacity: 0.8, weight: 5, dashArray: '6, 6' }] },
  createMarker: function() { return null; }
});

// Estado de las rutas
var rutasActivas = {
  1: false,
  2: false
};

// Función para mostrar/ocultar rutas
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

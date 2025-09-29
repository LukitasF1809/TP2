// Inicializar el mapa en Buenos Aires (Obelisco aprox.)
var map = L.map('map').setView([-34.6037, -58.3816], 15);

// Cargar tiles de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Recorrido 1 (rojo) – circuito pequeño alrededor del Obelisco
var recorrido1 = [
  [-34.6037, -58.3816], // Obelisco
  [-34.6045, -58.3800], // hacia el Este
  [-34.6060, -58.3810], // hacia el Sur
  [-34.6050, -58.3830], // hacia el Oeste
  [-34.6037, -58.3816]  // volver al Obelisco
];

// Recorrido 2 (azul) – circuito más amplio
var recorrido2 = [
  [-34.6037, -58.3816], // Obelisco
  [-34.6015, -58.3785], // Plaza Lavalle
  [-34.6040, -58.3760], // Av. Córdoba
  [-34.6065, -58.3790], // Retiro
  [-34.6050, -58.3830], // regreso
  [-34.6037, -58.3816]  // Obelisco
];

// Dibujar recorrido 1
var polyline1 = L.polyline(recorrido1, {
  color: 'red',
  weight: 5
}).addTo(map);

// Dibujar recorrido 2
var polyline2 = L.polyline(recorrido2, {
  color: 'blue',
  weight: 4,
  dashArray: '6, 6' // punteado
}).addTo(map);

// Agrupar y ajustar vista
var group = L.featureGroup([polyline1, polyline2]);
map.fitBounds(group.getBounds());

// Marcadores de inicio/fin
L.marker(recorrido1[0]).addTo(map).bindPopup("Inicio/Fin Recorrido 1");
L.marker(recorrido2[0]).addTo(map).bindPopup("Inicio/Fin Recorrido 2");
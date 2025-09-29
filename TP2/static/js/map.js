
// Inicializar mapa centrado en Tandil (o donde quieras)
var map = L.map('map').setView([-37.326811908156536, -59.1145229079095], 13);

// Capa de tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Definís puntos del recorrido (waypoints)
// fíjate que los puntos intermedios pueden indicar el camino que querés que siga

var ruta1 = L.Routing.control({
waypoints : [
  L.latLng(-37.326811908156536, -59.1145229079095),   // inicio
  L.latLng(-37.31923558883404, -59.10499570199474),   // punto intermedio
  L.latLng(-37.31215342851336, -59.11415812753187),   // otro punto
  L.latLng(-37.314662125446276, -59.117516253013164)    // fin

],
routeWhileDragging : true, 
language : 'es',
lineOptions : {styles:[{color : 'blue' , opacity: 0.7}]},
createMarker : function (){return null;}
}).addTo(map) ;

// Crear el control de enrutamiento
var control = L.Routing.control({
  waypoints: waypoints,
  routeWhileDragging: false,  // opcional: si permitís que el usuario arrastre puntos
  showAlternatives: false,    // mostrar rutas alternativas, si el motor lo permite
  draggableWaypoints: true,
  addWaypoints: false,        // evita que el usuario agregue puntos extras al hacer clic
  fitSelectedRoute: true,
  lineOptions: {
    styles: [
      {color: 'red', weight: 5}
    ]
  }
}).addTo(map);

// (Opcional) para extraer la ruta en forma de polyline o coordenadas
control.on('routesfound', function(e) {
  var routes = e.routes;
  var summary = routes[0].summary;
  console.log("Distancia (m): " + summary.totalDistance);
  console.log("Tiempo (seg): " + summary.totalTime);

  // Si querés, podés extraer el array de latlngs de la ruta:
  var routeLatLngs = routes[0].coordinates;
  // Por ejemplo, podés agregar marcadores a cada extremo:
  L.marker(routeLatLngs[0]).addTo(map).bindPopup("Inicio").openPopup();
  L.marker(routeLatLngs[routeLatLngs.length - 1]).addTo(map).bindPopup("Fin");
});
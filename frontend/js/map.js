"use strict";

// Setting map bounds (limits)
const southWest = L.latLng(35, -22);
const northEast = L.latLng(68.16, 41);
const maxBoundArea = L.latLngBounds(southWest, northEast);

// Declaring map variable.
const map = L.map('map', {tap: false, zoomControl: false, maxBounds: maxBoundArea});

// Setting icon variables
const grayIcon = L.divIcon({className: "gray-icon"})
const greenIcon = L.divIcon({className: "green-icon"})
const blueIcon = L.divIcon({className: "blue-icon"})
const yellowIcon = L.divIcon({className: "yellow-icon"})
const misterXIcon = L.divIcon({className: "misterX-icon"})


// Adding layer to the map. With minZoom and maxZoom
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
    minZoom: 3.5,
    maxZoom: 6,
}).addTo(map);


// Setting starting view and zoom.
map.setView([48.88216501257649, 19.006699861864657], 4);


// Creating group of markers.
let markerGroup = L.layerGroup().addTo(map)
let misterXGroup = L.layerGroup().addTo(map)












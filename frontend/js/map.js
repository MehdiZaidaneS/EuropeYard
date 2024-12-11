"use strict";

const southWest = L.latLng(35, -22);
const northEast = L.latLng(68.16, 41);
const maxBoundArea = L.latLngBounds(southWest, northEast);

const map = L.map('map', {tap: false, zoomControl: false, maxBounds: maxBoundArea});

const grayIcon = L.divIcon({className: "gray-icon"})
const greenIcon = L.divIcon({className: "green-icon"})
const blueIcon = L.divIcon({className: "blue-icon"})
const yellowIcon = L.divIcon({className: "yellow-icon"})
const misterXIcon = L.divIcon({className: "misterX-icon"})

L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
    minZoom: 3.5,
    maxZoom: 6,
}).addTo(map);

map.setView([48.88216501257649, 19.006699861864657], 4);

let markerGroup = L.layerGroup().addTo(map)
let misterXGroup = L.layerGroup().addTo(map)












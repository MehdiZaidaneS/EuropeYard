"use strict";

// Setting map bounds (limits)
const southWest = L.latLng(35, -22);
const northEast = L.latLng(68.16, 41);
const maxBoundArea = L.latLngBounds(southWest, northEast);

// Declaring map variable.
const map = L.map('map', {tap: false, zoomControl: false, maxBounds: maxBoundArea});

// Setting icon variables

const misterXIcon = L.icon({
    iconUrl: 'img/logo.png',
    iconSize:     [25, 25], // size of the icon

});

const greenIcon = L.icon({
    iconUrl: 'img/busIcon.png',
    iconSize:     [20, 20], // size of the icon
});

const blueIcon = L.icon({
    iconUrl: 'img/boatIcon.png',
    iconSize:     [20, 20], // size of the icon
});

const yellowIcon = L.icon({
    iconUrl: 'img/planeIcon.png',
    iconSize:     [20, 20], // size of the icon
});



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
















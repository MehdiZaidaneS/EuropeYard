"use strict"

let playerLocation = ""
let busTickets = 10;
let boatTickets = 5;
let planeTickets = 1;
let gameOn = true;


// Set starter location for the player.
async function getLocation() {
    const response = await apiCall("getcountry", "")// Fetches the result from the api call to "get country" endpoint.

    // update my location text
    updatePlayerLocationText(response["country"])
    // Update my current marker.
    await updatePlayerLocationMarker(response["country"])

    createDialog("Your random location was " + playerLocation + ". Uff a bit far away from me.");


}

// Updates player location text in HTML.
function updatePlayerLocationText(location) {
    const span = document.querySelector("#mylocation")
    span.innerHTML = location
}

// Update player marker on the map. (Russia and Ireland gives wrong lat and lon, so I set them manually)
async function updatePlayerLocationMarker(location) {
    playerLocation = location
    if (playerLocation === "Russia") {
        L.marker([54.96, 35.47]).addTo(markerGroup).bindPopup(`You are currently in ${playerLocation}.`);
    } else if (playerLocation === "Ireland") {
        L.marker([53.58, -8.11]).addTo(markerGroup).bindPopup(`You are currently in ${playerLocation}.`);
    } else {
        const url = `https://restcountries.com/v3.1/name/${playerLocation}` //API to get countries LAT and LONG
        try {
            const response = await fetch(url);
            const json_data = await response.json();
            const latlng = json_data[0]["latlng"] //Saves the lat and long fetched.
            L.marker(latlng).addTo(markerGroup).bindPopup(`You are currently in ${playerLocation}.`); //Added marker in the location.
        } catch (error) {
            console.log("error.message")
        }

    }
}

// Function that checks if player is in same position as MisterX. In case of that WIN.
function playerPosition(location) {
    if (location === misterLocation) {
        const h1 = document.querySelector("#victory")
        misterXGroup.clearLayers()
        h1.innerHTML = "Victoria!"
        createDialog("Damn it! You got me this time... Next time will be different.")
        gameOn = false
        return true
    } else {
        //Game continues
        randomMove() //Mister X moves always after player moves.
        console.log("You didnt catch Mister X this time.")
    }
}

// IMPORTANT function of movement of player.
function moveTo(vehicleTicket, vehicle, destination) {
    if (vehicleTicket > 0) {
        roundCounter = roundCounter + 1; //Counts the round player played.
        markerGroup.clearLayers() // Clear all the marks on the map.
        updateTickets(vehicle) //Updates the tickets according to the vehicle using.
        updatePlayerLocationMarker(destination) //Updates the location marker of the player
        updatePlayerLocationText(destination) //Updates the text of the location of the player.
        //createPlayerMovementCard(vehicle)
        playerPosition(destination) // Checks if player found MisterX

    } else {
        createDialog("Don't you see? You don't have enough " + vehicle + " tickets HAHA") //You cant move, if you don't have enough tickets
    }
}

//Checks what vehicle is updating. And then takes one ticket away and updates the text of tickets left.
function updateTickets(vehicle) {
    if (vehicle === "Bus") {
        busTickets -= 1;
        const span = document.querySelector("#busTickets")
        span.innerHTML = busTickets
    } else if (vehicle === "Boat") {
        boatTickets -= 1;
        const span = document.querySelector("#boatTickets")
        span.innerHTML = boatTickets
    } else {
        planeTickets -= 1;
        const span = document.querySelector("#planeTickets")
        span.innerHTML = planeTickets
    }
}

//Mark all the possible destinations on the map.
async function markPossibleDestinations(destinations, icon, vehicleTicket, vehicle) {
    for (let destination of destinations) {
        if (destination === "Russia") {
            L.marker([54.96, 35.47]).addTo(markerGroup).setIcon(icon).on("click", function (e) {
                createRandomMsg()
                moveTo(vehicleTicket, vehicle, destination) //When the marker it is clicked
            })
        } else if (destination === "Ireland") {
            L.marker([53.58, -8.11]).addTo(markerGroup).setIcon(icon).on("click", function (e) {
                createRandomMsg()
                moveTo(vehicleTicket, vehicle, destination)
            })
        } else {
            const url = `https://restcountries.com/v3.1/name/${destination}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(markerGroup).setIcon(icon).on("click", function (e) {
                    createRandomMsg()
                    moveTo(vehicleTicket, vehicle, destination)
                })
            } catch (error) {
                console.log("error.message")
            }
        }
    }
}


// Player bus movement function
async function busDestinations(location) {
    const response = await apiCall("busdestinations", location)
    if (response.length > 0) {
        await markPossibleDestinations(response, greenIcon, busTickets, "Bus")
    } else {
        createDialog("You can't travel with bus from " + location)
    }

}

// Player boat movement function.
async function boatDestinations(location) {
    const response = await apiCall("boatdestinations", location)
    if (response.length > 0) {
        await markPossibleDestinations(response, blueIcon, boatTickets, "Boat")
    } else {
        createDialog("There is no sea you can sail on, brother!");
    }

}

// Player plane movement function
async function planeDestinations(location) {
    const response = await apiCall("planedestinations", location)
    await markPossibleDestinations(response, yellowIcon, planeTickets, "Plane")


}


// Chat dialog maker

function createDialog(message) {

    const chat = document.querySelector(".chat")
    const div = document.createElement("div")
    const p = document.createElement("p")
    const img = document.createElement("img")
    img.src = "img/logo.png"
    img.width = 30
    img.height = 30
    img.alt = ""
    img.style.marginLeft = "7px";
    p.innerHTML = message

    div.appendChild(img)
    div.appendChild(p)

    chat.appendChild(div)

    chat.scrollTop = chat.scrollHeight;

}


function createRandomMsg() {

    const randomMsg = Math.floor(Math.random() * 8)
    const randomInt = Math.floor(Math.random() * 20)

    if (randomInt === 3) {
        fetch('testdata/datatest.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => createDialog(data["messages"][randomMsg]["msg"]))
            .catch(error => console.error('Failed to fetch data:', error));

    }
}


const buttons = document.getElementsByClassName("vehicle")
for (let button of buttons) {
    button.addEventListener("click", function (evt) {
        evt.preventDefault();
        const h1 = button.querySelector(".text")
        if (gameOn) {
            if (h1.innerHTML === "Bus") {
                console.log("i pressed bus")
                busDestinations(playerLocation)
            } else if (h1.innerHTML === "Boat") {
                console.log("i pressed boat")
                boatDestinations(playerLocation)
            } else {
                console.log("i pressed plane")
                planeDestinations(playerLocation)
            }
        } else {
            console.log("You won baaaabyyy")
        }


    })
}


const startButton = document.getElementById("start-game")
const misterXBoard = document.querySelector(".misterX-board")
const playerBoard = document.querySelector(".player-board");
const startButtons = document.getElementById("start-buttons")
const movementButtons = document.getElementById("movement-buttons")
const controllerH1 = document.getElementById("controller-h1");

startButton.addEventListener("click", function (evt) {
    evt.preventDefault()
    misterXBoard.style.display = "block";
    playerBoard.style.display = "block";
    movementButtons.style.display = "block";
    startButtons.style.display = "none";
    controllerH1.innerHTML = "What is your next move?";
    start()
})


// Starting function
async function start() {
    await getLocation()
    await getMisterXLocation()
}



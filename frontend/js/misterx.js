"use strict";

let misterLocation = ""
let roundCounter = 0


//Gets a country from the API and set it as Mister X Location
async function getMisterXLocation() {
    const countries = await apiCall("getallcountries", "")
    countries.splice(countries.indexOf(playerLocation), 1)
    misterLocation = randomlyChooseCountry(countries)
    console.log("MisterX was spawned in " + misterLocation)

}

// Mister X bus method.
async function mxBusDestinations(location) {
    const destinations = await apiCall("busdestinations", location) //Getting all destinations

    if (destinations.includes(playerLocation)) {
        destinations.splice(destinations.indexOf(playerLocation), 1) //Removing player location as destination
    }

    if (checkVehicleUsability(destinations)) {
        misterLocation = randomlyChooseCountry(destinations)  //Choosing one random country from all the destinations
        console.log("Now he is in " + misterLocation)
        createMisterXMovementCard("Bus")
    } else {
        console.log("He couldn't use bus so he used boat")
        await mxBoatDestinations(misterLocation) //In case of not being able to use bus, uses boat.
    }
}


// Mister X boat method.
async function mxBoatDestinations(location) {
    const destinations = await apiCall("boatdestinations", location) //Getting all possible destinations from current location.

    if (destinations.includes(playerLocation)) {
        destinations.splice(destinations.indexOf(playerLocation), 1) //Removing player location as destination
    }

    if (checkVehicleUsability(destinations)) {
        misterLocation = randomlyChooseCountry(destinations)  //Choosing one random country from all the destinations
        console.log("Now he is in " + misterLocation)
        createMisterXMovementCard("Boat")
    } else {
        console.log("He couldn't use boat so he used bus")
        await mxBusDestinations(misterLocation) // In case not being able to use boat, uses bus.
    }
}

// Mister X flying method.
async function mxPlaneDestinations(location) {
    const destinations = await apiCall("planedestinations", location) //Getting all destinations
    destinations.splice(destinations.indexOf(playerLocation), 1) //Removing player location as destination
    misterLocation = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
    console.log("Now he is in " + misterLocation)
    createMisterXMovementCard("Plane")
}


//Function that updates every 3 rounds MisterX's location.
async function updateMxLocation() {
    if (roundCounter !== 0 && roundCounter % 3 === 0) {
        misterXGroup.clearLayers()
        createMisterXMovementCard(misterLocation)
        const span = document.querySelector("#misterXLocation")
        span.innerHTML = misterLocation
        if (misterLocation === "Russia") {
            L.marker([54.96, 35.47]).addTo(misterXGroup).setIcon(misterXIcon)
        } else if (misterLocation === "Ireland") {
            L.marker([53.58, -8.11]).addTo(misterXGroup).setIcon(misterXIcon)
        } else {
            const url = `https://restcountries.com/v3.1/name/${misterLocation}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                console.log(json_data)
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(misterXGroup).setIcon(misterXIcon)
            } catch (error) {
                console.log("error.message")
            }
        }
    } else {
        console.log("Doesnt reveal it self")
    }
}


function checkVehicleUsability(options) {
    return options.length !== 0;            //Checks if the vehicle has options to travel, by check the list of destinations length.
}


// Randomly choose a country from the list options.
function randomlyChooseCountry(listOfOptions) {
    const randomInt = Math.floor(Math.random() * listOfOptions.length)
    return listOfOptions[randomInt]
}


// Function that creates movement card of Mister X according to vehicle he used.
async function createMisterXMovementCard(text) {
    const cardBoard = document.querySelector(".mx-cards")
    const div = document.createElement("div")
    const h1 = document.createElement("h1")
    h1.innerHTML = text
    const img = document.createElement("img")
    img.alt = ""
    if (text === "Bus") {
        img.src = "img/MxBus.jpg"
    } else if (text === "Boat") {
        img.src = "img/MxBoat.jpg"
    } else if (text === "Plane") {
        img.src = "img/MxPlane.jpg"
    } else {
        const picture = `https://restcountries.com/v3.1/name/${misterLocation}`
        try {
            const response = await fetch(picture);
            const json_data = await response.json();
            img.src = json_data[0]["flags"]["svg"]
        } catch (error) {
            console.log("error.message")
        }
    }

    div.appendChild(img)
    div.appendChild(h1)
    cardBoard.appendChild(div)
}


// Mister X moves through the map, choosing vehicle randomly.
async function randomMove() {
    const randomInt = Math.floor(Math.random() * 10) + 1;
    console.log(randomInt)
    if (randomInt <= 5) {
        await updateMxLocation()
        console.log("Mister X will use bus now...")
        await mxBusDestinations(misterLocation)

    } else if (randomInt > 5 && randomInt <= 9) {
        await updateMxLocation()
        console.log("Mister X will use boat now...")
        await mxBoatDestinations(misterLocation)

    } else {
        await updateMxLocation()
        console.log("Mister X will fly now...")
        await mxPlaneDestinations(misterLocation)

    }
}

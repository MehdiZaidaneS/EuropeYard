"use strict";

let misterLocation = ""


//Gets a country from the API and set it as Mister X Location
async function getMisterXLocation() {
    const countries = await apiCall("getallcountries", "")
    countries.splice(countries.indexOf(playerLocation), 1)
    const country = randomlyChooseCountry(countries)

    //I delete later
    const span = document.querySelector("#misterXLocation")
    span.innerHTML = country
    //----------------------------------------------------------------------
    misterLocation = country
    console.log("MisterX was spawned in " + misterLocation)

}

// Mister X bus method.
async function mxBusDestinations(location) {
    const destinations = await apiCall("busdestinations", location) //Getting all destinations

    if (destinations.includes(playerLocation)) {
        destinations.splice(destinations.indexOf(playerLocation), 1) //Removing player location as destination
    }

    if (checkVehicleUsability(destinations)) {
        const busTo = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
        await updateMxLocation(busTo) // Updating Mister X position variable and text
        console.log("Now he is in " + misterLocation)
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
        const busTo = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
        await updateMxLocation(busTo) // Updating Mister X position variable and text
        console.log("Now he is in " + misterLocation)
    } else {
        console.log("He couldn't use boat so he used bus")
        await mxBusDestinations(misterLocation) // In case not being able to use boat, uses bus.
    }
}

// Mister X flying method.
async function mxPlaneDestinations(location) {
    const destinations = await apiCall("planedestinations", location) //Getting all destinations
    destinations.splice(destinations.indexOf(playerLocation), 1) //Removing player location as destination
    const flyTo = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
    await updateMxLocation(flyTo) // Updating Mister X position variable and text
    console.log("Now he is in " + misterLocation)
}


//Function that updates every 3 rounds MisterX's location.
async function updateMxLocation(newLocation) {

    // Can delete soon.
    const span = document.querySelector("#misterXLocation")
    span.innerHTML = newLocation
    misterLocation = newLocation
    misterXGroup.clearLayers()
    // ---------------------------------------------------------------

    if (misterLocation === "Russia") {
        L.marker([54.96, 35.47]).addTo(misterXGroup).setIcon(misterXIcon)
    } else if (misterLocation === "Ireland") {
        L.marker([53.58, -8.11]).addTo(misterXGroup).setIcon(misterXIcon)
    } else {
        const url = `https://restcountries.com/v3.1/name/${misterLocation}`
        try {
            const response = await fetch(url);
            const json_data = await response.json();
            const latlng = json_data[0]["latlng"]
            L.marker(latlng).addTo(misterXGroup).setIcon(misterXIcon)
        } catch (error) {
            console.log("error.message")
        }
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


// Mister X moves through the map, choosing vehicle randomly.
async function randomMove() {
    const randomInt = Math.floor(Math.random() * 3) + 1;
    switch (randomInt) {
        case 1:
            console.log("Mister X will use bus now...")
            await mxBusDestinations(misterLocation)
            break;
        case 2:
            console.log("Mister X will use boat now...")
            await mxBoatDestinations(misterLocation)
            break;
        case 3:
            console.log("Mister X will fly now...")
            await mxPlaneDestinations(misterLocation)
            break;
    }

}

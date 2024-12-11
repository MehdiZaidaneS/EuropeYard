"use strict";

let misterLocation = ""


//Gets a country from the API and set it as Mister X Location
async function getMisterXLocation() {
    const countries = await apiCall("getallcountries", "")
    countries.splice(countries.indexOf(myLocation), 1)
    const country = randomlyChooseCountry(countries)
    console.log(countries)
    const span = document.querySelector("#misterXlocation")
    span.innerHTML = country
    misterLocation = country
    console.log("MisterX was spawned in " + misterLocation)

}

// Mister X bus method.
async function mxbusdestinations(location) {
    const destinations = await apiCall("busdestinations", location) //Getting all destinations

    if (destinations.includes(myLocation)) {
        destinations.splice(destinations.indexOf(myLocation), 1) //Removing player location as destination
    }

    if (checkVehicleUsability(destinations)) {
        const busto = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
        updateMxLocation(busto) // Updating Mister X position variable and text
        console.log("Now he is in " + misterLocation)
    } else {
        console.log("He couldnt use bus so he used boat")
        boatdestinations(misterLocation)
    }
}

// Mister X boat method.
async function mxboatdestinations(location) {
    const destinations = await apiCall("boatdestinations", location) //Getting all destinations

    if (destinations.includes(myLocation)) {
        destinations.splice(destinations.indexOf(myLocation), 1) //Removing player location as destination
    }

    if (checkVehicleUsability(destinations)) {
        const busto = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
        updateMxLocation(busto) // Updating Mister X position variable and text
        console.log("Now he is in " + misterLocation)
    } else {
        console.log("He couldnt use boat so he used bus")
        mxbusdestinations(misterLocation)
    }
}

// Mister X flying method.
async function mxplanedestinations(location) {
    const destinations = await apiCall("planedestinations", location) //Getting all destinations
    destinations.splice(destinations.indexOf(myLocation), 1) //Removing player location as destination
    const flyto = randomlyChooseCountry(destinations) //Choosing one random country from all the destinations
    updateMxLocation(flyto) // Updating Mister X position variable and text
    console.log("Now he is in " + misterLocation)
}


function checkVehicleUsability(options) {
    return options.length !== 0;

}


//Function that updates Mister X location and text location.
async function updateMxLocation(newLocation) {
    const span = document.querySelector("#misterXlocation")
    span.innerHTML = newLocation
    misterLocation = newLocation
    misterXGroup.clearLayers()
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


// Randomly choose a country from the list options.
function randomlyChooseCountry(listOfOptions) {
    const randomInt = Math.floor(Math.random() * listOfOptions.length)
    return listOfOptions[randomInt]
}


function randomMove() {
    const randomInt = Math.floor(Math.random() * 3) + 1;
    switch (randomInt) {
        case 1:
            console.log("Mister X will use bus now...")
            mxbusdestinations(misterLocation)
            break;
        case 2:
            console.log("Mister X will use boat now...")
            mxboatdestinations(misterLocation)
            break;
        case 3:
            console.log("Mister X will fly now..")
            mxplanedestinations(misterLocation)
            break;
    }

}

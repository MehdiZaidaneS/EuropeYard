"use strict"

let myLocation = ""

/*
async function getData(url){
    const response = await fetch(url)
    if (!response.ok) throw new Error ('Invalid server input!')
    const data = await response.json()
    document.querySelector("#name").innerHTML = data;
    return data
}
const data = getData("http://127.0.0.1:5000/getcountry")
*/


async function getLocation() {
    const response = await apiCall("getcountry", "")
    const span = document.querySelector("#mylocation")
    span.innerHTML = response["country"]
    myLocation = response["country"]
    console.log("My random location was " + myLocation)
    const url = `https://restcountries.com/v3.1/name/${myLocation}`
    try {
        const response = await fetch(url);
        const json_data = await response.json();
        const latlng = json_data[0]["latlng"]
        L.marker(latlng).addTo(markerGroup)
    } catch (error) {
        console.log("error.message")
    }
    return response["country"]
}

async function updateMyLocation(location) {
    myLocation = location
    const span = document.querySelector("#mylocation")
    span.innerHTML = location
    markerGroup.clearLayers()

    if (location === "Russia") {
        L.marker([54.96, 35.47]).addTo(markerGroup)
    } else if (location === "Ireland") {
        L.marker([53.58, -8.11]).addTo(markerGroup)
    } else {
        const url = `https://restcountries.com/v3.1/name/${myLocation}`
        try {
            const response = await fetch(url);
            const json_data = await response.json();
            const latlng = json_data[0]["latlng"]
            L.marker(latlng).addTo(markerGroup)
        } catch (error) {
            console.log("error.message")
        }
    }


}


const buttons = document.getElementsByClassName("vehicle")
for (let button of buttons) {
    button.addEventListener("click", function (evt) {
        evt.preventDefault();
        if (button.innerHTML === "Bus") {
            console.log("i pressed bus")
            busdestinations(myLocation)
        } else if (button.innerHTML === "Boat") {
            console.log("i pressed boat")
            boatdestinations(myLocation)
        } else {
            console.log("i pressed plane")
            planedestinations(myLocation)
        }

    })
}

async function busdestinations(location) {
    const response = await apiCall("busdestinations", location)
    for (let option of response) {
        if (option === "Russia") {
            L.marker([54.96, 35.47]).addTo(markerGroup).setIcon(greenIcon).on("click", function (e) {
                updateMyLocation(option)
            })
        } else if (option === "Ireland") {
            L.marker([53.58, -8.11]).addTo(markerGroup).setIcon(greenIcon).on("click", function (e) {
                updateMyLocation(option)
            })
        } else {
            const url = `https://restcountries.com/v3.1/name/${option}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(markerGroup).setIcon(greenIcon).on("click", function (e) {
                    updateMyLocation(option)
                })
            } catch (error) {
                console.log("error.message")
            }
        }

    }
}

async function boatdestinations(location) {
    const response = await apiCall("boatdestinations", location)
    for (let country of response) {
        if (country === "Russia") {
            L.marker([54.96, 35.47]).addTo(markerGroup).setIcon(blueIcon).on("click", function (e) {
                updateMyLocation(country)
            })
        } else if (country === "Ireland") {
            L.marker([53.58, -8.11]).addTo(markerGroup).setIcon(blueIcon).on("click", function (e) {
                updateMyLocation(country)
            })
        } else {
            const url = `https://restcountries.com/v3.1/name/${country}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(markerGroup).setIcon(blueIcon).on("click", function (e) {
                    updateMyLocation(country)
                })
            } catch (error) {
                console.log("error.message")
            }
        }

    }
}

async function planedestinations(location) {
    const response = await apiCall("planedestinations", location)
    for (let destination of response) {
        if (destination === "Russia") {
            L.marker([54.96, 35.47]).addTo(markerGroup).setIcon(yellowIcon).on("click", function (e) {
                updateMyLocation(destination)
            })
        } else if (destination === "Ireland") {
            L.marker([53.58, -8.11]).addTo(markerGroup).setIcon(yellowIcon).on("click", function (e) {
                updateMyLocation(destination)
            })
        } else {
            const url = `https://restcountries.com/v3.1/name/${destination}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(markerGroup).setIcon(yellowIcon).on("click", function (e) {
                    updateMyLocation(destination)
                })
            } catch (error) {
                console.log("error.message")
            }
        }
    }

}


async function getAllCountry() {
    let countries = []

    const response = await apiCall("getallcountries", "")
    for (let country of response) {
        countries.push(country)
    }
    return countries
}

async function getCords() {
    const countries = await getAllCountry()
    for (let country of countries) {
        if (country === "Russia") {
            L.marker([54.96, 35.47]).addTo(map).setIcon(grayIcon)
        } else if (country === "Ireland") {
            L.marker([53.58, -8.11]).addTo(map).setIcon(grayIcon)
        } else {
            const url = `https://restcountries.com/v3.1/name/${country}`
            try {
                const response = await fetch(url);
                const json_data = await response.json();
                const latlng = json_data[0]["latlng"]
                L.marker(latlng).addTo(map).setIcon(grayIcon)
            } catch (error) {
                console.log("error.message")
            }

        }

    }
}

getLocation()

"use strict"

async function apiCall(endpoint, data){

    const fetchOptions = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    }
    const url = "http://127.0.0.1:5000/"

    try{
        const response = await fetch(url + endpoint + "/" + data, fetchOptions)

        if (response.ok) {
            console.log("promise resolved and HTTP status is succesful")
            const json_response = await response.json()
            return json_response
        } else {
            const json_response = await response.json()
            // json_response still needs to get processed
            console.log(json_response.text)
        }

    }catch (error){
        console.log("promise rejected: " + error)
    }

}


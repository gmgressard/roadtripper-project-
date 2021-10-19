// hardcode 3, get working, use ajax to make request to server to get rest of data 
'use strict';

function initMap() {

    console.log("********* Function called *************")

    const natParkCoord = {
        lng: -149.63156,
        lat: 60.18852
    };

    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: natParkCoord,
        zoom: 11,
    });

    const marker = new google.maps.Marker({
        position: natParkCoord,
        title: 'np',
        map: basicMap
    })
};
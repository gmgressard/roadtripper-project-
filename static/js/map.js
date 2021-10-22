// hardcode 3, get working, use ajax to make request to server to get rest of data 
'use strict';

function initMap() {

    console.log("********* Function called *************")
    console.log($('#map').data())
    
    const natParkCoord = {
        lng: parseFloat($('#map').attr('data-lng')),
        lat: parseFloat($('#map').attr('data-lat'))
    };

    console.log(typeof natParkCoord.lng)// returns string

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
//update username and password
'use strict';

$('#updateuser').on('submit', evt => {
    evt.preventDefault();

    const formInputs = {
        newUsername: $('#new_username').val(),
        newpassword: $('#new_password').val(),
    };

    $.post('/updateprofile', formInputs, res => {
        alert(res);
    });
});



function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}


function callApiGet(url, callback, onError) {
    callApi("GET", url, {}, callback, onError)
}

function callApiPost(url, data, callback, onError) {
    callApi("POST", url, JSON.stringify(data), callback, onError)
}

function callApiPut(url, data, callback, onError) {
    callApi("PUT", url, JSON.stringify(data), callback, onError)
}

function callApiPatch(url, data, callback, onError) {
    callApi("PATCH", url, JSON.stringify(data), callback, onError)
}

function callApiDelete(url, callback, onError) {
    callApi("DELETE", url, {  }, callback, onError)
}

function callApi(type, url, data, callback, onError) {
    $.ajax({
        type: type,
        url: url,
        headers: { 'X-CSRFToken': csrftoken, 'Content-Type':'application/json'},
        dataType: 'json',
        data: data,
        success: function(result) {
            if (callback) {
                if (callback.length == 2) {
                    callback(result, url);
                } else {
                    callback(result);
                }
            }
        },
        error: function(error) {
            if (onError) {
                onError(error);
            } else {
                console.log(error);
            }
        },
    })
}

function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response;
}

$(document).ready(function () {
    csrftoken = getCookie("csrftoken");
});
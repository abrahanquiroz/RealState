function onApiError(data) {
    console.log(data)
}

function getRealStateData() {
    data = {}
    data["name"] = $("#input-name").val();
    data["address"] = $("#input-address").val();
    data["country"] = $("#input-country").val();
    data["city"] = $("#input-city").val();
    data["postal_code"] = $("#input-postal_code").val();
    data["type"] = $("#select-type").val();
    data["area"] = parseInt($("#input-area").val());
    return data;
}

$(document).ready(function() {
    $("#create-realstate-button").click(function(event) {
        data = getRealStateData()
        callApiPost("/api/real_state/", data, function(data){
            window.location.href = "/";
        }, function(data){
            onApiError(data);
        })
    });
    $("#edit-realstate-button").click(function(event) {
        realStateId = ($(this).data("id"))
        data = getRealStateData()
        callApiPut("/api/real_state/"+realStateId+"/", data, function(data){
            window.location.href = "/";
        })
    });
    $(".delete-button").click(function(event) {
        realStateId = ($(this).data("id"))
        callApiDelete("/api/real_state/"+realStateId+"/", function(data){
            window.location.href = "/";
        })
    })
});
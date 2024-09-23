$(document).ready(function() {
    $("#save-realstate-button").click(function(event) {
        data = {}
        data["name"] = $("#input-name").val();
        data["address"] = $("#input-address").val();
        data["country"] = $("#input-country").val();
        data["city"] = $("#input-city").val();
        data["postal_code"] = $("#input-postal_code").val();
        data["type"] = $("#select-type").val();
        data["area"] = parseInt($("#input-area").val());
        callApiPost("/real_state/", data, function(data){
            window.location.href = "/";
        })
    });
    $(".delete-button").click(function(event) {
        realStateId = ($(this).data("id"))
        callApiDelete("/real_state/"+realStateId+"/", function(data){
            window.location.href = "/";
        })
    })
});
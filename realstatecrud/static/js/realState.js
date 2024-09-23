function onApiError(data) {
    console.log(data)
}

function getRealStateRow(property) {
    return `
            <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">${property.name}</h5>
                        <p class="card-text">
                            <strong>Dirección:</strong> ${property.address} <br>
                            <strong>Ciudad:</strong> ${property.city} <br>
                            <strong>País:</strong> ${property.country} <br>
                            <strong>Código Postal:</strong> ${property.postal_code} <br>
                            <strong>Tipo:</strong> ${property.type} <br>
                            <strong>Área:</strong> ${property.area} m²
                        </p>
                        <div class="d-flex justify-content-between align-items-center">
                            <a href="/realstate/edit/${property.id}" class="btn btn-primary">Editar</a>
                            <button id="delete-button-${property.id}" data-id="${property.id}" type="submit" class="btn btn-danger delete-button">Eliminar</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
}

function populateRealStateTable() {
    callApiGet("/api/real_state/", function(data){
        let realStateTableText = "";
        if (data.length>0){
            for (let property of data){
                realStateTableText += getRealStateRow(property)
            };
            $("#realstate-table").html(realStateTableText)
            $("#edit-realstate-button").click(editRealState);
            $(".delete-button").click(deleteRealState);
        }else{
            let noData = `<h3 class="text-center">No hay propiedades agregadas.</h3>`
            $("#realstate-table").html(noData)
        }
    })
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

function createRealState(event) {
    data = getRealStateData()
    callApiPost("/api/real_state/", data, function(data){
        window.location.href = "/";
    }, function(data){
        onApiError(data);
    })
}

function editRealState(event) {
    realStateId = ($(this).data("id"))
    data = getRealStateData()
    callApiPut("/api/real_state/"+realStateId+"/", data, function(data){
        window.location.href = "/";
    })
}

function deleteRealState(event) {
    realStateId = ($(this).data("id"))
    callApiDelete("/api/real_state/"+realStateId+"/", function(data){
        window.location.href = "/";
    })
}

$(document).ready(function() {
    realStateTable = $("#realstate-table");
    if (realStateTable.length===1) {
      populateRealStateTable();
    }
    $("#create-realstate-button").click(createRealState);
    $("#edit-realstate-button").click(editRealState);
    $(".delete-button").click(deleteRealState);
    $("#input-filter-realstate").change(function(event){
        filterText = $(this).val()
        console.log(filterText)
    });
    
});


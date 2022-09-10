

  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var Carname = document.getElementById("cbrand");
    var Caryear = document.getElementById("cyear");
    var SellerType = document.getElementById("cseller");
    var KM_driven = document.getElementById("ckmdriven");
    var FuelType=document.getElementById("cfuel");
    var Transmission = document.getElementById("ctrans");
    var Owner = document.getElementById("cowner");
    var Milage = document.getElementById("cmilage");
    var Engine = document.getElementById("cengin");
    var Seates = document.getElementById("cseats");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
     var url = "http://127.0.0.1:5000/used_car_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/used_car_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        Carname: Carname.value,
        Caryear: Caryear.value,
        SellerType: SellerType.value,
        KM_driven: KM_driven.value,
        FuelType: FuelType.value,
        Transmission: Transmission.value,
        Owner: Owner.value,
        Milage: Milage.value,
        Engine: Engine.value,
        Seates: Seates.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/used_car_price"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/used_car_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_vehical_names request");
        if(data) {
            var Carname = data.Carname;
            var cbrand = document.getElementById("cbrand");
            $('#cbrand').empty();
            for(var i in Carname) {
                var opt = new Option(Carname[i]);
                $('#cbrand').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;
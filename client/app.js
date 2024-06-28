function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
	var mean_radius = document.getElementById("uimean_radius");
  var mean_texture = document.getElementById("uimean_texture");
  var mean_perimeter = document.getElementById("uimean_perimeter");
  var mean_area = document.getElementById("uimean_area");
  var mean_smoothness = document.getElementById("uimean_smoothness");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_breast_cancer"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      t_mean_radius: parseFloat(mean_radius.value),
      t_mean_texture: parseFloat(mean_texture.value),
      t_mean_perimeter: parseFloat(mean_perimeter.value),
      t_mean_area: parseFloat(mean_area.value),
      t_mean_smoothness: parseFloat(mean_smoothness.value)
  },function(data, status) {
      console.log(data.estimated_price);
      var prediction = data.prediction;
      console.log(prediction)
      if (prediction == 1){
        estPrice.innerHTML = "<h2>" + "Positive" + " :(</h2>";
      }
      else if (prediction == 0){
        estPrice.innerHTML = "<h2>" + "Negative" + " :)</h2>";
      }
      // estPrice.innerHTML = "<h2>" + data.prediction.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "page loaded" );
}

window.onload = onPageLoad;

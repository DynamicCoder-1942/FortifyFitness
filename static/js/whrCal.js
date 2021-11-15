document.getElementById('calorie-form').addEventListener('submit', function(e){
    document.getElementById('results').style.display = 'none';
  
    document.getElementById('loading').style.display = 'block';
  
    setTimeout(calculateCalories, 2000);
  
    e.preventDefault();
  });
  
  function calculateCalories(e) {
    
    //const age = document.getElementById('age');
    const gender = document.querySelector('input[name="customRadioInline1"]:checked');
    const weight = document.getElementById('weight');
    const height = document.getElementById('height');
    //const activity = document.getElementById('list').value;
    const totalCalories = document.getElementById('total-calories');
    
    
  var whrRatio = (height.value/weight.value).toFixed(2);
  totalCalories.value = whrRatio
  
  //document.getElementById("demo").innerHTML = "Hello world";
  
  
  if (totalCalories.value <= 0.80) {
    document.getElementById("demo").innerHTML = "Based upon a waist measurement and hip measurement you have 'LOW health risk'";
  }
  else if (totalCalories.value > 0.81 && totalCalories.value < 0.84) {
    document.getElementById("demo").innerHTML = "Based upon a waist measurement and hip measurement you have 'MODERATE health risk'";
  }
  else if (totalCalories.value >= 0.85) {
    document.getElementById("demo").innerHTML = "Based upon a waist measurement and hip measurement you have 'HIGH health risk'";
  }
  else {
    document.getElementById("demo").innerHTML = " ";
  }
  
  //totalCalories.value = whrRatio
  
  
  
  
    document.getElementById('results').style.display = 'block';
  
    document.getElementById('loading').style.display = 'none';
  }
  
  function errorMessage(error) {
    document.getElementById('results').style.display = 'none';
  
    document.getElementById('loading').style.display = 'none';
    const errorDiv = document.createElement('div');
    const card = document.querySelector('.card');
    const heading = document.querySelector('.heading');
    errorDiv.className = 'alert alert-danger';
    errorDiv.appendChild(document.createTextNode(error));
  
    card.insertBefore(errorDiv, heading);
  
    setTimeout(clearError, 4000);
  }
  
  function clearError() {
    document.querySelector('.alert').remove();
  }
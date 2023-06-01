function submitForm() {
    // Get form data
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    // Create JSON object
    var data = {
      name: name,
      birth: parseInt(age),  // Assuming birth is represented by age in this example
      death: null,  // Modify this if you have a way to get the death value
      powers: null,  // Modify this if you have a way to get the powers value
      allies: null,  // Modify this if you have a way to get the allies value
      image: null  // Modify this if you have a way to get the image value
    };
    // Send POST request to FastAPI endpoint
    fetch('/hero', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {  
        if (response.ok) {
    // Handle successful response
    response.json().then(superhero => {
      console.log('Form data submitted successfully.');
      console.log('Received superhero object:', superhero);
      // Display confirmation message or perform further actions with the superhero object
      document.getElementById("jin").innerHTML = "Successfly Posted via JavaScript: as JSON Object<br>"+
      "Posted to '/hero' End-Point with a post method sent as json <br>"+
      "Server returned 'Superhero' object<br>superhero.name: "+superhero.name+"<br>superhero.birth: "
      +superhero.birth;
    });
      } else {
        // Handle error response
        console.error('Error submitting form data.');
      }
    })
    .catch(error => {
      // Handle network error
      console.error('Network error:', error);
    });
  }
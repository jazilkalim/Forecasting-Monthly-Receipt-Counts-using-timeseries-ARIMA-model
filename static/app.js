function onClickedPredictCount() {
  // Get the year input value
  var year = document.getElementById('uiYear').value;
  var month = document.querySelector('input[name="uiMonth"]:checked').value;

  // Ensure the form is filled correctly
  if (!year || !month) {
      alert('Please enter both year and month');
      return;
  }

  // Use jQuery to send a POST request to the Flask server
  $.ajax({
      url: 'http://127.0.0.1:5000/predict_receipt_count',  // Flask server URL
      method: 'POST',
      contentType: 'application/x-www-form-urlencoded',
      data: { year: year, month: month },
      success: function(response) {
          // Show the result in the UI
          document.getElementById('predicted-count').innerText = response.estimated_count;
      },
      error: function(error) {
          console.error('Error:', error);
          alert('Failed to get prediction');
      }
  });
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');
    const predictedValueP = document.getElementById('predicted-value');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        console.log('Submitting data:', data);

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Received data:', data);
            predictedValueP.textContent = `$${data.prediction.toFixed(2)}`;
            resultDiv.classList.remove('hidden');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while making the prediction.');
        });
    });
});
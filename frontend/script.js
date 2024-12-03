document.getElementById('check-btn').addEventListener('click', async () => {
    const features = [
        document.getElementById('feature1').value,
        document.getElementById('feature2').value,
        document.getElementById('feature3').value,
        document.getElementById('feature4').value,
        document.getElementById('feature5').value,
        document.getElementById('feature6').value,
        document.getElementById('feature7').value,
        document.getElementById('feature8').value,
    ].map(Number);

    const response = await fetch('http://192.168.0.17:5010/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ features }),
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.result || data.error;
});
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

// Add a toggle button to switch between dark and light modes
// Toggle dark mode based on user preference
const toggleDarkMode = () => {
    document.body.classList.toggle('dark-mode');
    
    // Save the current theme in localStorage
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
};

// Check if there's a saved theme in localStorage and apply it
window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }

    // Add dark mode toggle button
    const darkModeButton = document.createElement('button');
    darkModeButton.textContent = 'Toggle Dark Mode';
    darkModeButton.style.position = 'absolute';
    darkModeButton.style.top = '20px';
    darkModeButton.style.right = '20px';
    darkModeButton.style.padding = '10px 20px';
    darkModeButton.style.backgroundColor = '#007bff';
    darkModeButton.style.color = 'white';
    darkModeButton.style.border = 'none';
    darkModeButton.style.borderRadius = '5px';
    darkModeButton.style.cursor = 'pointer';

    darkModeButton.addEventListener('click', toggleDarkMode);
    document.body.appendChild(darkModeButton);
});
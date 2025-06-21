const microphoneBtn = document.getElementById('microphoneBtn');
const outputCommand = document.getElementById('outputCommand');
const outputResponse = document.getElementById('outputResponse');

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const speechSynthesis = window.speechSynthesis;

if (SpeechRecognition && speechSynthesis) {
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    microphoneBtn.addEventListener('click', () => {
        recognition.start();
        outputCommand.textContent = 'Listening...';
        outputResponse.textContent = '';
    });

    recognition.onresult = (event) => {
        const command = event.results[0][0].transcript;
        outputCommand.textContent = command;
        sendCommandToBackend(command);
    };

    recognition.onerror = (event) => {
        outputCommand.textContent = `Error: ${event.error}`;
        speakText(`Sorry, I didn't catch that. Error: ${event.error}`);
    };

    function sendCommandToBackend(command) {
        fetch('https://yugi123.pythonanywhere.com/command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => {
            outputResponse.textContent = data.response;
            speakText(data.response);
        })
        .catch(error => {
            console.error('Error:', error);
            outputResponse.textContent = 'Error communicating with backend.';
            speakText('Sorry, there was an error communicating with the backend.');
        });
    }

    function speakText(text) {
        speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
    }

} else {
    microphoneBtn.disabled = true;
    outputCommand.textContent = 'Web Speech API is not supported in this browser.';
    alert('Web Speech API is not supported in this browser. Please use Chrome or Edge.');
}

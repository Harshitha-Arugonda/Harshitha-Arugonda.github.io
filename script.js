// Initialize SpeechRecognition object
const recognition = new webkitSpeechRecognition();

// Set properties for recognition
recognition.continuous = false;
recognition.interimResults = false;

// Function to handle when speech is recognized
recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById('output').textContent = transcript;

    // Send the transcript to the server for further processing (you'll need server-side code for this)
    sendTranscriptToServer(transcript);
};

// Function to start speech recognition when button is clicked
document.getElementById('start-btn').addEventListener('click', function() {
    recognition.start();
});

// Function to send transcript to server for processing
function sendTranscriptToServer(transcript) {
    // Send the transcript to the server using fetch or XMLHttpRequest
    // You'll need server-side code to handle this request and convert speech to text
}

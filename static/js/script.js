const messages = document.getElementById("messages");

// ================= SEND MESSAGE =================
document.getElementById("send").onclick = async () => {

    const questionInput = document.getElementById("question");
    const question = questionInput.value;

    if (!question) return;

    // USER MESSAGE
    messages.innerHTML += `
        <div class="chat user-msg user">
            <img src="/static/user.png" class="avatar">
            <div class="bubble">${question}</div>
        </div>
    `;

    // LOADER
    const loaderId = "loader-" + Date.now();
    messages.innerHTML += `
        <div class="chat bot-msg bot" id="${loaderId}">
            <img src="/static/bot.png" class="avatar">
            <div class="bubble">
                <span class="spinner"></span> Thinking...
            </div>
        </div>
    `;

    messages.scrollTop = messages.scrollHeight;

    // API CALL
    const response = await fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question})
    });

    const data = await response.json();

    // REPLACE LOADER WITH RESPONSE
    const loaderDiv = document.getElementById(loaderId);

    loaderDiv.innerHTML = `
        <img src="/static/bot.png" class="avatar">
        <div class="bubble">
            <span id="typing-${loaderId}"></span>

            <div class="actions">
                <button onclick="speakText(\`${data.answer}\`)">🔊</button>
                <button onclick="copyText(\`${data.answer}\`)">📋</button>
            </div>
        </div>
    `;

    const typingDiv = document.getElementById(`typing-${loaderId}`);

    typeEffect(typingDiv, data.answer);

    // AUTO SPEAK (optional)
    speakText(data.answer);

    questionInput.value = "";
    messages.scrollTop = messages.scrollHeight;
};


// ================= TYPING EFFECT =================
function typeEffect(element, text, speed = 15) {
    let i = 0;
    element.innerHTML = "";

    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }

    typing();
}


// ================= VOICE INPUT =================
const voiceBtn = document.getElementById("voice");

voiceBtn.onclick = () => {

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("❌ Voice not supported. Use Chrome/Edge.");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.start();

    voiceBtn.innerText = "🎤 Listening...";
    voiceBtn.classList.add("listening");

    recognition.onresult = (e) => {
        document.getElementById("question").value =
            e.results[0][0].transcript;
    };

    recognition.onerror = (e) => {
        console.error(e);
        alert("Mic error: " + e.error);
    };

    recognition.onend = () => {
        voiceBtn.innerText = "🎤 Speak";
        voiceBtn.classList.remove("listening");
    };
};


// ================= SPEAK TEXT =================
function speakText(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN";
    speech.rate = 1;

    window.speechSynthesis.speak(speech);
}


// ================= COPY =================
function copyText(text) {
    navigator.clipboard.writeText(text);
    alert("Copied!");
}


// ================= DROPDOWN =================
document.getElementById("suggestions").onchange = function() {
    document.getElementById("question").value = this.value;
};


// ================= THEME TOGGLE =================
const toggle = document.getElementById("themeToggle");

toggle.onclick = () => {
    const body = document.body;

    if (body.classList.contains("dark-mode")) {
        body.classList.replace("dark-mode", "light-mode");
        toggle.innerText = "☀️";
    } else {
        body.classList.replace("light-mode", "dark-mode");
        toggle.innerText = "🌙";
    }
};
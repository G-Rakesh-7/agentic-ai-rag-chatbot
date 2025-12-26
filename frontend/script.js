const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

function addMessage(content, isUser = false) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = isUser ? "👤" : "🤖";
    
    const messageContent = document.createElement("div");
    messageContent.className = "message-content";
    
    const messageText = document.createElement("p");
    messageText.textContent = content;
    
    messageContent.appendChild(messageText);
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(messageContent);
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageDiv;
}

function addTypingIndicator() {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message bot-message";
    messageDiv.id = "typingIndicator";
    
    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = "🤖";
    
    const typingDiv = document.createElement("div");
    typingDiv.className = "typing-indicator";
    typingDiv.innerHTML = "<span></span><span></span><span></span>";
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(typingDiv);
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById("typingIndicator");
    if (indicator) {
        indicator.remove();
    }
}

async function send() {
    const question = userInput.value.trim();
    
    if (!question) {
        return;
    }
    
    // Add user message
    addMessage(question, true);
    
    // Clear input and disable button
    const questionToSend = question;
    userInput.value = "";
    sendButton.disabled = true;
    
    // Add typing indicator
    addTypingIndicator();
    
    try {
        console.log("Sending question:", questionToSend);
        
        const response = await fetch("/chat", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({ question: questionToSend })
        });
        
        console.log("Response status:", response.status);
        
        removeTypingIndicator();
        
        if (!response.ok) {
            const errorText = await response.text();
            console.error("Error response:", errorText);
            throw new Error(`Server error: ${response.status} - ${errorText}`);
        }
        
        const data = await response.json();
        console.log("Response data:", data);
        
        if (data && data.answer) {
            addMessage(data.answer, false);
        } else {
            throw new Error("Invalid response format from server");
        }
    } catch (error) {
        removeTypingIndicator();
        console.error("Full error:", error);
        const errorMessage = `Error: ${error.message}. Make sure the backend server is running on port 8000.`;
        const errorDiv = addMessage(errorMessage, false);
        errorDiv.querySelector(".message-content").classList.add("error-message");
    } finally {
        sendButton.disabled = false;
        userInput.focus();
    }
}

function handleKeyPress(event) {
    if (event.key === "Enter" || event.keyCode === 13) {
        if (!event.shiftKey) {
            event.preventDefault();
            send();
        }
    }
}

// Make functions globally accessible
window.send = send;
window.handleKeyPress = handleKeyPress;

// Focus input on load
window.addEventListener("load", () => {
    if (userInput) {
        userInput.focus();
    }
});

// Also try DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
    if (userInput) {
        userInput.focus();
    }
});

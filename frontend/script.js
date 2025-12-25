async function send() {
    const question = document.getElementById("userInput").value;
    const responseElement = document.getElementById("response");
    
    if (!question.trim()) {
        responseElement.innerText = "Please enter a question.";
        return;
    }
    
    responseElement.innerText = "Thinking...";
    
    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });
        
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        
        const data = await response.json();
        responseElement.innerText = data.answer;
    } catch (error) {
        responseElement.innerText = `Error: ${error.message}. Make sure the backend server is running on http://127.0.0.1:8000`;
        console.error("Error:", error);
    }
}
  
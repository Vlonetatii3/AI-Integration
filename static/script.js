const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatContainer = document.getElementById("chatContainer");
const resetBtn = document.getElementById("resetBtn");

function addMessage(text, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);

  const bubbleDiv = document.createElement("div");
  bubbleDiv.classList.add("bubble");
  bubbleDiv.textContent = text;

  messageDiv.appendChild(bubbleDiv);
  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const message = messageInput.value.trim();
  if (!message) return;

  addMessage(message, "user");
  messageInput.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    addMessage(data.reply, "bot");
  } catch (error) {
    addMessage("Error connecting to server.", "bot");
  }
});

resetBtn.addEventListener("click", async () => {
  try {
    const response = await fetch("/reset", {
      method: "POST"
    });

    const data = await response.json();
    addMessage(data.message, "bot");
  } catch (error) {
    addMessage("Could not reset the game.", "bot");
  }
});
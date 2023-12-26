const socket = new WebSocket("ws://localhost:5000");

socket.onopen = (event) => {
  console.log("WebSocket connection opened:", event);
  socket.send("Hello, WebSocket!");
};

socket.onmessage = (event) => {
  console.log("Received message:", event.data);
};

socket.onclose = (event) => {
  console.log("WebSocket connection closed:", event);
};

socket.onerror = (error) => {
  console.error("WebSocket error:", error);
};

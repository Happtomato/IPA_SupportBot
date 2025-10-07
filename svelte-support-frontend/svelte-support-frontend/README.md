# README - Svelte Frontend with Docker Deployment
<!-- TOC -->
* [README - Svelte Frontend with Docker Deployment](#readme---svelte-frontend-with-docker-deployment)
  * [Overview](#overview)
  * [Main Script](#main-script)
    * [App Component](#app-component)
    * [ChatMessage Component](#chatmessage-component)
    * [ChatContainer Component](#chatcontainer-component)
    * [ChatInput Component](#chatinput-component)
    * [Docker Deployment](#docker-deployment)
    * [Conclusion](#conclusion)
<!-- TOC -->

## Overview
This Svelte application provides a frontend interface for a chatbot service. It consists of four main components and is designed to be deployed using Docker.

## Main Script
The main script (`<script>` tag at the top) manages the core functionality of the application:
- **Imports:** Components `ChatMessage`, `ChatInput`, and `ChatContainer` are imported.
- **Message Handling:** A `messages` array is maintained to store both user and bot messages.
- **sendMessage Function:** 
  - Handles sending messages to the backend Flask API.
  - Updates the `messages` array with the user's query and the bot's response.
  - Handles API responses and errors.

```javascript
import ChatMessage from './ChatMessage.svelte';
import ChatInput from './ChatInput.svelte';
import ChatContainer from './ChatContainer.svelte';

let messages = [];
async function sendMessage(event) {
  // ...
}
```
### App Component
The `<div class="app">` is the main container for the chat application:

ChatContainer: Wraps the messages display.
Each Loop: Iterates over `messages` to display each message.
ChatInput: Component for user to input their messages.
```html
<div class="app">
  <ChatContainer>
    <!-- Loop through messages -->
  </ChatContainer>
  <ChatInput on:sendMessage={sendMessage}/>
</div>

<style>
  .app { /* Styling for the app container */ }
</style>
```
### ChatMessage Component
This component displays individual chat messages, distinguishing between user and bot messages:

Styling: Differentiates between user and bot messages through styling.
Avatar: Shows an avatar for bot messages.
```html
<div class="message-container {message.sender}">
  <!-- Conditional rendering for bot avatar -->
  <div class="message-text">{message.text}</div>
</div>

<style>
  .message-container { /* Styling for message container */ }
</style>
```
### ChatContainer Component
Defines the layout and style of the chat messages container:

Slot: A slot for placing the chat messages.
Scrolling: Handles vertical scrolling for overflow content.
```html
<div class="chat-container">
  <slot />
</div>

<style>
  .chat-container { /* Styling for chat container */ }
</style>
```
### ChatInput Component
Manages user input for sending messages:

Event Dispatch: Uses Svelte's createEventDispatcher for sending messages.
Input Handling: Manages text input and sends messages on button click or 'Enter' key press.
```html
<div class="input-area">
  <input type="text" bind:value={inputText} on:keyup={(e) => e.key === 'Enter' && onSend()} placeholder="Type your message here..." />
  <button on:click={onSend}>Send</button>
</div>

<style>
  .input-area { /* Styling for input area */ }
</style>
```
### Docker Deployment
This application is configured for deployment using Docker, ensuring it can be hosted on any platform supporting Docker containers.

### Conclusion
The frontend is structured into modular components for ease of maintenance and clarity. It integrates seamlessly with the backend API, providing a dynamic user experience for interacting with the chatbot.
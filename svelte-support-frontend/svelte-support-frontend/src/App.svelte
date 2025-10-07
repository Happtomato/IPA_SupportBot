<script>
  import ChatMessage from './ChatMessage.svelte';
  import ChatInput from './ChatInput.svelte';
  import ChatContainer from './ChatContainer.svelte';

  let messages = [];

  async function sendMessage(event) {
    const text = event.detail;
    const userMessage = {text, sender: 'user'};
    messages = [...messages, userMessage];

    try {
      const apiResponse = await fetch('https://fl-supportbot-api.azurewebsites.net/sendMessageToAzure', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({Question: text}),
      });

      if (!apiResponse.ok) {
        throw new Error(`HTTP error! Status: ${apiResponse.status}`);
      }

      const response = await apiResponse.json();
      const botReply = response.message || "I didn't understand that.";
      messages = [...messages, {text: botReply, sender: 'bot'}];
    } catch (error) {
      messages = [...messages, {text: 'Sorry, there was an error processing your request.', sender: 'bot'}];
    }
  }

  $: if (messages.length > 0) {
    setTimeout(() => {
      const chatContainer = document.querySelector('.chat-container');
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 0);
  }
</script>

<div class="app">
  <ChatContainer>
    {#each messages as message, index (index)}
      <ChatMessage key={index} {message}/>
    {/each}
  </ChatContainer>
  <ChatInput on:sendMessage={sendMessage}/>
</div>

<style>
  .app {
    max-width: 600px;
    margin: auto;
    margin-top: 50px;
  }
</style>

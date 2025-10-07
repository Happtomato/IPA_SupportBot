<script>
  export let message;
</script>

<div class="message-container {message.sender}">
  {#if message.sender === 'bot'}
    <div class="avatar"></div>
  {/if}
  <div class="message-text">{message.text}</div>
</div>

<style>
  .message-container {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    max-width: 100%;
  }
  .message-container.bot {
    flex-direction: row;
  }
  .message-container.user {
    flex-direction: row-reverse;
  }
  .message-text {
    padding: 10px;
    border-radius: 20px;
    background-color: #e0e0e0;
    color: #333;
    text-align: left;
    max-width: calc(100% - 50px);
    margin: 0 10px;
  }
  .message-container.user .message-text {
    background-color: #a8300c;
    color: white;
  }
  .avatar {
    min-width: 30px;
    height: 30px;
    border-radius: 50%;
    background-image: url('/bot_avatar.png');
    background-size: cover;
    background-position: center;
    margin-right: 10px;
  }
</style>

<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  let inputText = '';

  function onSend() {
    dispatch('sendMessage', inputText.trim());
    inputText = '';
  }
</script>

<div class="input-area">
    <input
      type="text"
      bind:value={inputText}
      on:keyup={(e) => e.key === 'Enter' && onSend()}
      placeholder="Type your message here..."
    />
    <button on:click={onSend}>Send</button>
</div>

<style>
  .input-area {
    display: flex;
    justify-content: space-between;
    padding: 10px;
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    border-radius: 20px;
  }
  input[type="text"] {
    flex-grow: 1;
    padding: 10px;
    margin-right: 10px;
    border: 2px solid #ccc;
    border-radius: 20px;
  }
  button {
    padding: 10px 20px;
    border-radius: 20px;
    border: none;
    background-color: #ff5722;
    color: white;
    cursor: pointer;
  }
  button:hover {
    background-color: #e64a19;
  }
</style>

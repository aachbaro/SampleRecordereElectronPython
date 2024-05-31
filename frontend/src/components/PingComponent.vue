<template>
    <div>
      <button @click="sendPing">Test Ping</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PingComponent',
    methods: {
      async sendPing() {
        try {
          const response = await fetch('http://localhost:5000/ping');
          const text = await response.text();
          console.log(text);  // Affiche "pong" dans la console
        } catch (error) {
          console.error('Error:', error);
        }
      }
    }
  }
  </script>
<template>
    <div>
      <button @click="sendPing">Test Ping</button>
    </div>
</template>
  
<script>

  import axios from 'axios'

  export default {
    name: 'PingComponent',
    methods: {
      async sendPing() {
        const path = 'http://localhost:5000/ping'
        axios.get(path)
        .then ((res) => {
          console.log(res.data)
        })
        .catch ((err) => {
          console.error(err)
        })
      }
    }
  }
</script>
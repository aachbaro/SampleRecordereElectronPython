<template>
    <v-container>
        <div
          @mouseenter="expandWindow"
          @mouseleave="shrinkWindow">
          <v-btn icon size="20" @click="startRecording">
            <v-icon size="18">mdi-microphone</v-icon>
          </v-btn>
        </div>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'RecordWidget',
    data() {
        return {
          originalWidth: window.outerWidth, // Stocke la largeur originale de la fenêtre
          originalHeight: window.outerHeight // Stocke la hauteur originale de la fenêtre
      };
    },
    methods: {
      startRecording() {
        console.log('Recording button pressed');
        axios.post('http://127.0.0.1:5000/recordButtonClicked')
            .then(response => {
                console.log('File uploaded successfully');
                console.log(response)

                this.$emit('file-uploaded');
            })
            .catch(error => {
                console.error('Error uploading file', error);
            });
      },
      expandWindow() {

      // const newWidth = 170;
      window.resizeTo(100, 0);
    },
    shrinkWindow() {
      // Ajustez la largeur de votre fenêtre à sa taille originale
      // par exemple, réduisez de 100 pixels
      // const newWidth = 70;
      window.resizeTo(50, 0);
    }
    }
  }
  </script>

<style scoped>
  
  .v-container {
    background-color: transparent !important; /* Ensure the background is transparent */
    width: 100%;
    padding: 5px;
    margin-right: auto;
    margin-left: auto;
}
</style>
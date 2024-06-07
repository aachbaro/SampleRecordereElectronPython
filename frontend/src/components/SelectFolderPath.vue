<template>
    <div>
      <input type="file" ref="directoryInput" style="display: none" webkitdirectory @change="handleDirectorySelection" />
      <v-btn icon @click="selectDirectory">
        <v-icon>mdi-folder</v-icon>
      </v-btn>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'SelectDirectoryPath',
    methods: {
        selectDirectory() {

        },
        handleFileUpload(event) {
            if (event) {
                const dataToSend = "caca";

                axios.post('http://127.0.0.1:5000/upload', dataToSend)
                .then(response => {
                    console.log('File uploaded successfully');
                    console.log(response)

                    this.$emit('file-uploaded');
                })
                .catch(error => {
                    console.error('Error uploading file', error);
                });
            }
        }
    }
  };
  </script>
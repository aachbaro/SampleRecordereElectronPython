<template>
    <div>
      <input type="file" ref="directoryInput" style="display: none" @change="handleDirectorySelection" />
      <v-btn icon @click="selectDirectory">
        <v-icon>mdi-folder</v-icon>
      </v-btn>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  // const { ipcRenderer } = require('electron')
  
  
  export default {
    name: 'SelectFolderPath',
    methods: {
        selectDirectory() {
          console.log("select-folder-path")
          window.ipcRenderer.send('select-folder', 'Message simple depuis SelectFolderPath');
        },
    },
    mounted() {
      window.ipcRenderer.receive('select-folder', (filePaths) => {
        console.log('Dossiers sélectionnés :', filePaths);
        this.$emit('directorySelected', filePaths);

      axios.post('http://127.0.0.1:5000/selectSaveFolder', filePaths)
              .then(response => {
                  console.log('Folder selected successfully');
                  console.log(response)
              })
              .catch(error => {
                  console.error('Error selecting folder', error);
              });
      });
    }
  };
  </script>
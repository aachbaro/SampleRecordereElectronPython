<template>
    <div>
      <input type="file" ref="fileInput" style="display: none" @change="handleFileUpload" />
      <v-btn icon @click="selectFile">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    name: 'SelectFileButton',
    methods: {
      selectFile() {
        this.$refs.fileInput.click();
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const dataToSend = file.path;
            this.$emit('directorySelected', dataToSend);
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
  
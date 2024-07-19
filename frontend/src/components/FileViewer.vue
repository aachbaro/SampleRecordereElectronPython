<template>
    <v-container>
      <v-card class="mx-auto" width="100%" max-width="600" color="#e8eddf">
        <v-toolbar title="Sample">
          <!-- <SelectFileButton @file-uploaded="fetchSamples" /> -->
          <SelectFolderPath @directorySelected="fetchSamples" />
        </v-toolbar>
          <v-list class="scrollable-list">
            <v-list-item v-for="(sample, index) in samples" :key="index">
              <SampleItem :sample="sample" />
            </v-list-item>
          </v-list>
      </v-card>
    </v-container>
  </template>
  
  <script>
    import SampleItem from './SampleItem.vue'
    import SelectFolderPath from './SelectFolderPath.vue'
    import axios from 'axios'
  
    export default {
        name: 'SampleLibrary',
        components: {
            SampleItem,
            SelectFolderPath
            // SelectFileButton,
        },
        data: () => ({
            samples: []
        }),
        methods: {
            async fetchSamples() {
              console.log("FileViewer: fetch Sample")
                try {
                    await axios.get('http://localhost:5000/getSampleLibrary')
                    .then((res) => {
                      console.log("res", res.data)

                    })
                    
                } catch (error) {
                    console.error("There was an error fetching the samples:", error);
                }
            },
        },
        mounted() {
          this.fetchSamples();
        }
    }
  </script>

<style scoped>
.scrollable-list {
  max-height: 400px;
  overflow-y: auto;
}
</style>

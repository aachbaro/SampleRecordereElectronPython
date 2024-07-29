<template>
    <v-container>
      <v-card class="mx-auto" width="100%" max-width="600" color="#e8eddf">
        <v-toolbar title="Samples">
          <SelectFileButton @file-uploaded="fetchSamples" />
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
  import SelectFileButton from './BrowseFile.vue'
  import axios from 'axios'
  
  export default {
    name: 'SampleLibrary',
    components: {
      SampleItem,
      SelectFileButton
    },
    data: () => ({
      samples: []
    }),
    methods: {
      async fetchSamples() {
        try {
          console.log("SampleLibfetchSample")
          const response = await axios.get('http://localhost:5000/getSampleLibrary');
          this.samples = response.data.reverse();
        } catch (error) {
          console.error("There was an error fetching the samples:", error);
        }
      }
    },
    mounted() {
      // this.fetchSamples();
    }
  }
  </script>


<style scoped>
  .scrollable-list {
    max-height: 400px;
    overflow-y: auto;
  }
</style>

<template>
  <v-container>
    <v-col class="mb-4">
      <v-row class="text-center">
        <h1 class="display-2 font-weight-bold mb-3">100PLEUR</h1>
      </v-row>
      <v-row>
        <sample-library />
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
// import PingComponent from '../components/PingComponent.vue'
// import SelectFileButton from '../components/BrowseFile.vue'
import SampleLibrary from "../components/FileViewer.vue";
// import SelectFolderPath from '../components/SelectFolderPath.vue'

export default {
  name: "HomeComponent",
  components: {
    // PingComponent,
    // SelectFileButton,
    SampleLibrary,
    // SelectFolderPath
  },
  data: () => ({}),
};
</script>

<style scoped>


</style>

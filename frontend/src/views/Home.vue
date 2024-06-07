<template>
  <v-container>
    <v-col class="mb-4">
    <v-row class="text-center">
      <!-- <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col> -->

        <h1 class="display-2 font-weight-bold mb-3">
          100PLEUR
        </h1>
        <select-folder-path />
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
import SampleLibrary from '../components/SampleLibrary.vue'
import SelectFolderPath from '../components/SelectFolderPath.vue'


export default {
  name: 'HomeComponent',
  components: {
    // PingComponent,
    // SelectFileButton,
    SampleLibrary,
    SelectFolderPath
  },
  data: () => ({
  }),
}
</script>

<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          100PLEUR
        </h1>
        <ping-component />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import PingComponent from '../components/PingComponent.vue'

export default {
  name: 'HomeComponent',
  components: {
    PingComponent
  },
  data: () => ({
  }),
}
</script>

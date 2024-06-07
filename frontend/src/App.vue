<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <v-main>
      <!-- <v-row> -->
        <!-- <router-link to="/Home">HomeComponent</router-link> -->
        <router-view />
      <!-- </v-row> -->
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
}
</script>

<style scoped>
.v-main {
    /* overflow: hidden; */
    background-color: transparent !important;
    scrollbar-width: none;
    overflow-y: hidden;
}

::-webkit-scrollbar {
  width: 0px !important
}
</style>

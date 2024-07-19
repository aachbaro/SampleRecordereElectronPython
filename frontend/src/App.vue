<!-- frontend/src/App.vue -->

<template>
  <v-app>
        <router-view class="routerView"></router-view>
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

<style>

/* .v-app {
  background-color: ;
} */

/* .v-main {
    overflow: hidden;
    background-color: transparent;
    scrollbar-width: none;
    overflow-y: hidden;
} */

::-webkit-scrollbar {
  width: 0px !important
}

.routerView {
  background-color: black;
}

</style>

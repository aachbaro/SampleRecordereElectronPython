<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <router-view class="routerView"></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
};
</script>

<style>
::-webkit-scrollbar {
  width: 0px !important;
}

.routerView {
  background-color: black;
}
</style>

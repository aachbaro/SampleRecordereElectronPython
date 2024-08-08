<!-- frontend/src/App.vue -->

<template>
  <v-app class="entireApp">
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

.entireApp {
  height: 100%;
}
</style>

<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <v-main>
      <router-link to="/">HomeComponent</router-link>
    </v-main>
    <router-view />
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

<template>
  <v-container>
    <v-card class="mx-auto" width="100%" max-width="600" color="#e8eddf">
      <v-toolbar title="Samples"> </v-toolbar>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "SampleLibrary",
  components: {},
  data: () => ({}),
  computed: {
    libraries_paths() {
      return this.$store.state.libraries_paths;
    },
    libraries_names() {
      return this.$store.state.libraries_names;
    },
  },
  methods: {},
  mounted() {
    this.$store.dispatch("fetchLibrariesPaths");
  },
};
</script>

<style scoped>
.scrollable-list {
  max-height: 400px;
  overflow-y: auto;
}
</style>

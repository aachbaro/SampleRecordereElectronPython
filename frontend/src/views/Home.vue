<template>
  <v-container>
    <v-col class="mb-4">
      <v-tabs v-model="tab">
        <v-tab value="Libraries">Libraries</v-tab>
        <v-tab value="Settings">Settings</v-tab>
      </v-tabs>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="Libraries">
          <sample-library />
        </v-tabs-window-item>
        <v-tabs-window-item value="Settings">
          <settings-component />
        </v-tabs-window-item>
      </v-tabs-window>
    </v-col>
  </v-container>
</template>

<script>
import SampleLibrary from "../components/FileViewer.vue";
import SettingsComponent from "../components/Settings.vue";

export default {
  name: "HomeComponent",
  components: {
    SampleLibrary,
    SettingsComponent,
  },
  data: () => ({
    tab: null,
  }),
};
</script>

<style scoped></style>

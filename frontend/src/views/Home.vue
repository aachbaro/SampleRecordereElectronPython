<template>
  <div class="entireHome">
    <div class="windows">
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
    </div>
    <div class="recordHistory">
      <record-history />
    </div>
  </div>
</template>

<script>
import SampleLibrary from "../components/FileViewer.vue";
import RecordHistory from "../components/RecordHistory.vue";
import SettingsComponent from "../components/Settings.vue";

export default {
  name: "HomeComponent",
  components: {
    SampleLibrary,
    SettingsComponent,
    RecordHistory,
  },
  data: () => ({
    tab: null,
  }),
};
</script>

<style scoped>

.entireHome {
  display: flex;
  width: 100%;
}

.windows {
  width: 70%;
}

.recordHistory {
  width: 30%;
  height: 100%;
}

</style>

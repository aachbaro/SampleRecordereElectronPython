<template>
  <v-col>
    <settings-librararies-list />
    <backward-recording />
  </v-col>
</template>

<script>
import SettingsLibrarariesList from "../components/Settings_Librararies.vue";
import BackwardRecording from "../components/Settings_BackwardRecording.vue"

export default {
  name: "SettingsComponent",
  components: {
    SettingsLibrarariesList,
    BackwardRecording,
  },
};
</script>

<style scoped>
.backward-recording {
  padding: 8px;
  border-radius: 8px;
  outline: 1px solid #ccc;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.recording-time-selector {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.recording-time-selector v-icon {
  margin-right: 10px;
}

svg {
  width:25px;
  height: 25px;
}

</style>

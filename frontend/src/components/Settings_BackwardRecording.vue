<template>
  <div class="backward-recording">
    <div class="icon-label">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="icon">
        <path
          d="M11 8H13V14H11V8M15 1H9V3H15V1M12 20C8.13 20 5 16.87 5 13S8.13 6 12 6C15.54 6 18.45 8.62 18.93 12.03C19.65 12.08 20.34 12.23 21 12.5C20.87 10.57 20.16 8.81 19.03 7.39L20.45 5.97C20 5.46 19.55 5 19.04 4.56L17.62 6C16.07 4.74 14.12 4 12 4C7.03 4 3 8.03 3 13S7.03 22 12 22C12.34 22 12.67 22 13 21.94C12.63 21.35 12.35 20.69 12.18 20C12.12 20 12.06 20 12 20M22 18.5V14.5L20.83 15.67C20.11 14.95 19.11 14.5 18 14.5C15.79 14.5 14 16.29 14 18.5S15.79 22.5 18 22.5C19.68 22.5 21.12 21.47 21.71 20H20C19.54 20.61 18.82 21 18 21C16.62 21 15.5 19.88 15.5 18.5S16.62 16 18 16C18.69 16 19.32 16.28 19.77 16.73L18 18.5H22Z"
        />
      </svg>
      <span>Backward recording</span>
    </div>
    <div class="recording-time-selector">
      <v-text-field
        v-model="new_bac_rec_time"
        label="Max recording time (seconds)"
        type="number"
        :min="0"
        :max="20"
        :disabled="!bac_rec_enabled"
        :class="{ disabled: !bac_rec_enabled }"
        outlined
      ></v-text-field>
      <v-btn icon v-if="bac_rec_time != new_bac_rec_time" @click="modifyBacRecSettings"
        ><v-icon size="23">mdi-check</v-icon>
      </v-btn>
    </div>
    <v-switch v-model="new_bac_rec_state" @change="modifyBacRecSettings" />
  </div>
</template>

<script>
export default {
  name: "BackwardRecording",
  data() {
    return {
      new_bac_rec_state: false,
      new_bac_rec_time: 0,
    };
  },
  computed: {
    bac_rec_enabled() {
      return this.$store.state.bac_rec_enabled;
    },
    bac_rec_time() {
      return this.$store.state.bac_rec_time;
    },
  },
  methods: {
    modifyBacRecSettings() {
      console.log("toggle", this.new_bac_rec_state);
      this.$store.dispatch("modifyBackwardRecordingInfos", {
        bac_rec_enabled: this.new_bac_rec_state,
        bac_rec_time: this.new_bac_rec_time,
      });
    },
  },
  created() {
    this.$store.dispatch("fetchBackwardRecordingInfos").then(
      () => {
        this.new_bac_rec_state = this.$store.state.bac_rec_enabled;
        this.new_bac_rec_time = this.$store.state.bac_rec_time;
      },
      (error) => {
        console.error(error);
      }
    );
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

svg {
  width: 25px;
  height: 25px;
}

.icon-label {
  display: flex;
  align-items: center;
}

.icon-label span {
  margin-left: 8px;
}

.v-text-field.disabled {
  color: #353b48;
}
</style>

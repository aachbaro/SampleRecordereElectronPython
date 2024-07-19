<template>
  <div class="widget">
      <div class="btnWrap">
        <v-btn
          icon
          size="20"
          :class="{ recording: isRecording }"
          @click="startRecording"
        >
          <v-icon size="16">mdi-microphone</v-icon>
        </v-btn>

        <v-btn icon size="20" class="folder-button">
          <v-icon size="16">mdi-folder</v-icon>
        </v-btn>
      </div>
      <div class="dragzone" :class="{ hidden: hover }">
        <v-icon size="23">mdi-drag-vertical</v-icon>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RecordWidget",
  data() {
    return {
      isRecording: false
    };
  },
  methods: {
    startRecording() {
      console.log("Recording button pressed");
      axios
        .post("http://127.0.0.1:5000/recordButtonClicked")
        .then((response) => {
          console.log("Record Button clicked");
          this.isRecording = response.data;
          this.$emit("file-uploaded");
        })
        .catch((error) => {
          console.error("Error managing record state", error);
        });
    },
  },
};
</script>

<style scoped>

.widget {
  display:flex;
  align-content: center;
  align-items: center;
  justify-items: center;
  /* justify-content: center */
}

.btnWrap {
  display: flex;
  align-content: center;
  align-items: center;
  /* justify-items: center; */
  /* justify-content: center; */
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: solid;
  border-width: 1px;
  border-color: white;
  opacity: 70%;
  transition: width 0.5s ease-in-out;
  overflow: hidden;
  /* outline: 1px solid red; */
}

.btnWrap:hover {
  width: 72px;
}

.btnWrap:hover + .dragzone {
  opacity: 0;
}

.btnWrap:hover .folder-button {
  opacity: 100%;
}

.btnWrap button {
  margin: 7px;
  background-color: white !important;
}

.btnWrap button:hover {
  background-color: #aaa !important;
}

.recording {
  color: red !important;
}

.btnWrap .folder-button {
  opacity: 0%;
  transition: opacity 1s ease-in;
}

.dragzone {
  display:flex;
  align-content: center;
  align-items: center;
  justify-content: center;
  justify-items: center;
  width: 20px;
  height: 40px;
  /* background-color: #aaa !important; */
  color: white;
  -webkit-app-region: drag;
  opacity: 50%;
  transition: opacity 1s;
}

.dragzone.hidden {
  opacity: 0;
}

</style>

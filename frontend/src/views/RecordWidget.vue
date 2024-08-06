<template>
  <div class="widget">
    <div class="firstLine">
      <div :class="['btnWrap', { 'blue-border': bac_rec_enabled }]">
        <v-btn
          icon
          size="20"
          :class="{ recording: isRecording }"
          @wheel="changeBacRecTime"
          @click="startRecording"
        >
          <v-icon size="16" v-if="!bac_rec_enabled || selected_bac_rec_time == 0">mdi-microphone</v-icon>
          <span
            class="show_bac_rec_time"
            v-if="bac_rec_enabled && selected_bac_rec_time != 0"
            >{{ selected_bac_rec_time }}s</span
          >
        </v-btn>
        <div class="folder-button" @wheel="changeLibraryPath">
          <div class="icon-wrapper" @click="showDirName">
            <v-icon size="24" class="folder-icon">mdi-folder</v-icon>
            <p class="folder-number">{{ selected_library_path }}</p>
          </div>
        </div>
      </div>
      <div class="dragzone">
        <v-icon size="23">mdi-drag-vertical</v-icon>
      </div>
    </div>
    <div v-if="show_dir_name" class="libraryName">
      <span>{{ libraries_names[selected_library_path] }}</span>
      {{ bac_rec_time }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RecordWidget",
  data() {
    return {
      selected_library_path: 0,
      isRecording: false,
      show_dir_name: false,
      selected_bac_rec_time: 0,
    };
  },
  computed: {
    libraries_paths() {
      return this.$store.state.libraries_paths;
    },
    libraries_names() {
      return this.$store.state.libraries_names;
    },
    bac_rec_enabled() {
      return this.$store.state.bac_rec_enabled;
    },
    bac_rec_time() {
      return this.$store.state.bac_rec_time;
    },
  },
  methods: {
    startRecording() {
      console.log("Recording button pressed");
      axios
        .post("http://127.0.0.1:5000/recordButtonClicked", {
          path: this.libraries_paths[this.selected_library_path],
          retroTime: this.selected_bac_rec_time
        })
        .then((response) => {
          console.log("Record Button clicked");
          this.isRecording = response.data;
          this.$emit("file-uploaded");
        })
        .catch((error) => {
          console.error("Error managing record state", error);
        });
    },

    changeLibraryPath(event) {
      if (event.deltaY > 0) {
        this.selected_library_path =
          (this.selected_library_path + 1) % this.libraries_paths.length;
      } else {
        this.selected_library_path =
          (this.selected_library_path - 1 + this.libraries_paths.length) %
          this.libraries_paths.length;
      }
    },
    changeBacRecTime(event) {
      if (event.deltaY > 0) {
        this.selected_bac_rec_time =
          Math.min((this.selected_bac_rec_time + 1), this.bac_rec_time)
      } else {
        this.selected_bac_rec_time =
          Math.max((this.selected_bac_rec_time - 1), 0)
      }
    },

    showDirName(event) {
      event;
      this.show_dir_name = !this.show_dir_name;
      window.ipcRenderer.send(
        this.show_dir_name ? "start-resize" : "end-resize",
        "Message simple depuis SelectFolderPath"
      );
    },
  },
  mounted() {
    this.$store.dispatch("fetchLibrariesPaths");
    this.$store.dispatch("fetchBackwardRecordingInfos");

    window.ipcRenderer.receive("libraries-updated", () => {
      console.log("receiving libraries-updadted");
      this.$store.dispatch("fetchLibrariesPaths");
    });

    window.ipcRenderer.receive("bac_rec-updated", () => {
      console.log("receiving bac_rec-updadted");
      this.$store.dispatch("fetchBackwardRecordingInfos");
    });
  },
};
</script>

<style scoped>
.firstLine {
  display: flex;
  align-content: center;
  align-items: center;
  justify-items: center;
}

.btnWrap {
  display: flex;
  align-content: center;
  align-items: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: solid;
  border-width: 1px;
  border-color: white;
  opacity: 70%;
  transition: width 0.3s ease-in-out;
  overflow: hidden;
}

.btnWrap:hover {
  width: 80px;
}

.btnWrap:hover .icon-wrapper {
  display: block;
}

.btnWrap.expanded {
  width: 200px;
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

.folder-button {
  position: relative; /* Ensure that the text is positioned relative to the button */
  width: 25px;
  height: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-wrapper {
  display: none;
  position: relative; /* Position text over icon */
  width: 100%;
  height: 100%;
}

.folder-icon {
  position: absolute; /* Position the icon */
  width: 30px;
  height: 30px;
  color: white;
}

.folder-button:hover .folder-icon {
  color: #aaa;
}

.folder-number:hover .folder-icon {
  color: #aaa;
}

.folder-number {
  position: absolute; /* Position the number over the icon */
  top: 51%;
  left: 50%;
  transform: translate(-50%, -50%); /* Center the text */
  color: black;
  font-size: 14px;
  font-weight: 500;
  z-index: 0; /* Ensure the number is above the icon */
  cursor: pointer;
}

.libraryindicator {
  background-color: white !important;
  /* position: absolute; */
}

.dragzone {
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: center;
  justify-items: center;
  width: 20px;
  height: 40px;
  color: white;
  -webkit-app-region: drag;
  opacity: 50%;
  transition: opacity 1s;
}

.dragzone.hidden {
  opacity: 0;
}

.libraryName {
  color: #aaa;
  font-size: 11px;
  justify-content: start;
}

.show_bac_rec_time {
  font-size: 13px;
  font-weight: 550;
}

.blue-border {
  border-color: #feca57 !important;
  border-color: #1dd1a1 !important;
}
</style>

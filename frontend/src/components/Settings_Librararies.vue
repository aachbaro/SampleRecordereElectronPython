<template>
  <div class="card">
    <div class="header" @click="toggleList">
      <div>
        <v-icon>mdi-folder-outline</v-icon>
        <span class="header-title"> Sample Libraries</span>
      </div>
      <v-icon class="toggleLibraryList">
        {{ showList ? "mdi-chevron-up" : "mdi-chevron-down" }}
      </v-icon>
    </div>
    <v-divider v-if="showList" class="divider"></v-divider>

    <div class="LibrariesItems" v-if="showList">
      <v-list></v-list>
    </div>
    <v-divider v-if="showList" class="divider"></v-divider>
    <div class="addLibrary" v-if="showList" @click="selectDirectory">
      <v-icon size="23">mdi-folder-plus-outline</v-icon>
      <p>Add Sample Library</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SettingsLibrariesList",
  data: () => ({
    showList: false,
  }),
  methods: {
    selectDirectory() {
      console.log("select-folder-path");
      window.ipcRenderer.send(
        "select-folder",
        "Message simple depuis SelectFolderPath"
      );
    },

    toggleList() {
      this.showList = !this.showList;
    },
  },
  mounted() {
    window.ipcRenderer.receive("select-folder", (filePaths) => {
      console.log("Dossiers sélectionnés :", filePaths);
      this.$emit("directorySelected", filePaths);

      axios
        .post("http://127.0.0.1:5000/selectSaveFolder", filePaths)
        .then((response) => {
          console.log("Folder selected successfully");
          console.log(response);
        })
        .catch((error) => {
          console.error("Error selecting folder", error);
        });
    });
  },
};
</script>

<style scoped>
.card {
  /* background-color: #eee !important; */
  padding: 8px;
  border-radius: 8px;
  outline: 1px solid #ccc;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 8px 0;
}

.header-title {
  font-size: 1rem;
  margin-left: 10px;
}

.header:hover .toggleLibraryList {
  background-color: #ddd !important;
}

.toggleLibraryList {
  cursor: pointer;
  border-radius: 4px;
  padding: 5px;
}

.divider {
  margin: 8px 0;
}

.LibrariesItems {
  margin: 16px 0;
}

.addLibrary {
  display: flex;
  align-items: center;
  margin-top: 16px;
  cursor: pointer;
  color: #3f51b5; /* Accent color */
}

.addLibrary v-icon {
  margin-right: 8px;
}
</style>

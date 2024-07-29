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
    <!-- <v-divider v-if="showList" class="divider"></v-divider> -->

    <div class="LibrariesItems" v-if="showList">
      <div
        v-for="(path, index) in libraries_paths"
        :key="index"
        class="library-card"
      >
        {{ libraries_names[index] }}
        <button icon size="20" @click="removeLibrary(index)" small>
          <v-icon size="18">mdi-delete</v-icon>
        </button>
      </div>
    </div>
    <!-- <v-divider v-if="showList" class="divider"></v-divider> -->
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
    showList: true,
    libraries_paths: [],
    libraries_names: [],
  }),
  methods: {
    selectDirectory() {
      console.log("select-folder-path");
      window.ipcRenderer.send(
        "select-folder",
        "Message simple depuis SelectFolderPath"
      );
    },

    fetchLibrariesPaths() {
      axios
        .get("http://127.0.0.1:5000/getLibrariesPaths")
        .then((response) => {
          this.libraries_paths = response.data;
          this.libraries_names = this.libraries_paths.map((path) =>
            path.split("\\").pop()
          );
          this.libraries_names = this.libraries_names.map((path) =>
            path.split("/").pop()
          );
          console.log("Libraries Paths:", this.libraries_paths);
          console.log("library names:", this.libraries_names);
        })
        .catch((error) => {
          console.error("Error fetching libraries paths", error);
        });
    }, 

    removeLibrary(index) {
      axios
        .post("http://127.0.0.1:5000/removeLibraryPath", {
          path: this.libraries_paths[index],
        })
        .then((response) => {
          console.log("Sending remove library request for: ", this.libraries_paths[index]);
          console.log(response);
          this.fetchLibrariesPaths();
        }) 
        .catch((error) => {
          console.error("Error removing library path", error);
        });
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
          this.fetchLibrariesPaths();
        })
        .catch((error) => {
          console.error("Error selecting folder", error);
        });
    });

    this.fetchLibrariesPaths();
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
  padding: 10px;
}

.addLibrary {
  display: flex;
  align-items: center;
  /* margin-top: 16px; */
  cursor: pointer;
  margin-left: 20px;
  margin-bottom: 10px;
  color: #3f51b5; /* Accent color */
}

.addLibrary p {
  margin-left: 10px;
}

.library-card {
  display: flex;
  justify-content: space-between;
  border-radius: 3px;
  width: 100%;
  padding: 10px;

  border: solid;
  border-width: 1px;
  border-color: #aaa;
  margin-bottom: 10px;
}
</style>

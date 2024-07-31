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

    <div class="LibrariesItems" v-if="showList">
      <div
        v-for="(path, index) in libraries_paths"
        :key="index"
        class="library-card"
      >
        {{ libraries_names[index] }}
        <button icon size="20" @click="removeLib(index)" small>
          <v-icon size="18">mdi-delete</v-icon>
        </button>
      </div>
    </div>

    <div class="addLibrary" v-if="showList" @click="selectDirectory">
      <v-icon size="23">mdi-folder-plus-outline</v-icon>
      <p>Add Sample Library</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsLibrariesList",
  data: () => ({
    showList: true,
  }),
  computed: {
    libraries_paths() {
      return this.$store.state.libraries_paths;
    },
    libraries_names() {
      return this.$store.state.libraries_names;
    },
  },

  methods: {
    selectDirectory() {
      console.log("select-folder-path");
      window.ipcRenderer.send("select-folder-path", "");
    },

    removeLib(index) {
      console.log("remove library:", this.libraries_paths[index])
      this.$store.dispatch("removeLibraryPath", this.libraries_paths[index]);
    },

    toggleList() {
      this.showList = !this.showList;
    },
  },
  mounted() {
    this.$store.dispatch("fetchLibrariesPaths");

    window.ipcRenderer.receive("select-folder", (filePaths) => {
      console.log("Dossiers sélectionnés :", filePaths);
      this.$store.dispatch("addLibraryPath", filePaths);
    });

    // window.ipcRenderer.receive("libraries-updated", () => {
    //   console.log("receiving libraries-updadted")
    //   this.$store.dispatch("fetchLibrariesPaths");
    // });
  },
};
</script>

<style scoped>
.card {
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

.LibrariesItems {
  padding: 10px;
}

.addLibrary {
  display: flex;
  align-items: center;
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
  border: solid 1px #aaa;
  margin-bottom: 10px;
}
</style>

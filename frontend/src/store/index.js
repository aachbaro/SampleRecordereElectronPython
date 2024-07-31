import axios from "axios";
import { createStore } from "vuex";

const store = createStore({
  state: {
    libraries_paths: [],
    libraries_names: [],
  },

  actions: {
    fetchLibrariesPaths({ commit }) {
      axios
        .get("http://127.0.0.1:5000/getLibrariesPaths")
        .then((response) => {
          const libraries_paths = response.data;
          const libraries_names = libraries_paths.map((path) =>
            path.split("\\").pop().split("/").pop()
          );
          commit("setLibraries", { libraries_paths, libraries_names });
          console.log("Libraries Paths:", libraries_paths);
          console.log("Library Names:", libraries_names);
        })
        .catch((error) => {
          console.error("Error fetching libraries paths", error);
        });
    },

    addLibraryPath({ dispatch }, filePaths) {
      axios
        .post("http://127.0.0.1:5000/selectSaveFolder", filePaths)
        .then((response) => {
          console.log("Folder selected successfully");
          console.log(response);
          dispatch("fetchLibrariesPaths");
          window.ipcRenderer.send("update-libraries");
        })
        .catch((error) => {
          console.error("Error selecting folder", error);
        });
    },

    removeLibraryPath({ dispatch }, filePaths) {
      axios
        .post("http://127.0.0.1:5000/removeLibraryPath", filePaths)
        .then((response) => {
          console.log("Sending remove library request for: ", filePaths);
          console.log(response);
          dispatch("fetchLibrariesPaths");
          window.ipcRenderer.send("update-libraries");
        })
        .catch((error) => {
          console.error("Error removing library path", error);
        });
    },
  },

  mutations: {
    setLibraries(state, { libraries_paths, libraries_names }) {
      console.log("Commiting setLibraries");
      state.libraries_paths = libraries_paths;
      state.libraries_names = libraries_names;
    },
  },
});

export default store;

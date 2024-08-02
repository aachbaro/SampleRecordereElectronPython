import axios from "axios";
import { createStore } from "vuex";

const store = createStore({
  state: {
    libraries_paths: [],
    libraries_names: [],
    bac_rec_enabled: false,
    bac_rec_time: 1,
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

    fetchBackwardRecordingInfos({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get("http://127.0.0.1:5000/getBacRecInfos").then(
          (response) => {
            console.log(response);
            const { bac_rec_enabled, bac_rec_time } = response.data;
            console.log({ bac_rec_enabled, bac_rec_time });
            commit("setBackwardRecordingInfos", {
              bac_rec_enabled,
              bac_rec_time,
            });
            resolve(response);
          },
          (error) => {
            reject(error);
          }
        );
      });
    },

    modifyBackwardRecordingInfos({ dispatch }, payload) {
      axios
        .post(
          "http://127.0.0.1:5000/modifyBackRecording",
          {
            // bac_rec_enabled: payload.bac_rec_enabled,
            // bac_rec_time: payload.new_bac_rec_time,
            payload,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          console.log(response);
          dispatch("fetchBackwardRecordingInfos");
          window.ipcRenderer.send("update-bac_rec");
        })
        .catch((error) => {
          console.error("Error activating backward Recording", error);
        });
    },
  },

  mutations: {
    setLibraries(state, { libraries_paths, libraries_names }) {
      console.log("Commiting setLibraries");
      state.libraries_paths = libraries_paths;
      state.libraries_names = libraries_names;
    },
    setBackwardRecordingInfos(state, { bac_rec_enabled, bac_rec_time }) {
      console.log("Commiting bacRec infos");
      state.bac_rec_enabled = bac_rec_enabled;
      state.bac_rec_time = bac_rec_time;
    },
  },
});

export default store;

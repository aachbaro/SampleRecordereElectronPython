// libraries.js

// import axios from "axios";

const state = {
  count:
  // libraries_paths: [],
  // libraries_names: [],
};

const getters = {
  // getLibrariesPaths(state) {
  //   return state.libraries_paths;
  // },
  // getLibrariesNames(state) {
  //   return state.libraries_names;
  // },
};

const actions = {
  // async fetchLibrariesPaths({ commit }) {
  //   try {
  //     console.log("fetchLibraryPaths from store");
  //     const response = await axios.get(
  //       "http://127.0.0.1:5000/getLibrariesPaths"
  //     );
  //     const libraries_paths = response.data;
  //     const libraries_names = libraries_paths.map((path) =>
  //       path.split("\\").pop().split("/").pop()
  //     );
  //     commit("setLibraries", { libraries_paths, libraries_names });
  //   } catch (error) {
  //     console.error("Error fetching libraries paths", error);
  //   }
  // },

  // async removeLibrary({ dispatch }, path) {
  //   try {
  //     console.log("Remove libraries path from store")
  //     await axios.post("http://127.0.0.1:5000/removeLibraryPath", { path });
  //     await dispatch("fetchLibrariesPaths"); // Update the store
  //   } catch (error) {
  //     console.error("Error removing library path", error);
  //   }
  // },
};

const mutations = {
  // setLibraries(state, { libraries_paths, libraries_names }) {
  //   state.libraries_paths = libraries_paths;
  //   state.libraries_names = libraries_names;
  // },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};

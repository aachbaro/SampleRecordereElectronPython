<template>
  <v-container>
    <div class="NotifWrapper">
      Record History
      <div v-for="sample in notifications" :key="sample.filename">
        <SampleNotif
          :date="sample.date"
          :filename="sample.filename"
          :length="sample.length"
          @delete-sample="handleDeleteSample"
          @rename-sample="handleRenameSample"
        />
      </div>
    </div>
  </v-container>
</template>

<script>
import SampleNotif from "./SampleNotif.vue";
import axios from "axios";

export default {
  name: "RecordHistory",
  components: {
    SampleNotif,
  },
  computed: {
    notifications() {
      return this.$store.state.notifications;
    },
  },
  methods: {
    async handleDeleteSample(filename) {
      try {
        // Envoie de la requête DELETE à l'API Flask
        const response = await axios.delete("http://127.0.0.1:5000/deleteAudio", {
          params: {
            filePath: filename,
          },
        });

        // Mise à jour de l'état des notifications après suppression
        this.$store.commit("setSampleHistory", response.data);
      } catch (error) {
        console.error("Erreur lors de la suppression du fichier:", error);
      }
    },
    // handleRenameSample({ oldFilename, newFilename }) {
    //   // Implémente ta logique pour renommer le fichier ici
    // },
  },
  mounted() {
    this.$store.dispatch("fetchSampleHistory");

    window.ipcRenderer.receive("update-notifications", (recordData) => {
      console.log("RecordHistory: receiving add notif");
      this.$store.dispatch("addNotification", recordData);
    });
  },
};
</script>

<style scoped>
.NotifWrapper {
  height: 100%;
  border-radius: 10px;
  border: solid;
  border-width: 1px;
  border-color: black;
}
</style>

<template>
  <v-container>
    <div class="sample-detail-card">
      <h3 class="sample-title">{{ sampleName }}</h3>
      <br />
      in {{ directoryName }}/ <br />
      {{ formattedDate }} <br />
      {{ length }}s
      <div class="buttonWrapper">
        <button icon @click="togglePlay">
          <v-icon>{{ isPlaying ? "mdi-pause" : "mdi-play" }}</v-icon>
        </button>
        <button icon @click="deleteSample">
          <v-icon>mdi-delete</v-icon>
        </button>
        <button icon @click="renameSample">
          <v-icon>mdi-pencil</v-icon>
        </button>
      </div>
      <!-- Utilisation de la route Flask pour l'URL du fichier audio -->
      <audio ref="audioPlayer" :src="audioUrl" @ended="onAudioEnded"></audio>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "SampleNotif",
  props: {
    date: {
      type: String,
      required: true,
    },
    filename: {
      type: String,
      required: true,
    },
    length: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      isPlaying: false,
      audioBlobUrl: null,
    };
  },
  computed: {
    formattedDate() {
      const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
      };
      return new Date(this.date).toLocaleDateString(undefined, options);
    },
    sampleName() {
      return this.filename.split(/[/\\]/).pop();
    },
    directoryName() {
      const parts = this.filename.split(/[/\\]/);
      return parts[parts.length - 2];
    },
    directoryPath() {
      const parts = this.filename.split(/[/\\]/);
      parts.pop();
      return parts.join("/") + "/";
    },
  },
  methods: {
    async togglePlay() {
      const audio = this.$refs.audioPlayer;

      if (!this.audioBlobUrl && !this.isPlaying) {
        try {
          const response = await axios.get("http://127.0.0.1:5000/audio", {
            params: {
              directoryPath: this.directoryPath,
              filename: this.sampleName,
            },
            responseType: "blob", // important pour recevoir le fichier sous forme de blob
          });

          // Création d'une URL temporaire pour le Blob
          this.audioBlobUrl = URL.createObjectURL(response.data);
          audio.src = this.audioBlobUrl;
          audio.play();
          this.isPlaying = true;
        } catch (error) {
          console.error("Erreur lors de la récupération de l'audio:", error);
        }
      } else if (this.isPlaying) {
        audio.pause();
        this.isPlaying = false;
      } else {
        audio.play();
        this.isPlaying = true;
      }
    },
    onAudioEnded() {
      this.isPlaying = false;
    },
    deleteSample() {
      if (confirm("Are you sure you want to delete this sample?")) {
        this.$emit("delete-sample", this.filename);
      }
    },
    renameSample() {
      const newFilename = prompt("Enter new filename:", this.sampleName);
      if (newFilename && newFilename !== this.sampleName) {
        this.$emit("rename-sample", {
          oldFilename: this.filename,
          newFilename,
        });
      }
    },
  },
};
</script>

<style scoped>
.sample-detail-card {
  border-radius: 10px;
  border: solid;
  border-width: 1px;
  border-color: black;
}
.sample-title {
  font-size: 10px;
  font-weight: bold;
}
.buttonWrapper {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}
</style>

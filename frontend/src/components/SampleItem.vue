<!-- <template>
    <v-card class="mx-auto my-2" max-width="400" color="grey darken-4">
      <v-card-title>{{ sample.name }}</v-card-title>
      <v-card-subtitle>{{ sample.description }}</v-card-subtitle>
      <v-card-actions>
        <v-btn text @click="playSample">Play</v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script>
  export default {
    name: 'SampleItem',
    props: {
      sample: {
        type: Object,
        required: true
      }
    },
    methods: {
      playSample() {
        // Logic to play the sample
        console.log(`Playing sample: ${this.sample.name}`);
      }
    }
  }
  </script>
  
  <style scoped>
  .v-card {
    width: 100%;
  }
  </style> -->

  <template>
    <div>
        <v-card width="100%" color="#f5cb5c">
            <v-row>
                <v-col>
                    <p>{{ sample.name }}</p>
                </v-col>
                <v-col>
                    <p>{{ sample.duration }}</p>
                </v-col>
                <v-col>
                    <v-btn @click="playSample">
                 <!-- <v-icon>mdi-play</v-icon> -->
                <v-img
                :src="require('../assets/playIcon.png')"
                height="24"
                width="24"
                contain
                />
          </v-btn>
                </v-col>
                <v-col>
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                </v-col>
            </v-row>
        </v-card>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SampleItem',
    props: {
      sample: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  
  <!-- <style scoped>
  p {
    margin: 0;
    color: white;
  }
  </style> -->
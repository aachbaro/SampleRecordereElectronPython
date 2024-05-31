// frontend/main.js

import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Importe Vue Router
import vuetify from './plugins/vuetify';
import { loadFonts } from './plugins/webfontloader';

loadFonts();

createApp(App)
  .use(router) // Utilise Vue Router
  .use(vuetify)
  .mount('#app');

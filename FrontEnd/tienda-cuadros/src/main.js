
import { createApp } from 'vue'
import App from './App.vue'


// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import { createRouter, createWebHistory } from 'vue-router'
import cargarCuadros from './components/cargarCuadros.vue'
import iniciarSesion from './components/iniciarSesion.vue'

const routes = [
  { path: '/cargarCuadros', component: cargarCuadros },
  { path: '/iniciarSesion', component: iniciarSesion }
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes // short for `routes: routes`
})

const app = createApp(App)
app.use(router)
//app.http.headers.common['Access-Control-Allow-Origin'] = '*'
app.mount("#app")
import Vue from "vue";
import VueRouter from "vue-router";
import CargarCuadros from "@/components/CargarCuadros.vue";
import iniciarSesion from "@/components/iniciarSesion.vue";

Vue.use(VueRouter);

const routes = [
  { path: "/", component: CargarCuadros },
  { path: "/Iniciar", component: iniciarSesion },
];

const router = new VueRouter({
  routes,
});

export default router;

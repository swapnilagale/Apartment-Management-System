import { createApp } from "vue";
import App from "./App.vue";
import ApartmentDetail from "./components/pages/ApartmentDetail.vue";
import ApartmentUpdate from "./components/pages/ApartmentUpdate.vue";
import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/pages/HomePage.vue";
import ApartmentList from "./components/pages/ApartmentList.vue";
import AboutPage from "./components/pages/AboutPage.vue";
import AddNewApartment from "./components/pages/AddNewApartment.vue";
import BuildingPage from "./components/pages/BuildingPage.vue";
import ApartmentType from "./components/pages/ApartmentTypePage.vue";


const routes = [
  {
    path: "/",
    component: HomePage,
  },
  {
    path: "/apartment-list",
    component: ApartmentList,
  },
  {
    path: "/apartment-detail/:id",
    component: ApartmentDetail,
  },
  {
    path: "/apartment-update/:id",
    component: ApartmentUpdate,
  },
  {
    path: "/add-new-apartment",
    component: AddNewApartment,
  },
  {
    path: "/apartment-type",
    component: ApartmentType,
  },
  {
    path: "/building",
    component: BuildingPage,
  },
  {
    path: "/about",
    component: AboutPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
  linkActiveClass: "active",
});

const app = createApp(App);
app.use(router);
app.mount("#app");

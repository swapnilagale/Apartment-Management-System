<template>
  <div class="container">
    <div></div>
    <div class="row">
      <div class="col-sm-3" v-for="apt in apartments" :key="apt.id">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">{{ apt.name }}</h3>
            <p class="card-text">
              {{ apt.building.title }}
            </p>

            <router-link
              class="btn btn-dark space"
              :to="`/apartment-detail/${apt.id}`"
              >View Detail</router-link
            >

            <router-link
              class="btn btn-info space"
              :to="`/apartment-update/${apt.id}`"
              >Update</router-link
            >

            <button
              type="button"
              class="btn btn-danger"
              v-on:click="deleteApartment(apt.id)"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ApartmentList",
  data() {
    return {
      apartments: [],
    };
  },
  methods: {
    deleteApartment(id) {
      if (confirm("Do you really want to delete?")) {
        axios
          .delete(`http://127.0.0.1:8001/apartment/` + id)
          .then((response) => {
            console.log(response);
            if (response.status === 204) {
              this.$router.go({ path: "/apartment-list" });
            }
          })
          .catch((error) => {
            //  console.log(error)
            alert(error);
          });
      }
    },
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8001/apartment-list/")
      .then((response) => {
        this.apartments = response.data;
      })
      .catch((error) => {
        //  console.log(error)
        alert(error);
      });
  },
};
</script>

<style scoped>
.card {
  margin-top: 30px;
  margin-bottom: 30px;
}
.btn {
  margin: 10px;
}
</style>

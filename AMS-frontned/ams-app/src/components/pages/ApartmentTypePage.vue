<template>
  <div class="container">
    <h2 class="text-center mt-5">Apartment Type List</h2>

    <!-- Input -->
    <div class="d-flex mt-2">
      <input
        type="text"
        v-model="apartment.type"
        placeholder="Enter Apartment Type"
        class="w-50 form-control center"
      />
      <button class="btn btn-warning rounded-0" @click="createApartmentType()">
        SUBMIT
      </button>
    </div>
    <div class="row">
      <div class="col-sm-3 mt-10" v-for="apt_type in apartmentTypes" :key="apt_type.id">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Apartment Type: {{ apt_type.type }}</h4>

            <button
              type="button"
              class="btn btn-info space"
              v-on:click="updateApartmentType(apt_type.id)"
            >
              Update
            </button>

            <button
              type="button"
              class="btn btn-danger space"
              v-on:click="deleteApartmentType(apt_type.id)"
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
  name: "ApartementTypePage",
  data() {
    return {
      apartmentTypes: [],
      apartment: {
        type: "",
      }
     
    };
  },
  methods: {
    updateApartmentType(id) {
      axios
        .patch(`http://127.0.0.1:8001/apartmentType/` + id + `/`)
        .then((response) => {
          console.log(response);
         
        })
        .catch((error) => {
          //  console.log(error)
          alert(error);
        });
    },

    deleteApartmentType(id) {
      if (confirm("Do you really want to delete?")) {
        axios
          .delete(`http://127.0.0.1:8001/apartmentType/` + id)
          .then((response) => {
            console.log(response);
            if (response.status === 204) {
              this.$router.go({ path: "/apartment-type" });
            }
          })
          .catch((error) => {
            //  console.log(error)
            alert(error);
          });
      }
    },
    createApartmentType() {
      axios
        .post("http://127.0.0.1:8001/apartmentType-list/", this.apartment)

        .then((response) => {
          console.log(response);

          if (response.status === 201) {
            this.$router.go({ path: "/apartment-type" });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8001/apartmentType-list/")
      .then((response) => {
        this.apartmentTypes = response.data;
      })
      .catch((error) => {
        //  console.log(error)
        alert(error);
      });
  },
};
</script>

<style scoped>
.btn {
  margin: 10px;
}
</style>

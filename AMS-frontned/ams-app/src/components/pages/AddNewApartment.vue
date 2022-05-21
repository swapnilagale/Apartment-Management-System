<template>
  <div class="container">
    <form @submit.prevent="createApartment">
      <div class="row mb-3">
        <label class="col-sm-2 col-form-label">Apartment Name</label>
        <div class="col-sm-4">
          <input type="text" class="form-control" v-model="apartment.name" />
        </div>
      </div>
      <div class="row mb-3">
        <label class="col-sm-2 col-form-label">Apartment Description</label>
        <div class="col-sm-4">
          <input
            type="text"
            class="form-control"
            v-model="apartment.description"
          />
        </div>
      </div>

      <div class="row mb-3">
        <label for="apartmenttype" class="col-sm-2 col-form-label"
          >Apartment Type</label
        >
        <div class="col-sm-4">
          <select
            v-model="apartment.apartment_type.type"
            name="apartment_type"
            class="form-select"
          >
            <option value="" disabled selected>Select your option</option>

            <option v-for="apt_type in apartmentTypes" :key="apt_type.id">
              {{ apt_type.type }}
            </option>
          </select>
        </div>
      </div>

      <div class="row mb-3">
        <label for="building" class="col-sm-2 col-form-label">Building</label>
        <div class="col-sm-4">
          <select
            v-model="apartment.building.title"
            name="building"
            class="form-select"
          >
            <option value="" disabled selected>Select your option</option>
            <option v-for="b in buildings" :key="b.id">{{ b.title }}</option>
          </select>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-sm-10 offset-sm-2">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" id="gridCheck1" />
            <label class="form-check-label" for="gridCheck1">
              Is Active ?
            </label>
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Create</button>
    </form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      apartment: {
        name: "",
        description: "",
        apartment_type: {
          type: "",
        },
        building: {
          title: "",
        },
      },
      buildings: [],
      apartmentTypes: [],
    };
  },

  methods: {
    createApartment() {
      axios
        .post("http://127.0.0.1:8001/apartment-list/", this.apartment)
        .then((response) => {
          console.log(this.apartment)
          if(!this.apartment){
            console.log("hmmm")
          }
          if (response.status === 201) {
            this.$router.push({ path: "/apartment-list" });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  beforeCreate() {
    axios
      .get("http://127.0.0.1:8001/building-list/")
      .then((response) => {

        this.buildings = response.data;
      })
      .catch((error) => {
        //  console.log(error)
        alert(error);
      });
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

<template>
  <div>
    <h1>Apartment Name: {{ apartment.name }}</h1>
    <p>Apartment Type: {{ apartment.apartment_type.type }}</p>
    <p>Building: {{ apartment.building.title }}</p>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      apartment: "",
      id: "",
    };
  },
  created() {
    this.id = this.$route.params.id;
    axios
      .get(`http://127.0.0.1:8001/apartment/${this.id}/`)
      .then((response) => {
        console.log(response.data);
        this.apartment = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

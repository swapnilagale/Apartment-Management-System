<template>
   <h1>Dashboard</h1>
  <div class="container">
    <div class="row">
      <div class="col-sm-4">
        <div class="card" style="height: 10rem">
          <div class="card-body">
            <h3 class="card-title text-center pt-3">Total Number Of Apartments</h3>
            <h3 class="card-text text-center">{{totalApartment}}</h3>
          </div>
        </div>
      </div>

      <div class="col-sm-4">
        <div class="card" style="height: 10rem">
          <div class="card-body">
            <h3 class="card-title text-center pt-3">Total Number Of Buildings</h3>
            <h3 class="card-text text-center">{{totalBuilding}}</h3>
          </div>
        </div>
      </div>

      <div class="col-sm-4">
        <div class="card" style="height: 10rem">
          <div class="card-body">
            <h3 class="card-title text-center pt-3">Locked Apartment</h3>
            <h3 class="card-text text-center">{{totalApartment}}</h3>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name:"HomePage",
  data(){
    return{
        totalApartment:'',
        totalBuilding:'',

    }
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8001/apartment-list/")
      .then((response) => {
       this.totalApartment=response.data.length;
      })
      .catch((error) => {
        //  console.log(error)
        alert(error);
      });

    axios
      .get("http://127.0.0.1:8001/building-list/")
      .then((response) => {
        this.totalBuilding = response.data.length;
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
  background-color:#764AF1;
  color:white;
}
</style>

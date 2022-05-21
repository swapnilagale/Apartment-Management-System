<template>
  <div class="container">
    <h2 class="text-center mt-5">Building List</h2>

    <!-- Input -->
    <div class="d-flex mt-2">
      <input
        type="text"
        v-model="building.title"
        placeholder="Enter Building title"
        class="w-50 form-control center"
      />
      <button class="btn btn-warning rounded-0" @click="createBuilding()">
        SUBMIT
      </button>
    </div>
    <div class="row">
      <div class="col-sm-3 mt-10" v-for="bldng in buildings" :key="bldng.id">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Building Name : {{ bldng.title }}</h4>

            <button
              type="button"
              class="btn btn-info space"
              v-on:click="updateBuilding(bldng.id)"
            >
              Update
            </button>

            <button
              type="button"
              class="btn btn-danger space"
              v-on:click="deleteBuilding(bldng.id)"
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
  name: "BuildingPage",
  data() {
    return {
      buildings: [],
      building: {
        title: "",
      },
      editedBuilding: {
        title: null,
      },
      title: "",
    };
  },
  methods: {
    updateBuilding(id) {
      axios
        .patch(`http://127.0.0.1:8001/building/` + id + `/`)
        .then((response) => {
          console.log(response);
          this.building.title = this.buildings[id - 2].title;
          this.editedBuilding.title = id;
        })
        .catch((error) => {
          //  console.log(error)
          alert(error);
        });
    },

    deleteBuilding(id) {
      if (confirm("Do you really want to delete?")) {
        axios
          .delete(`http://127.0.0.1:8001/building/` + id)
          .then((response) => {
            console.log(response);
            if (response.status === 204) {
              this.$router.go({ path: "/building" });
            }
          })
          .catch((error) => {
            //  console.log(error)
            alert(error);
          });
      }
    },
    createBuilding() {
      axios
        .post("http://127.0.0.1:8001/building-list/", this.building)

        .then((response) => {
          console.log(response);

          if (response.status === 201) {
            this.$router.go({ path: "/building" });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8001/building-list/")
      .then((response) => {
        this.buildings = response.data;
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

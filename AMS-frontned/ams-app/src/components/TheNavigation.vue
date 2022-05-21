<template>
  <div class="d-flex" id="wrapper">
    <!-- Sidebar -->
    <div class="bg-white" id="sidebar-wrapper">
      <div
        class="sidebar-heading text-center py-4 primary-text fs-4 fw-bold text-uppercase border-bottom"
      >
        <i class="fas fa-user-secret me-2"></i>Apartment Management System
      </div>

      <div class="list-group list-group-flush my-3">
        <router-link
          to="/"
          class="list-group-item bg-transparent second-text fw-bold"
          >Home</router-link
        >
        <router-link
          to="/apartment-list"
          class="list-group-item bg-transparent second-text fw-bold"
          >Apartment List</router-link
        >
        <router-link
          to="/add-new-apartment"
          class="list-group-item bg-transparent second-text fw-bold"
          >Add New Apartment</router-link
        >
        <router-link
          to="/apartment-type"
          class="list-group-item bg-transparent second-text fw-bold"
          >Apartment Type</router-link
        >
        <router-link
          to="/building"
          class="list-group-item bg-transparent second-text fw-bold"
          >Building</router-link
        >
        <router-link
          to="/about"
          class="list-group-item bg-transparent second-text fw-bold"
          >About</router-link
        >
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">
      <nav
        class="navbar navbar-expand-lg navbar-light bg-transparent py-4 px-4"
      >
        <div class="d-flex align-items-center">
          <i
            class="fas fa-align-left primary-text fs-4 me-3"
            id="menu-toggle"
          ></i>
        </div>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle second-text fw-bold"
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <i class="fas fa-user me-2"></i>John Doe
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Profile</a></li>
                <li><a class="dropdown-item" href="#">Settings</a></li>
                <li><a class="dropdown-item" href="#">Logout</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </nav>

      <div class="container-fluid px-4">
        <div class="row g-3 my-2">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>
<style>
:root {
  --main-bg-color: #009d63;
  --main-text-color: #009d63;
  --second-text-color: #bbbec5;
  --second-bg-color: #c1efde;
}

.primary-text {
  color: var(--main-text-color);
}

.second-text {
  color: var(--second-text-color);
}

.primary-bg {
  background-color: var(--main-bg-color);
}

.secondary-bg {
  background-color: var(--second-bg-color);
}

.rounded-full {
  border-radius: 100%;
}

#wrapper {
  overflow-x: hidden;
  background-image: linear-gradient(
    to right,
    #baf3d7,
    #c2f5de,
    #cbf7e4,
    #d4f8ea,
    #ddfaef
  );
}

#sidebar-wrapper {
  min-height: 100vh;
  margin-left: -15rem;
  -webkit-transition: margin 0.25s ease-out;
  -moz-transition: margin 0.25s ease-out;
  -o-transition: margin 0.25s ease-out;
  transition: margin 0.25s ease-out;
}

#sidebar-wrapper .sidebar-heading {
  padding: 0.875rem 1.25rem;
  font-size: 1.2rem;
}

#sidebar-wrapper .list-group {
  width: 15rem;
}

#page-content-wrapper {
  min-width: 100vw;
}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}

#menu-toggle {
  cursor: pointer;
}

a.list-group-item {
  border: none;
  padding: 20px 30px;
}

a.list-group-item.active {
  background-color: transparent;
  color: var(--main-text-color);
  font-weight: bold;
  border: none;
}

@media (min-width: 768px) {
  #sidebar-wrapper {
    margin-left: 0;
  }

  #page-content-wrapper {
    min-width: 0;
    width: 100%;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: -15rem;
  }
}
</style>

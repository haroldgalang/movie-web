<template>
  <div class="container mt-4">
    <h1 class="mb-4">My Movie Collection</h1>

    <SearchBar @search="handleSearch" />

    <button
      class="btn btn-success mb-3"
      data-bs-toggle="modal"
      data-bs-target="#movieFormModal"
      @click="openForm()"
    >
      Add New Movie
    </button>

    <MovieList ref="movieList" @edit-movie="editMovie" />

    <!-- Modal -->
    <div
      class="modal fade"
      id="movieFormModal"
      tabindex="-1"
      aria-labelledby="movieFormModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="movieFormModalLabel">
              {{ selectedMovie ? "Edit Movie" : "Add New Movie" }}
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
              @click="clearForm"
            ></button>
          </div>
          <div class="modal-body">
            <MovieForm
              :movieToEdit="selectedMovie"
              :onMovieAdded="refreshMovies"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import MovieForm from "./components/MovieForm.vue";
import MovieList from "./components/MovieList.vue";
import SearchBar from "./components/SearchBar.vue";

const selectedMovie = ref(null);
const movieList = ref(null);

const refreshMovies = () => {
  movieList.value.fetchMovies();
  clearForm();
};

const openForm = () => {
  selectedMovie.value = null;
};

const editMovie = (movie) => {
  selectedMovie.value = { ...movie };
  const modal = new bootstrap.Modal(document.getElementById("movieFormModal"));
  modal.show();
};

const clearForm = () => {
  selectedMovie.value = null;
};
</script>

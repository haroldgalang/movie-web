<template>
  <div class="container mt-4">
    <h1 class="mb-4">My Movie Collection</h1>
    <MovieForm :movieToEdit="selectedMovie" :onMovieAdded="refreshMovies" />
    <MovieList @edit-movie="selectMovieToEdit" ref="movieList" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import MovieForm from "./components/MovieForm.vue";
import MovieList from "./components/MovieList.vue";

const selectedMovie = ref(null);
const movieList = ref(null);

const selectMovieToEdit = (movie) => {
  selectedMovie.value = movie;
};

const refreshMovies = () => {
  movieList.value.fetchMovies();
  selectedMovie.value = null; // Reset form after add/update
};
</script>

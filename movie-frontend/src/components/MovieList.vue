<template>
  <div class="row">
    <MovieCard
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      :onDelete="fetchMovies"
      :onEdit="editMovie"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, defineEmits } from "vue";
import axios from "axios";
import MovieCard from "./MovieCard.vue";

const emit = defineEmits(["edit-movie"]);

const movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/movies/");
    movies.value = response.data;
  } catch (error) {
    console.error("Failed to fetch movies:", error);
  }
};

const editMovie = (movie) => {
  emit("edit-movie", movie);
};

onMounted(fetchMovies);
defineExpose({ fetchMovies });
</script>

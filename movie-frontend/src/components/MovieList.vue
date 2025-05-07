<template>
  <div class="row">
    <MovieCard
      v-for="movie in filteredMovies"
      :key="movie.id"
      :movie="movie"
      :onDelete="fetchMovies"
      :onEdit="editMovie"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, defineEmits } from "vue";
import axios from "axios";
import MovieCard from "./MovieCard.vue";

const emit = defineEmits(["edit-movie"]);
const movies = ref([]);
const searchQuery = ref("");

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

const filteredMovies = computed(() => {
  return movies.value.filter((movie) => {
    const query = searchQuery.value.toLowerCase();
    return (
      movie.title.toLowerCase().includes(query) ||
      movie.genre.toLowerCase().includes(query)
    );
  });
});

const setSearchQuery = (query) => {
  searchQuery.value = query;
};

onMounted(fetchMovies);
defineExpose({ fetchMovies, setSearchQuery });
</script>

<template>
  <div class="card p-3 mb-4">
    <h3>{{ isEdit ? "Edit Movie" : "Add New Movie" }}</h3>
    <form @submit.prevent="handleSubmit">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input
          v-model="movie.title"
          type="text"
          placeholder="Title"
          id="title"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="genre" class="form-label">Genre</label>
        <input
          v-model="movie.genre"
          type="text"
          placeholder="Genre"
          id="genre"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="director" class="form-label">Director</label>
        <input
          v-model="movie.director"
          type="text"
          placeholder="Director"
          id="director"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="release_year" class="form-label">Release Year</label>
        <input
          v-model.number="movie.release_year"
          type="number"
          placeholder="Release Year"
          id="release_year"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="rating" class="form-label">Rating</label>
        <input
          v-model.number="movie.rating"
          type="number"
          step="0.1"
          min="0"
          max="10"
          placeholder="Rating"
          id="rating"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="poster" class="form-label">Poster URL</label>
        <input
          v-model="movie.poster"
          type="text"
          id="poster"
          class="form-control"
        />
      </div>

      <button type="submit" class="btn btn-primary">
        {{ isEdit ? "Update Movie" : "Add Movie" }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, watch, reactive } from "vue";
import axios from "axios";

const props = defineProps({
  movieToEdit: Object,
  onMovieAdded: Function,
});

const movie = reactive({
  title: "",
  genre: "",
  director: "",
  release_year: null,
  rating: null,
  poster: "",
});

const isEdit = ref(false);

watch(
  () => props.movieToEdit,
  (newMovie) => {
    if (newMovie) {
      Object.assign(movie, newMovie); // ✅ Correct use of reactive
      isEdit.value = true;
    }
  }
);

const handleSubmit = async () => {
  try {
    console.log("Payload being sent:", { ...movie }); // ✅ Debug line
    const response = await axios.post(
      "http://127.0.0.1:8000/api/movies/",
      movie
    );
    console.log("Success:", response.data);
    props.onMovieAdded();
    resetForm();
  } catch (error) {
    console.error("Error adding movie:", error.response?.data || error.message);
  }
};

const resetForm = () => {
  Object.assign(movie, {
    title: "",
    genre: "",
    director: "",
    release_year: null,
    rating: null,
    poster: "",
  });
  isEdit.value = false;
};
</script>

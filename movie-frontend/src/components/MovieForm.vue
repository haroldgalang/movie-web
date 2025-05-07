<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div class="mb-3">
        <label class="form-label">Title</label>
        <input
          v-model="movie.title"
          type="text"
          class="form-control"
          :class="{ 'is-invalid': errors.title }"
        />
        <div class="invalid-feedback">{{ errors.title }}</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Genre</label>
        <input
          v-model="movie.genre"
          type="text"
          class="form-control"
          :class="{ 'is-invalid': errors.genre }"
        />
        <div class="invalid-feedback">{{ errors.genre }}</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Director</label>
        <input
          v-model="movie.director"
          type="text"
          class="form-control"
          :class="{ 'is-invalid': errors.director }"
        />
        <div class="invalid-feedback">{{ errors.director }}</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Release Year</label>
        <input
          v-model="movie.release_year"
          type="number"
          class="form-control"
          :class="{ 'is-invalid': errors.release_year }"
        />
        <div class="invalid-feedback">{{ errors.release_year }}</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Rating</label>
        <input
          v-model="movie.rating"
          type="number"
          step="0.1"
          min="0"
          max="10"
          class="form-control"
          :class="{ 'is-invalid': errors.rating }"
        />
        <div class="invalid-feedback">{{ errors.rating }}</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Poster URL</label>
        <input
          v-model="movie.poster"
          type="text"
          class="form-control"
          :class="{ 'is-invalid': errors.poster }"
        />
        <div class="invalid-feedback">{{ errors.poster }}</div>
      </div>

      <button type="submit" class="btn btn-primary">
        {{ isEdit ? "Update Movie" : "Add Movie" }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from "vue";
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

const errors = reactive({
  title: "",
  genre: "",
  director: "",
  release_year: "",
  rating: "",
  poster: "",
});

const isEdit = ref(false);

watch(
  () => props.movieToEdit,
  (newMovie) => {
    if (newMovie) {
      Object.assign(movie, newMovie);
      isEdit.value = true;
    }
  }
);

const validateForm = () => {
  let valid = true;
  Object.keys(errors).forEach((key) => (errors[key] = ""));

  if (!movie.title) {
    errors.title = "Title is required.";
    valid = false;
  }
  if (!movie.genre) {
    errors.genre = "Genre is required.";
    valid = false;
  }
  if (!movie.director) {
    errors.director = "Director is required.";
    valid = false;
  }
  if (!movie.release_year) {
    errors.release_year = "Release year is required.";
    valid = false;
  }
  if (movie.rating === null || movie.rating < 0 || movie.rating > 10) {
    errors.rating = "Rating must be between 0 and 10.";
    valid = false;
  }

  return valid;
};

const handleSubmit = async () => {
  if (!validateForm()) return;

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/movies/",
      movie
    );
    props.onMovieAdded();
    resetForm();
    // Close modal manually
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("movieFormModal")
    );
    modal.hide();
  } catch (error) {
    console.error("Submission error:", error.response?.data || error.message);
  }
};

const resetForm = () => {
  movie.title = "";
  movie.genre = "";
  movie.director = "";
  movie.release_year = null;
  movie.rating = null;
  movie.poster = "";
  isEdit.value = false;
};
</script>

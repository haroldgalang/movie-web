<template>
  <div class="col-md-4 mb-4">
    <div class="card h-100">
      <img
        :src="movie.poster"
        class="card-img-top"
        alt="Poster"
        style="height: 300px; object-fit: cover"
      />
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <strong></strong> {{ movie.release_year }}<br />
        <p class="card-text">
          <strong></strong> {{ movie.genre }}<br /><br />
          <strong>Director:</strong> {{ movie.director }}<br />
          <strong>Rating:</strong> {{ movie.rating }}
        </p>
        <button class="btn btn-sm btn-danger me-2" @click="deleteMovie">
          Delete
        </button>
        <button class="btn btn-sm btn-secondary" @click="editMovie">
          Edit
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";

const props = defineProps({
  movie: Object,
  onDelete: Function,
  onEdit: Function,
});

const deleteMovie = async () => {
  if (confirm(`Are you sure you want to delete "${props.movie.title}"?`)) {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/movies/${props.movie.id}/`);
      props.onDelete(); // Refresh list
    } catch (error) {
      console.error("Failed to delete movie:", error);
    }
  }
};

const editMovie = () => {
  props.onEdit(props.movie); // Send movie to MovieForm
};
</script>

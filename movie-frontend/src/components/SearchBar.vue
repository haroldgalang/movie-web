<template>
  <div class="mb-4">
    <input
      v-model="query"
      @input="handleSearch"
      type="text"
      placeholder="Search by title or genre"
      class="form-control"
    />
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const emit = defineEmits(["search"]);
const query = ref("");

const handleSearch = () => {
  emit("search", query.value);
};
</script>

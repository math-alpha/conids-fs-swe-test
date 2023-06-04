<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<script lang="ts">
import { defineComponent } from "vue"

export default defineComponent({
  name: "App",
});
</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">Purchase Management</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/purchases" class="nav-link">Purchases</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/add-purchases" class="nav-link">Add</router-link>
        </li>
      </div>
    </nav>
  </div>

  <div class="container mt-5">
    <RouterView />
  </div>
</template>

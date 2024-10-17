<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="nav-1-line">
      <RouterLink to="/">ЛОГО</RouterLink>
      <span>{{ currentTime }}</span>
      <span>{{ currentDate }}</span>
      <RouterLink to="/authorization">АВТОРИЗ</RouterLink>
    </nav>
    <nav class="nav-2-line">
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
      <RouterLink to="/some-page">сэйм паге</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<script>
export default {
  data() {
    return {
      currentDate: "",
      currentTime: "",
    };
  },
  mounted() {
    // Получение текущей даты и времени при загрузке компонента
    this.getCurrentDateTime();
    
    // Обновление времени каждую секунду
    setInterval(() => {
      this.getCurrentDateTime();
    }, 1000);
  },
  methods: {
    getCurrentDateTime() {
      const now = new Date();

      this.currentDate = now.toLocaleDateString();
      this.currentTime = now.toLocaleTimeString();
      localStorage.setItem('currentDay', JSON.stringify({ day: now.getDate() }));
    },
  },
};
</script>

<style>
.nav-1-line {
  display: flex;
  justify-content: space-between;
}

.nav-2-line {
  display: flex;
  justify-content: space-between;
}
</style>
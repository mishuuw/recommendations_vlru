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
      <RouterLink to="/posters">Афиша</RouterLink>
      <RouterLink to="/some-page">Отключения</RouterLink>
      <RouterLink to="/some-page">Недвижимость</RouterLink>
      <RouterLink to="/some-page">Справочник</RouterLink>
      <RouterLink to="/some-page">Базы отдыха</RouterLink>
      <RouterLink to="/some-page">Фарпост</RouterLink>
      <RouterLink to="/some-page">Врачи</RouterLink>
      <RouterLink to="/some-page">ТВ-программа</RouterLink>
      <RouterLink to="/some-page">Транспорт</RouterLink>
      <RouterLink to="/some-page">Дром</RouterLink>
      <RouterLink to="/some-page">ЛовиКупон</RouterLink>
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

    localStorage.setItem('currentDay', JSON.stringify({ day: this.getDayNumber() }));
  },
  methods: {
    getCurrentDateTime() {
      const now = new Date();

      this.currentDate = now.toLocaleDateString();
      this.currentTime = now.toLocaleTimeString();
    },
    getDayNumber() {
      const startDate = new Date(2024, 0, 1); // 1 января 2024 года
      const selectedDate = new Date();
      
      // Разница в миллисекундах
      const diffInTime = selectedDate.getTime() - startDate.getTime();
      
      // Конвертируем миллисекунды в дни
      const diffInDays = Math.floor(diffInTime / (1000 * 3600 * 24));

      // Возвращаем результат, начиная с 1
      return diffInDays >= 0 ? diffInDays + 1 : 'Дата до 1 января 2024 года';
    }
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
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="nav-1-line">
      <RouterLink to="/"><img class="logo">
        <img src="@/assets/logo.png" width="150px">
      </RouterLink>
      <div class="time">
        <span>{{ currentDate }}</span>
        <span>{{ currentTime }}</span>
      </div>
      <RouterLink to="/authorization" v-if="!checkAuthorize">
        <img src="@/assets/account.png" class="acc">
      </RouterLink>
      <RouterLink to="/profile" v-else>
        <img src="@/assets/account.png" class="acc">
      </RouterLink>
    </nav>
    
    <nav class="nav-small" v-if="visibleMainMenu">
      <div class="nav-2-line-1">
        <RouterLink to="/posters">Афиша</RouterLink>
        <RouterLink to="/some-page">Отключения</RouterLink>
        <RouterLink to="/some-page">Недвижимость</RouterLink>
        <RouterLink to="/some-page">Справочник</RouterLink>
        <RouterLink to="/some-page">Базы отдыха</RouterLink>
        <RouterLink to="/some-page">Фарпост</RouterLink>
      </div>
      <div class="nav-2-line-2">
        <RouterLink to="/some-page">Врачи</RouterLink>
        <RouterLink to="/some-page">ТВ-программа</RouterLink>
        <RouterLink to="/some-page">Транспорт</RouterLink>
        <RouterLink to="/some-page">Дром</RouterLink>
        <RouterLink to="/some-page">ЛовиКупон</RouterLink>
      </div>
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
      checkAuthorize: false,
      visibleMainMenu: true,
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
    
    if (localStorage.getItem('authorizedUser')) {
      this.checkAuthorize = true
    } else {
      this.checkAuthorize = false
    }
    
    this.visibleMainMenu = localStorage.getItem('visibleMainMenu')
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
.acc {
  width: 40px;
  margin-top: 25px;
}

.nav-1-line {
  display: flex;
  justify-content: space-between;
}

.nav-2-line-1 {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.nav-2-line-2 {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 15px;
}

.nav-small {
  display: flex;
  flex-direction: column;
  margin: 50px auto 0;
  width: 90%;
} 

.nav-small a {
  background: #FF8A47;
  box-shadow: -4px 4px 4px rgba(18, 33, 70, 0.25);
  border-radius: 12px;
  padding: 5px;
  color: white;
  text-decoration: none;
  width: 100px;
  text-align: center;
}

.time {
  display: flex;
  flex-direction: column;
  /* color: #56A5E2; */
}

header {
  background-image: url('@/assets/header-bg.png');
  height: 200px;
  padding: 10px 30px;
}

body {
  margin: 0;
}

</style>
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import FooterView from './components/views/FooterView.vue';
</script>

<template>
  <header>
    <nav class="nav-1-line">
      <RouterLink to="/"><img class="logo">
        <img src="@/assets/logo.png" width="150px">
      </RouterLink>
      <!-- <div class="time">
        <span>{{ currentDate }}</span>
        <span>{{ currentTime }}</span>
      </div> -->
      <RouterLink to="/authorization" v-if="!checkAuthorize">
        <img src="@/assets/account.png" class="acc">
      </RouterLink>
      <RouterLink to="/profile" v-else>
        <img src="@/assets/account.png" class="acc">
      </RouterLink>
    </nav>
    
    <!-- <nav class="nav-small">
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
    </nav> -->
  </header>

  <div class="main">
    <RouterView />
  </div>

  <FooterView />
</template>

<script>
export default {
  components: {
    FooterView
  },
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
    
    // this.visibleMainMenu = localStorage.getItem('visibleMainMenu')
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
.main {
  min-height: 500px;
}

.acc {
  width: 40px;
  margin-top: 25px;
}

.nav-1-line {
  display: flex;
  justify-content: space-between;
}

/* .nav-2-line-1 {
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
} */

.time {
  display: flex;
  flex-direction: column;
  /* color: #56A5E2; */
}

header {
  background-image: url('@/assets/header-bg.png');
  height: 80px;
  padding: 10px 30px;
  margin-bottom: 20px;
}

body {
  margin: 0;
  background-color: rgb(248, 248, 248);
  font-family: "Arial";
}

.authorization-form {
  background: rgba(239, 239, 239, 0.55);
  box-shadow: 0px 13px 24.5px rgba(55, 89, 175, 0.25);
  border-radius: 12px;
  padding: 10px;
  max-width: 400px;
  margin: 0 auto;
  /* margin-top: 20px; */
}

.form-group input {
  background: #C1D3F4;
  border-radius: 12px;  
  border: 1px;
}

.authorization-form button {
  background: #FF9354;
  border-radius: 12px;
  padding: 6px;
  border: 1px;
}


.button-group {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin-bottom: 10px;
}

.selected {
  background: #EDEDED;
  box-shadow: 0px 4px 24.5px rgba(0, 0, 0, 0.25);
  border-radius: 12px;
}

.button-group a {
  display: block;
  width: 40%;
  padding: 5px;
  text-align: center;
  text-decoration: none;
  color: #FF8A47;
}

.submit {
  display: flex;
  justify-content: center;
  color: white;
}
</style>
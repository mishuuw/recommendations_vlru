<template>
  <div class="columns">
    <div class="c1">
      <div class="wrapper-left text-blue">
        <h5>Погода во Владивостоке</h5>
        <div class="wrapper-text">
          <div class="wrapper-img">
            <img src="@/assets/rainy.png" height="25px">
            <img src="@/assets/termo.png" height="30px" width="12px">
            <img src="@/assets/wind.png" height="25px">
          </div>
          <div class="wrapper-info">          
            <p>Пасмурно, сильный дождь</p>
            <p>Днём 9°С, ночью 5°С</p>
            <p>Ветер до 10 м/с, С-СЗ</p>
          </div>
        </div>
      </div>
      <div class="wrapper-left text-orange">
        <h5>Валюта по курсу ЦБ</h5>
        <div class="wrapper-text">
          <div class="wrapper-img">
            <img src="@/assets/dollar.png">
            <img src="@/assets/euro.png">
          </div>
          <div class="wrapper-info">
            <div class="set-margin-money">
              <p>96.59</p>
              <p>104.86</p>
            </div>
          </div>
        </div>
      </div> 
      <div class="wrapper-left text-blue">
        <h5>Вакансии</h5>
        <p>Дворник за 100к</p>
        <p>Таксист зв 10к</p>
      </div>
      <div class="wrapper-left text-orange">
        <h5>Реклама</h5>
        <p>Тут могла быть ваша реклама</p>
      </div>
    </div>
    <div class="c2">
      <div>
        <h2 style="color: #FF8A47; font-size: 50px;">Новости</h2>
        <div class="news-frame">
          <div>
            <h3>Нереальный шторм потопит Владивосток</h3>
            <span>23.10.24 6:00</span>
          </div>
          <p>
            Жители Владивостока, бегите из города, ожидаются цунами, ветер 1000км/ч
          </p>
        </div>
        <div class="recommend">
          <RecommendationsView />
        </div>

        <div class="bases">
          <BasesView />
        </div>
      </div>
    </div>
    <div class="c3">
      <h5 class="h5-first">Информация</h5>
      <ul>
        <li><RouterLink to="/posters">Афиша</RouterLink></li>
        <li><RouterLink to="/some-page">Врачи</RouterLink></li>
        <li><RouterLink to="/some-page">Отключения</RouterLink></li>
        <li><RouterLink to="/some-page">ТВ-программа</RouterLink></li>
        <li><RouterLink to="/some-page">Недвижимость</RouterLink></li>
        <li><RouterLink to="/some-page">Транспорт</RouterLink></li>
        <li><RouterLink to="/some-page">Справочник</RouterLink></li>
        <li><RouterLink to="/some-page">Базы отдыха</RouterLink></li>
      </ul>
      <h5 class="h5-second">Наши сайты</h5>
      <ul>
        <li><a href="https://www.drom.ru/">Дром</a></li>
        <li><a href="https://www.100sp.ru/vladivostok?utm_source=utm_vl.ru&utm_medium=link&utm_campaign=main">Совместные покупки</a></li>
        <li><a href="https://vladivostok.lovikupon.ru/today/?utm_source=vl.ru&utm_medium=left_menu&utm_term=%D0%9B%D0%BE%D0%B2%D0%B8%D0%9A%D1%83%D0%BF%D0%BE%D0%BD">ЛовиКупон</a></li>
        <li><a href="https://www.farpost.ru/vladivostok/">Фарпост</a></li>
      </ul>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import RecommendationsView from './RecommendationsView.vue';
import BasesView from './BasesView.vue';

  export default {
    components: {
      RecommendationsView,
      BasesView
    },
    data() {
      return {
        filter: '',
        recommendEvents: [],
        filteredEvents: [],
        popularEvents: [],
      }
    },
    methods: {
      getFilteredEvents() {
        axios.get('http://localhost:5000/getFiltredEvents', {params: {filter: this.filter}})
        .then((response) => {
          console.log(response);

          this.filteredEvents = JSON.parse(response)
        })
        .catch((error) => {
          console.log(error);
        })
      },

      getPopularEvents() {
        axios.get('http://localhost:5000/getPopularEvents')
        .then((response) => {
          console.log(response);

          this.popularEvents = JSON.parse(response)
        })
        .catch((error) => {
          console.log(error);
        })
      },

      addFavotite(eventID) {
        axios.post('http://localhost:5000/addFavorite', {"userID": localStorage.getItem('authorizedUser').userID, "eventID": eventID}) // поменять параметр
            .then((response) => {
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });
      },
    },
    mounted() {
      this.getPopularEvents()
      // localStorage.setItem('visibleMainMenu', true)
    },  
  };
  </script>
  
<style scoped>
  .text-blue {
    color: #4687FF;
  }

  .text-orange {
    color: #FF9354;
  }

  .columns {
    display: flex;
    flex-direction: row;
    height: 100%;
  }

  .c1 {
    width: 20%;
    /* height: 100%; */
    margin: 10px;
  }
  
  .c1 h5 {
    font-size: 20px;
  }

  .c1 p {
    font-size: 12px;
    margin: 0 0 20px 0;
  }

  .c2 {
    width: 60%;
    /* height: 100%; */
    margin-top: 10px;
  }

  .wrapper-img img {
    margin-bottom: 10px;
  }

  .wrapper-text {
    display: flex;
    flex-direction: row;
  }

  .wrapper-info {
    margin-left: 15px;
  }

  .wrapper-text div {
    display: flex;
    flex-direction: column;
  }

  .wrapper-left {
    display: flex;
    flex-direction: column;
    background: #ECECEC;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 30px;
  }

  .wrapper-left h5 {
    margin: 0 0 10px 0;
  }

  .c3 {
    width: 20%;
    /* height: 100%; */
    margin: 10px;
  }

  .set-margin-money p {
    margin: 8px 0 20px 0
  }

  .c3 li {
    list-style-type: none;
    background: #FF8A47;
    box-shadow: -4px 4px 4px rgba(18, 33, 70, 0.25);
    border-radius: 12px;
    padding: 5px;
    text-align: center;
    margin-bottom: 10px;
  }

  .c3 a {
    color: white;
    text-decoration: none;
  }

  .c3 ul {
    margin: 0;
    padding: 0;
  }

  .c3 h5 {
    font-size: 23px;
    color: #4687FF;
  }

  .h5-first {
    margin: 0px 0 10px 0;
  }

  .h5-second {
    margin: 30px 0 10px 0;
  }

  .c2 {
    background-image: url(@/assets/bg.png);
    background-size: no-repeat;
    background-position: center;
    background-size: cover;
    width: 100%;
    margin: 0 40px;
  }

  .news-frame {
    background-color: #ECECECcf;
    padding: 10px;
    border-radius: 10px;
  }

  .recommend {
    background-color: #ECECECcf;
    padding: 10px;
    border-radius: 10px;
    margin-top: 200px;
  }

  .bases {
    background-color: #ECECECcf;
    padding: 10px;
    border-radius: 10px;
    margin: 50px 0 30px 0;
  }

  .news-frame h3 {
    margin: 0;
  }
</style>
  
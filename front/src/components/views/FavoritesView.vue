<template>
    <div class="events-container">
      <h1>Избранные события</h1>
  
      <div v-if="favoriteEvents.length === 0" class="no-events">
        <p>Нет избранных событий.</p>
      </div>
  
      <div v-else class="events-list">
        <div v-for="event in favoriteEvents" :key="event.id" class="event-card">
          <h3>{{ event.title }}</h3>
          <p>{{ event.description }}</p>
          <p><strong>Дата:</strong> {{ event.date }}</p>
          <button @click="removeFromFavorites(event.id)">Удалить из избранного</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        favoriteEvents: [] // Массив для хранения избранных событий
      };
    },
    mounted() {
      this.loadFavoriteEvents();
    },
    methods: {
      // Загрузка избранных событий из localStorage
      loadFavoriteEvents() {
        // axios.get('http://localhost:5000/getFavoriteList', {
        //         params: {
        //         userID: userID // поменять параметр
        //         }
        //     })
        //     .then(function (response) {
        //         console.log(response);
        //     })
        //     .catch(function (error) {
        //         console.log(error);
        //     })
      },
      // Удаление события из избранного
      removeFromFavorites(eventId) {
        this.favoriteEvents = this.favoriteEvents.filter(event => event.id !== eventId);
        this.saveFavoriteEvents();
      },
      // Сохранение избранных событий в localStorage
      saveFavoriteEvents() {
        localStorage.setItem('favoriteEvents', JSON.stringify(this.favoriteEvents));
      }
    }
  };
  </script>
  
  <style scoped>
  .events-container {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  .no-events {
    text-align: center;
    font-size: 18px;
    color: #999;
  }
  
  .events-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .event-card {
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
  }
  
  .event-card h3 {
    margin: 0;
    margin-bottom: 10px;
  }
  
  .event-card button {
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #e74c3c;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .event-card button:hover {
    background-color: #c0392b;
  }
  </style>
  
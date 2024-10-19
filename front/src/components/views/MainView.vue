<template>
  <div>
    <b3>Интересные события</b3>
    <div>
      <button @click="this.filter = ''; getPopularEvents()">Популярное</button>
      <button @click="this.filter = 'concerts'; getFilteredEvents()">Концерты</button>
      <button @click="this.filter = 'theaters'; getFilteredEvents()">Театры</button>
    </div>
    <div v-if="recommendEvents.length" class="events-list">
        <div v-for="event in recommendEvents" :key="event.id" class="event-item">
            <h3>{{ event.title }}</h3>
            <p><strong>Дата:</strong> {{ event.date.day }} {{ event.date.month }} {{ event.date.year }}</p>
            <p><strong>Время:</strong> {{ event.time }}</p>
            <p><strong>Категория:</strong> {{ event.category }}</p>
        </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        filter: '',
        recommendEvents: []
      }
    },
    methods: {
      getFilteredEvents() {
        axios.get('http://localhost:5000/getFiltredEvents', {params: {filter: this.filter}})
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
      },

      getPopularEvents() {
        axios.get('http://localhost:5000/getPopularEvents')
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
      },

      // addFavotite(eventID) {
      //   axios.post('http://localhost:5000/addFavorite', {"userID": "..", "eventID": eventID}) // поменять параметр
      //       .then((response) => {
      //         console.log(response);
      //       })
      //       .catch((error) => {
      //         console.log(error);
      //       });
      // },
    },
    mounted() {
      this.getPopularEvents()
    },  
  };
  </script>
  
  <style scoped>
  
  </style>
  
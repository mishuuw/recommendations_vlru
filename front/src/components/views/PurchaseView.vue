<template>
    <div class="history-container" v-if="checkAuthorization">
      <h1>История покупок билетов</h1>
  
      <div v-if="purchasedTickets.length === 0" class="no-tickets">
        <p>Нет купленных билетов.</p>
      </div>
  
      <div v-else class="tickets-list">
        <div v-for="ticket in purchasedTickets" :key="ticket.id" class="ticket-card">
          <h3>Событие: {{ ticket.eventTitle }}</h3>
          <p><strong>Дата события:</strong> {{ ticket.eventDate }}</p>
          <p><strong>Количество билетов:</strong> {{ ticket.quantity }}</p>
          <p><strong>Дата покупки:</strong> {{ formatPurchaseDate(ticket.purchaseDate) }}</p>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Сначала пройдите авторизацию</p>
      <RouterLink to="/authorization">Авторизация</RouterLink>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        purchasedTickets: [], // Массив для хранения истории покупок билетов
        checkAuthorization: false
      };
    },
    mounted() {
      // localStorage.setItem('visibleMainMenu', false)

      if (localStorage.getItem('authorizedUser')) {
        this.checkAuthorization = true
        this.loadPurchasedTickets();
      }
    },
    methods: {
      // Загрузка купленных билетов из localStorage
      loadPurchasedTickets() {
        axios.get('http://localhost:5000/getPurchaseList', {
                params: {
                userID: localStorage.getItem('authorizedUser').userID
                }
            })
            .then(function (response) {
                console.log(response);

                this.purchasedTickets = JSON.parse(response)
            })
            .catch(function (error) {
                console.log(error);
            })
      },
      // Форматирование даты покупки
      formatPurchaseDate(date) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(date).toLocaleDateString('ru-RU', options);
      }
    }
  };
  </script>
  
  <style scoped>
  .history-container {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  .no-tickets {
    text-align: center;
    font-size: 18px;
    color: #999;
  }
  
  .tickets-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .ticket-card {
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
  }
  
  .ticket-card h3 {
    margin: 0;
    margin-bottom: 10px;
  }
  
  .ticket-card p {
    margin: 5px 0;
  }
  </style>
  
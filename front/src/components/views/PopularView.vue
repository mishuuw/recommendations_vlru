<template>
    <div class="event-list">
      <h3 style="color: #FF8A47; font-size: 20px;">Популярные события</h3>
      <div class="events-container">
        <!-- Кнопка для прокрутки влево -->
        <button @click="prevPage" :disabled="currentPage === 1" class="nav-button">
          &#9664;
        </button>
  
        <!-- Карточки событий -->
        <div class="events-wrapper">
          <div class="event-card" v-for="(event, index) in paginatedEvents" :key="index">
            <img src="@/assets/zatik.png" alt="Event image" class="event-image" style="opacity: 70%;"/>
            <div class="event-info">
              <h3>{{ event.title }}</h3>
              <p>{{ event.date }} - {{ event.time }}</p>
              <p style="margin-bottom: 0;">{{ event.location }}</p>
              <!-- Кнопка "Добавить в избранное" внизу -->
              <button @click="toggleFavorite(event)" class="favorite-button">
                <span v-if="event.isFavorite">&#10084;</span>
                <span v-else>&#9825;</span>
              </button>
            </div>
          </div>
        </div>
  
        <!-- Кнопка для прокрутки вправо -->
        <button @click="nextPage" :disabled="currentPage === totalPages" class="nav-button">
          &#9654;
        </button>
      </div>
  
      <!-- Индикаторы страниц -->
      <div class="pagination-indicator">
        Страница {{ currentPage }} из {{ totalPages }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "PopularEventsView",
    data() {
      return {
        events: [
          { title: "Concert of the Year", date: "2024-10-15", time: "07:00 PM", location: "Main Stadium", image: "concert.jpg" },
          { title: "Film Festival", date: "2024-10-20", time: "05:00 PM", location: "Cinema City", image: "festival.jpg" },
          { title: "Tech Conference", date: "2024-10-25", time: "09:00 AM", location: "Tech Hub", image: "tech.jpg" },
          { title: "Art Exhibition", date: "2024-10-30", time: "01:00 PM", location: "Modern Art Gallery", image: "art.jpg" },
          { title: "Food Carnival", date: "2024-11-01", time: "11:00 AM", location: "Central Park", image: "food.jpg" },
          { title: "Stand-up Comedy", date: "2024-11-05", time: "08:00 PM", location: "Comedy Club", image: "comedy.jpg" },
          { title: "Marathon", date: "2024-11-10", time: "06:00 AM", location: "City Square", image: "marathon.jpg" },
          { title: "Book Fair", date: "2024-11-15", time: "10:00 AM", location: "Exhibition Center", image: "book.jpg" },
        ],
        currentPage: 1,
        perPage: 4,
      };
    },
    computed: {
      totalPages() {
        return Math.ceil(this.events.length / this.perPage);
      },
      paginatedEvents() {
        const start = (this.currentPage - 1) * this.perPage;
        const end = start + this.perPage;
        return this.events.slice(start, end);
      },
    },
    methods: {
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      },
      prevPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },
      toggleFavorite(event) {
        event.isFavorite = !event.isFavorite;
      },
    },
  };
  </script>
  
  <style scoped>
  .event-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 0 30px 0;
  }
  
  .events-container {
    display: flex;
    align-items: center;
  }
  
  .events-wrapper {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
  }
  
  .event-card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    position: relative;
  }
  
  .event-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .event-info {
    margin-top: 10px;
  }
  
  .favorite-button {
    background: none;
    border: none;
    font-size: 32px;
    cursor: pointer;
    color: #FF8A47;
    transition: transform 0.3s;
  }
  
  .favorite-button:hover {
    transform: scale(1.2);
  }
  
  .nav-button {
    font-size: 24px;
    background: none;
    border: none;
    cursor: pointer;
  }
  
  .pagination-indicator {
    margin-top: 20px;
    font-size: 18px;
  }
  </style>
  
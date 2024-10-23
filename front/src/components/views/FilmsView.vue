<template>
  <div class="event-list">
    <h3 style="color: #FF8A47; font-size: 20px;">Популярные фильмы</h3>
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
  name: "RecommendationsView",
  data() {
    return {
      events: [
      { title: "Event 1", date: "2024-10-01", time: "10:00 AM", location: "Location 1", image: "event1.jpg" },
          { title: "Event 2", date: "2024-10-02", time: "11:00 AM", location: "Location 2", image: "event2.jpg" },
          { title: "Event 3", date: "2024-10-03", time: "12:00 PM", location: "Location 3", image: "event3.jpg" },
          { title: "Event 4", date: "2024-10-04", time: "01:00 PM", location: "Location 4", image: "event4.jpg" },
          { title: "Event 5", date: "2024-10-05", time: "02:00 PM", location: "Location 5", image: "event5.jpg" },
          { title: "Event 6", date: "2024-10-06", time: "03:00 PM", location: "Location 6", image: "event6.jpg" },
          { title: "Event 7", date: "2024-10-07", time: "04:00 PM", location: "Location 7", image: "event7.jpg" },
          { title: "Event 8", date: "2024-10-08", time: "05:00 PM", location: "Location 8", image: "event8.jpg" },
          { title: "Event 9", date: "2024-10-09", time: "06:00 PM", location: "Location 9", image: "event9.jpg" },
          { title: "Event 10", date: "2024-10-10", time: "07:00 PM", location: "Location 10", image: "event10.jpg" },
          { title: "Event 11", date: "2024-10-11", time: "08:00 PM", location: "Location 11", image: "event11.jpg" },
          { title: "Event 12", date: "2024-10-12", time: "09:00 PM", location: "Location 12", image: "event12.jpg" },
          { title: "Event 13", date: "2024-10-13", time: "10:00 PM", location: "Location 13", image: "event13.jpg" },
          { title: "Event 14", date: "2024-10-14", time: "11:00 PM", location: "Location 14", image: "event14.jpg" },
          { title: "Event 15", date: "2024-10-15", time: "12:00 AM", location: "Location 15", image: "event15.jpg" },
          { title: "Event 16", date: "2024-10-16", time: "01:00 AM", location: "Location 16", image: "event16.jpg" },
          { title: "Event 17", date: "2024-10-17", time: "02:00 AM", location: "Location 17", image: "event17.jpg" },
          { title: "Event 18", date: "2024-10-18", time: "03:00 AM", location: "Location 18", image: "event18.jpg" },
          { title: "Event 19", date: "2024-10-19", time: "04:00 AM", location: "Location 19", image: "event19.jpg" },
          { title: "Event 20", date: "2024-10-20", time: "05:00 AM", location: "Location 20", image: "event20.jpg" },
          { title: "Event 21", date: "2024-10-21", time: "06:00 AM", location: "Location 21", image: "event21.jpg" },
          { title: "Event 22", date: "2024-10-22", time: "07:00 AM", location: "Location 22", image: "event22.jpg" },
          { title: "Event 23", date: "2024-10-23", time: "08:00 AM", location: "Location 23", image: "event23.jpg" },
          { title: "Event 24", date: "2024-10-24", time: "09:00 AM", location: "Location 24", image: "event24.jpg" },
          { title: "Event 25", date: "2024-10-25", time: "10:00 AM", location: "Location 25", image: "event25.jpg" },
          { title: "Event 26", date: "2024-10-26", time: "11:00 AM", location: "Location 26", image: "event26.jpg" },
          { title: "Event 27", date: "2024-10-27", time: "12:00 PM", location: "Location 27", image: "event27.jpg" },
          { title: "Event 28", date: "2024-10-28", time: "01:00 PM", location: "Location 28", image: "event28.jpg" },
          { title: "Event 29", date: "2024-10-29", time: "02:00 PM", location: "Location 29", image: "event29.jpg" },
          { title: "Event 30", date: "2024-10-30", time: "03:00 PM", location: "Location 30", image: "event30.jpg" },
          { title: "Event 31", date: "2024-10-31", time: "04:00 PM", location: "Location 31", image: "event31.jpg" },
          { title: "Event 32", date: "2024-11-01", time: "05:00 PM", location: "Location 32", image: "event32.jpg" },
          { title: "Event 33", date: "2024-11-02", time: "06:00 PM", location: "Location 33", image: "event33.jpg" },
          { title: "Event 34", date: "2024-11-03", time: "07:00 PM", location: "Location 34", image: "event34.jpg" },
          { title: "Event 35", date: "2024-11-04", time: "08:00 PM", location: "Location 35", image: "event35.jpg" },
          { title: "Event 36", date: "2024-11-05", time: "09:00 PM", location: "Location 36", image: "event36.jpg" },
        // Остальные события...
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
  margin: 30px 0;
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
  /* margin-top: 15px; */
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

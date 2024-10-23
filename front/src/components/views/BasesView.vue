<template>
    <div class="base-list">
      <h3 style="color: #FF8A47;">Базы отдыха</h3>
      <div class="bases-container">
        <!-- Кнопка для прокрутки влево -->
        <button @click="prevPage" :disabled="currentPage === 1" class="nav-button">
          &#9664;
        </button>
  
        <!-- Карточки баз отдыха -->
        <div class="bases-wrapper">
          <div class="base-card" v-for="(base, index) in paginatedBases" :key="index">
            <img src="@/assets/zatik.png" alt="Base image" class="base-image" style="opacity: 70%;"/>
            <div class="base-info">
              <h3>{{ base.name }}</h3>
              <p>{{ base.location }}</p>
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
    data() {
      return {
        bases: [
          { name: "База отдыха 1", location: "Место 1", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 2", location: "Место 2", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 3", location: "Место 3", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 4", location: "Место 4", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 5", location: "Место 5", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 6", location: "Место 6", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 7", location: "Место 7", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 8", location: "Место 8", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 9", location: "Место 9", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 10", location: "Место 10", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 11", location: "Место 11", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 12", location: "Место 12", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 13", location: "Место 13", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 14", location: "Место 14", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 15", location: "Место 15", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 16", location: "Место 16", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 17", location: "Место 17", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 18", location: "Место 18", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 19", location: "Место 19", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 20", location: "Место 20", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 21", location: "Место 21", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 22", location: "Место 22", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 23", location: "Место 23", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 24", location: "Место 24", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 25", location: "Место 25", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 26", location: "Место 26", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 27", location: "Место 27", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 28", location: "Место 28", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 29", location: "Место 29", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 30", location: "Место 30", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 31", location: "Место 31", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 32", location: "Место 32", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 33", location: "Место 33", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 34", location: "Место 34", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 35", location: "Место 35", image: "https://via.placeholder.com/150" },
          { name: "База отдыха 36", location: "Место 36", image: "https://via.placeholder.com/150" },
        ],
        currentPage: 1,
        perPage: 4,
      };
    },
    computed: {
      totalPages() {
        return Math.ceil(this.bases.length / this.perPage);
      },
      paginatedBases() {
        const start = (this.currentPage - 1) * this.perPage;
        const end = start + this.perPage;
        return this.bases.slice(start, end);
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
    },
  };
  </script>
  
  <style scoped>
  .base-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0;
  }
  
  .bases-container {
    display: flex;
    align-items: center;
  }
  
  .bases-wrapper {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
  }
  
  .base-card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    position: relative;
  }
  
  .base-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .base-info {
    margin-top: 10px;
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
  
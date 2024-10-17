<template>
    <div class="event-poster">
      <h2>Афиша</h2>
      <select>
        <option>Владивосток</option>
        <option>Уссурийск</option>
        <option>Находка</option>
      </select>
      <div class="filters">
          <div class="filter-category">
              <label for="category">Фильтр по категории:</label>
              <select v-model="selectedCategory" @change="filterEvents">
                  <option value="">Все</option>
                  <option v-for="category in uniqueCategories" :key="category" :value="category">
                  {{ category }}
                  </option>
              </select>
          </div>

          <div class="filter-coming-days">
              <label>Мероприятия в близжайшие дни:</label>
              <div>
                  <button @click="this.eventDay = ''; filterOff(); filterEvents()">Все</button>
                  <button @click="this.eventDay = this.currentDay; filterOff(); filterEvents(); changeEventDay()">Сегодня</button>
                  <button @click="this.eventDay = this.currentDay + 1; filterOff(); filterEvents(); changeEventDay()">Завтра</button>
                  <button @click="this.eventDay = this.currentDay + 2; filterOff(); filterEvents(); changeEventDay()">Послезавтра</button>
                  <button @click="console.log('Other date')">Другая дата</button>
              </div>
          </div>
      </div>

      <div v-if="filteredEvents.length" class="events-list">
        <div v-for="event in filteredEvents" :key="event.id" class="event-item">
          <h3>{{ event.title }}</h3>
          <p><strong>Date:</strong> {{ event.date.day }} {{ event.date.month }} {{ event.date.year }}</p>
          <p><strong>Time:</strong> {{ event.time }}</p>
          <p><strong>Category:</strong> {{ event.category }}</p>
        </div>
      </div>
  
      <div v-else>
        <p>No events available for the selected category.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        events: [
          {
            id: 1,
            title: "Концерт залупкина",
            date: {
                day: '16',
                month: 'октябрь', 
                year: '2024',
            },
            time: "14:00",
            category: "Концерт",
          },
          {
            id: 2,
            title: "Поход в пизду мамонта",
            date: {
                day: '16',
                month: 'октябрь', 
                year: '2024',
            },
            time: "09:00",
            category: "Поход",
          },
          {
            id: 3,
            title: "Рыбалка у Васильича",
            date: {
                day: '16',
                month: 'октябрь', 
                year: '2024',
            },
            time: "18:00",
            category: "Рыбалка",
          },
          {
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '16',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 5,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '16',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },{
            id: 4,
            title: "Концерт Мэбыбэбы",
            date: {
                day: '17',
                month: 'октябрь', 
                year: '2024',
            },
            time: "19:00",
            category: "Концерт",
          },
        ],
        selectedCategory: "",
        filteredEvents: [],
        currentDay: '',
        eventDay: '',
      };
    },
    computed: {
      uniqueCategories() {
        return [...new Set(this.events.map((event) => event.category))];
      },
    },
    methods: {
      filterOff() {
        this.filteredEvents = this.events
      },
      changeEventDay() {
        if (this.eventDay) {
          this.filteredEvents = this.filteredEvents.filter(
          (event) => event.date.day == this.eventDay 
        )
        }
      },
      filterEvents() {
        if (this.selectedCategory) {
          this.filteredEvents = this.events.filter(
            (event) => event.category === this.selectedCategory
          );
        } else {
          this.filterOff()
        }
      },
    },
    mounted() {
      this.filteredEvents = this.events;
      this.currentDay = JSON.parse(localStorage.getItem('currentDay')).day
    },
  };
  </script>
  
  <style scoped>
  .filters {
    display: flex;
    justify-content: space-between;
  }

  .event-poster {
    min-width: 160px;
    padding: 20px;
  }
  
  .filter-category {
    margin-bottom: 20px;
  }
  
  .events-list {
    display: flex;
    flex-wrap: wrap;
  }
  
  .event-item {
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .event-item h3 {
    margin: 0;
    font-size: 1.5em;
  }
  
  .event-item p {
    margin: 5px 0;
  }
  
  strong {
    font-weight: bold;
  }
  </style>
  
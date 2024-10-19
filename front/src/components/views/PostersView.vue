<template>
    <div class="event-poster">
        <h2>Афиша</h2>
        <select>
            <option>Владивосток</option>
            <option>Уссурийск</option>
            <option>Находка</option>
        </select>

        <div>
            <RouterLink to="/favorites">Избранные события</RouterLink>
            <RouterLink to="/history">История покупок</RouterLink>
        </div>

        <div v-if="recommendEvents.length" class="events-list">
            <b3>Популярное в последнее время</b3>
            <div v-for="event in recommendEvents" :key="event.id" class="event-item">
                <h3>{{ event.title }}</h3>
                <p><strong>Дата:</strong> {{ event.date.day }} {{ event.date.month }} {{ event.date.year }}</p>
                <p><strong>Время:</strong> {{ event.time }}</p>
                <p><strong>Категория:</strong> {{ event.category }}</p>
            </div>
        </div>

        <!-- СДЕЛАТЬ ПРОЛИСТЫВАНИЕ ВПРАВО -->
        
        <div class="filters">
            <div class="filter-category">
                <label for="category">Фильтр по категории:</label>
                <select v-model="filters.type">
                    <option value="">Все</option>
                    <option value="concerts">Концерты</option>
                    <option value="theaters">Театры</option>
                    <option value="hike">Походы</option>
                </select>
            </div>

            <div class="filter-coming-days">
                <label>Мероприятия в близжайшие дни:</label>
                <div>
                    <button @click="filters.date = ''; getFilteredEvents()">Все</button>
                    <button @click="filters.date = currentDay; getFilteredEvents()">Сегодня</button>
                    <button @click="filters.date = currentDay + 1; getFilteredEvents()">Завтра</button>
                    <button @click="filters.date = currentDay + 2; getFilteredEvents()">Послезавтра</button>
                    <button @click="toggleDatePicker" class="btn">
                        {{ showDatePicker ? 'Скрыть' : 'Выбрать дату' }}
                    </button>
                    <div class="container">
                        <!-- Отображаем интерфейс выбора даты -->
                        <div v-if="otherDate.showDatePicker" class="datepicker">
                        <h3>Выберите дату:</h3>
                        <label>
                            День:
                            <select v-model="otherDate.selectedDay">
                            <option v-for="day in otherDate.days" :key="day" :value="day">{{ day }}</option>
                            </select>
                        </label>
                        <label>
                            Месяц:
                            <select v-model="otherDate.selectedMonth">
                            <option v-for="(month, index) in otherDate.months" :key="index" :value="index">{{ month }}</option>
                            </select>
                        </label>
                        <label>
                            Год:
                            <select v-model="otherDate.selectedYear">
                            <option v-for="year in otherDate.years" :key="year" :value="year">{{ year }}</option>
                            </select>
                        </label>
                        <p>Выбранная дата: {{ formattedDate }}</p>
                        <button @click="filters.date = getDayNumber(); getFilteredEvents()">Найти</button>
                        {{ findError }}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div v-if="filteredEvents.length" class="events-list">
                <b3>Популярное в последнее время</b3>
                <div v-for="event in filteredEvents" :key="event.id" class="event-item">
                    <h3>{{ event.title }}</h3>
                    <p><strong>Дата:</strong> {{ event.date.day }} {{ event.date.month }} {{ event.date.year }}</p>
                    <p><strong>Время:</strong> {{ event.time }}</p>
                    <p><strong>Категория:</strong> {{ event.category }}</p>
                </div>
            </div>
        </div>
        <!--  СДЕЛАТЬ ПРОЛИСТЫВАНИЕ ВНИЗ  -->
    </div>

    <div v-if="filmsEvents.length" class="events-list">
            <b3>Кино</b3>
            <div v-for="event in filmsEvents" :key="event.id" class="event-item">
                <h3>{{ event.title }}</h3>
                <p><strong>Дата:</strong> {{ event.date.day }} {{ event.date.month }} {{ event.date.year }}</p>
                <p><strong>Время:</strong> {{ event.time }}</p>
                <p><strong>Категория:</strong> {{ event.category }}</p>
            </div>
        </div>

        <!-- СДЕЛАТЬ ПРОЛИСТЫВАНИЕ ВПРАВО -->

</template>

<!-- ПРИ ПОИСКЕ ДАТЫ, НА КОТОРУЮ НЕТ КОНЦЕРТА ИЛИ КОТОРАЯ ПРОШЛА ВЕРНУТЬ ОШИБКУ -->

<script>
import axios from 'axios'

export default {
    data() {
      return {
        recommendEvents: [],
        filteredEvents: [],
        filmsEvents: [],
        currentDay: '',
        findError: '',
        filters: {
            date: '',
            type: '',
        },
        otherDate: {
            showDatePicker: false,
            selectedDay: 1,
            selectedMonth: 0,
            selectedYear: new Date().getFullYear(),
            days: Array.from({ length: 31 }, (_, i) => i + 1),
            months: [
                'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 
                'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
            ],
            years: Array.from({ length: 101 }, (_, i) => new Date().getFullYear() - i),
        }
      };
    },
    computed: {
        formattedDate() {
            return `${this.otherDate.selectedDay} ${this.otherDate.months[this.otherDate.selectedMonth]} ${this.otherDate.selectedYear}`;
        }
    },
    methods: {
        getFilteredEvents() {
            axios.get('http://localhost:5000/getFiltredEvents', {params: {filters: this.filters}})
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            })
        },
        toggleDatePicker() {
            this.otherDate.showDatePicker = !this.otherDate.showDatePicker;
        },
        getDayNumber() {
            const startDate = new Date(2024, 0, 1); // 1 января 2024 года
            const selectedDate = new Date(this.otherDate.selectedYear, this.otherDate.selectedMonth, this.otherDate.selectedDay);
            
            // Разница в миллисекундах
            const diffInTime = selectedDate.getTime() - startDate.getTime();
            
            // Конвертируем миллисекунды в дни
            const diffInDays = Math.floor(diffInTime / (1000 * 3600 * 24));

            // Возвращаем результат, начиная с 1
            return diffInDays >= 0 ? diffInDays + 1 : 'Дата до 1 января 2024 года';
        },
        // addFavotite(eventID) {
        //     axios.post('http://localhost:5000/addFavorite', {"userID": "..", "eventID": eventID}) // поменять параметр
        //         .then((response) => {
        //         console.log(response);
        //         })
        //         .catch((error) => {
        //         console.log(error);
        //         });
        // },
        mounted() {
            this.filteredEvents = this.events;
            this.currentDay = JSON.parse(localStorage.getItem('currentDay')).day

            axios.get('http://localhost:5000//getFilms')
                .then((response) => {
                console.log(response);
                })
                .catch((error) => {
                console.log(error);
                })

            // axios.get('http://localhost:5000/getRecommendedEvents', {
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
        }
    }
}
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
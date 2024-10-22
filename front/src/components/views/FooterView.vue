<template>
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <h4>Разделы</h4>
          <ul>
            <li>Концерты</li>
            <li>Театры</li>
            <li>Детям</li>
            <li>Стендап</li>
            <li>Спорт</li>
            <li>Городское событие</li>
            <li>Музеи и галереи</li>
            <li>Экскурсии и туры</li>
            <li>Вечеринки</li>
            <li>Впечатления</li>
            <li>Мастер-классы</li>
            <li>Обучение</li>
          </ul>
        </div>
  
        <div class="footer-section">
          <h4>Сайты Владивостока</h4>
          <ul>
            <li>Авто</li>
            <li>Кино</li>
            <li>Недвижимость</li>
            <li>Новости</li>
            <li>Объявления</li>
            <li>Работа</li>
            <li>Справочник компаний</li>
          </ul>
        </div>
  
        <div class="footer-section">
          <h4>Мы в социальных сетях</h4>
          <ul class="social-media">
            <li><a href="#">Facebook</a></li>
            <li><a href="#">Instagram</a></li>
            <li><a href="#">Twitter</a></li>
            <li><a href="#">VK</a></li>
          </ul>
        </div>
  
        <div class="footer-section">
          <h4>Информация</h4>
          <ul>
            <li>Вакансии</li>
            <li>Контакты</li>
            <li>Информационное сотрудничество и продажа билетов на Афише VL.ru</li>
            <li>Правила публикации события на Афише VL.ru</li>
          </ul>
        </div>
      </div>
  
      <div class="footer-bottom">
        <p>
          По вопросам, предложениям или ошибкам пишите на почту 
          <a href="mailto:bilet@vl.ru">bilet@vl.ru</a>
        </p>
        <p>
          © ООО "Примнет". При любом использовании материалов ссылка на 
          <a href="https://vl.ru/AFISHA" target="_blank">VL.ru/AFISHA</a> обязательна.
        </p>
        <p>
          Цитирование в Интернете возможно только при наличии гиперссылки. Все права защищены.
        </p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'FooterComponent',
  };
  </script>
  
  <style scoped>
  .footer {
    background-color: #f8f8f8;
    padding: 40px 20px;
    color: #333;
    font-family: Arial, sans-serif;
    border-top: 1px solid #ddd;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  
  .footer-section {
    flex: 1;
    min-width: 200px;
    margin: 10px;
  }
  
  .footer-section h4 {
    margin-bottom: 15px;
    font-size: 18px;
    color: #FF8A47;
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: 10px;
  }
  
  .footer-section a {
    color: #FF8A47;
    text-decoration: none;
  }
  
  .footer-section a:hover {
    text-decoration: underline;
  }
  
  .footer-bottom {
    text-align: center;
    margin-top: 20px;
  }
  
  .footer-bottom p {
    margin: 5px 0;
  }
  </style>
  
<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-section">
        <h4>Разделы афиши</h4>
        <ul>
          <li><a href="#">Концерты</a></li>
          <li><a href="#">Театры</a></li>
          <li><a href="#">Детям</a></li>
          <li><a href="#">Стендап</a></li>
          <li><a href="#">Спорт</a></li>
          <li><a href="#">Городское событие</a></li>
          <li><a href="#">Музеи и галереи</a></li>
          <li><a href="#">Экскурсии и туры</a></li>
          <li><a href="#">Вечеринки</a></li>
          <li><a href="#">Впечатления</a></li>
          <li><a href="#">Мастер-классы</a></li>
          <li><a href="#">Обучение</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h4>Сайты Владивостока</h4>
        <ul>
          <li><a href="#">Авто</a></li>
          <li><a href="#">Кино</a></li>
          <li><a href="#">Недвижимость</a></li>
          <li><a href="#">Новости</a></li>
          <li><a href="#">Объявления</a></li>
          <li><a href="#">Работа</a></li>
          <li><a href="#">Справочник компаний</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h4>Информация</h4>
        <ul>
          <li><a href="#">Вакансии</a></li>
          <li><a href="#">Контакты</a></li>
          <li><a href="#">Информационное сотрудничество и продажа билетов на Афише VL.ru</a></li>
          <li><a href="#">Правила публикации события на Афише VL.ru</a></li>
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
  color: black;
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

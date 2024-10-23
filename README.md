**Что бы нормально запустить проект требуется:**
1. Скачать весь репозиторий
2. cd front -> npm install -> npm i axios -> npm run serve
3. Запустить master.py 
4. Дождаться инициализации фронта и бека
5. Зайти на локальный сайт http://localhost:8081

**Что бы получить список рекомендаций (по умолчанию выдаются 36шт, сортированные по lambda x: x['views']:**
1. Импортировать файлик с нейронкой 
```python
from neural_network import NeuralNetwork
```
3. Создать экземпляр NeuralNetwork
```python
AI = NeuralNetwork()
```
5. Получить рекомендации используя единственный открытый метод:
```python
recommendations = AI.get_recommendations(user_id) # id - 32 символа
```

recommendations - list из 36 объектов со следующими параметрами:
```python
dict(
  event_id=event_id,
  categories=result.split(';'),
  title=result.split(';')[::-1][0], #в качестве имени главная категория события
  desc='Описание события',
  cost=0, #Цена события
  date=datetime.now().strftime("%d/%m/%Y"),
  time=datetime.now().strftime("%H:%M"),
  location=f'Ул. Пушкина, Д. {random.randint(0,50)}',
  program='Программа мероприятия. Вероятно, должна быть в JSON, но мне лень. затычка.',
  author='Автор события. в VL.RU есть странички у организаторов. затычка. мб ссылку сюда.',
  likes=random.randint(0,100),
  dislikes=random.randint(0,50),
  views=random.randint(0,5000)
)
```

**ВАЖНАЯ ИНФА:**

1. События (их наборы категорий) берутся из dump.db -> Events_to_Categories 
2. Для работы необходимо 2 БД, прилагал в ТГ (велики, лень запариваться с git lfs)
3. В дизайне много затычек. Всё нужное реализовано (идея редизайна, редизайн, рекомендалка соединена с сайтом, при просмотре страницы выдает рекомендации рандомного человека (реки хранятся в кеше 5 минут, потом генерятся заново, при перезагрузке страницы) )


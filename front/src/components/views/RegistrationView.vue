<template>
    <div class="register-form">
      <h2>Регистрация</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Имя пользователя:</label>
          <input
            type="text"
            id="username"
            v-model="form.username"
            @blur="validateUsername"
          />
          <span v-if="errors.username" class="error">{{ errors.username }}</span>
        </div>
  
        <div class="form-group">
          <label for="email">Почта:</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            @blur="validateEmail"
          />
          <span v-if="errors.email" class="error">{{ errors.email }}</span>
        </div>
  
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            @blur="validatePassword"
          />
          <span v-if="errors.password" class="error">{{ errors.password }}</span>
        </div>
  
        <button type="submit">Отправить</button>
        <RouterLink to="/authorization">Авторизация</RouterLink>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        form: {
          username: "",
          email: "",
          password: "",
        },
        errors: {
          username: null,
          email: null,
          password: null,
        },
      };
    },
    methods: {
      validateUsername() {
        if (this.form.username.length < 3) {
          this.errors.username = "Имя пользователя должно быть длинее 3 символов.";
        } else {
          this.errors.username = null;
        }
      },
      validateEmail() {
        const emailPattern =
          /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(this.form.email)) {
          this.errors.email = "Введите корректную почту.";
        } else {
          this.errors.email = null;
        }
      },
      validatePassword() {
        if (this.form.password.length < 6) {
          this.errors.password = "Пароль должен быть длинее 6 символов.";
        } else {
          this.errors.password = null;
        }
      },
      handleSubmit() {
        this.validateUsername();
        this.validateEmail();
        this.validatePassword();

        if (!this.errors.username && !this.errors.email && !this.errors.password) {
          console.log("Form data:", this.form);

          axios.post('http://localhost:5000/register', this.form)
            .then((response) => {
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-form {
    max-width: 400px;
    margin: 0 auto;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .error {
    color: red;
    font-size: 0.9em;
  }
  </style>
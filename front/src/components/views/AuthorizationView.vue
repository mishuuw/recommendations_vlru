<template>
    <div class="authorization-form">
      <h2>Авторизация</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="login">Имя пользователя или почти:</label>
          <input
            type="text"
            id="login"
            v-model="form.login"
            @blur="validateLogin"
          />
          <span v-if="errors.login" class="error">{{ errors.login }}</span>
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
        <RouterLink to="/registration">Регистрация</RouterLink>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          login: "",
          password: "",
        },
        errors: {
          login: null,
          password: null,
        },
      };
    },
    methods: {
      validateLogin() {
        if (this.form.login.length < 3) {
          this.errors.login = "Логин должен быть длинее 3 символов.";
        } else {
          this.errors.login = null;
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
        this.validateLogin();
        this.validatePassword();
  
        if (!this.errors.login && !this.errors.password) {
          console.log("Form data:", this.form);

        //   fetch("http://localhost:4000/registration", {
        //     method: 'POST', 
        //     headers: {
        //         'Content-Type': 'application/json;charset=utf-8'
        //     },
        //     body: JSON.stringify(Object.fromEntries(this.newPhoto)),
        // })
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .authorization-form {
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
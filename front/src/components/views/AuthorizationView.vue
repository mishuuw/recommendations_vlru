<template>
    <div class="authorization-form">
      <div class="button-group">
        <RouterLink to="/authorization" class="selected">Вход</RouterLink>
        <RouterLink to="/registration">Регистрация</RouterLink>
      </div>
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
        
        <div class="submit">
          <button type="submit">Отправить</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

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
        authorizedUser: null
      };
    },
    mounted() {
      // localStorage.setItem('visibleMainMenu', true)
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



          axios.post('http://localhost:5000/authorize', this.form)
            .then((response) => {
              console.log(response);
              // userID, username

              this.authorizedUser = JSON.parse(response)
              if (this.authorizedUser) {
                localStorage.setItem('authorizedUser', this.authorizedUser)
              } else {
                localStorage.setItem('authorizedUser', null)
              }
            })
            .catch((error) => {
              console.log(error);
              localStorage.setItem('authorizedUser', null)
            });
        }
      },
    },
  };
  </script>
  
  <style scoped> 
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
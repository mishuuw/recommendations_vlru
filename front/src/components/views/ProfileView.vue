<template>
    <div v-if="checkAuthorization">
        <h3>Профиль</h3>
        <p>Имя пользователя: {{ authorizedUser.username }}</p>
        <div>
            <RouterLink to="/favorites">Избранные события</RouterLink>
            <RouterLink to="/history">История покупок</RouterLink>
        </div>
        <button @click="logOut">Выйти из аккаунта</button>
    </div>
    <div v-else>
      <p>Сначала пройдите авторизацию</p>
      <RouterLink to="/authorization">Авторизация</RouterLink>
    </div>
</template>

<script>
export default {
    data() {
        return {
            authorizedUser: null,
            checkAuthorization: false,
        }
    }, 
    mounted() {
        // localStorage.setItem('visibleMainMenu', false)

        console.log(localStorage.getItem('authorizedUser'))

        if (localStorage.getItem('authorizedUser') !== 'null') {
            this.authorizedUser = localStorage.getItem('authorizedUser')
            this.checkAuthorization = true
        }

    },
    methods: {
        logOut() {
            localStorage.setItem('authorizedUser', null)
        }
    }
}
</script>
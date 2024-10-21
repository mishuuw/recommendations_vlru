<template>
    <h3>Тут будет нереальная инфа про ивент</h3>
</template>

<script>
// import axios from 'axios';

export default {
    data() {
        return {
            eventID: null,
            event: null,
        }
    },
    mounted() {
    //   localStorage.setItem('visibleMainMenu', false)

        axios.get('http://localhost:5000/getEventData', {
                params: {
                eventID: this.eventID // поменять параметр
                }
            })
            .then(function (response) {
                console.log(response);

                this.event = JSON.parse(response)
            })
            .catch(function (error) {
                console.log(error);
            })
    }
}
</script>
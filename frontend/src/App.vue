<template>
  <div id="app">
    <Header :contacts="contacts"></Header>
    <router-view></router-view>
    <Footer :contacts='contacts'></Footer>
  </div>
</template>

<script>
import Footer from './Footer'
import Header from './Header'
import $ from 'jquery'

export default {
    name: 'app',
    components: {
        Footer,
        Header
    },
    data: () => ({
        contacts: {}
    }),
    created: function(){
        this.getContacts()
    },
    methods: {
        getContacts() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/contacts/',
                type: 'GET',
                success: (data) => {
                    this.contacts = data
                },
                error: (err) => {
                    this.contacts = err
                }
            })
        }
    }
}
</script>

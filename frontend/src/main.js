import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Baloons from './components/Baloons'
import Decoration from './components/Decoration'
import Celebration from './components/Celebration'
import Sales from './components/Sales'
import Ideas from './components/Ideas'
import Top from './components/Top'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: Home,
        name: 'home',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Главная'
        }
    },
    {
        path: '/baloons',
        component: Baloons,
        name: 'baloons',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Воздушные шары'
        }
    },
    {
        path: '/decoration',
        component: Decoration,
        name: 'decoration',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Оформление праздников'
        }
    },
    {
        path: '/celebration',
        component: Celebration,
        name: 'celebration',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Товары для праздников'
        }
    },
    {
        path: '/sales',
        component: Sales,
        name: 'sales',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Акции'
        }
    },
    {
        path: '/ideas',
        component: Ideas,
        name: 'ideas',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Наши идеи'
        }
    },
    {
        path: '/top',
        component: Top,
        name: 'top',
        meta: {
            title: 'Шары и аксессуары для Ваших праздников | Популярные темы'
        }
    }
]

const router = new VueRouter({
    routes,
    mode: 'history',
    scrollBehavior () {
      return { x: 0, y: 0 }
    }
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    next()
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')

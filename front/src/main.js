import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home.vue'
import Diary from './components/Diary.vue'
import About from './components/About.vue'

Vue.use(VueRouter)

Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/diary',
      component: Diary
    },
    {
      path: '/about',
      component: About
    },
  ]

})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

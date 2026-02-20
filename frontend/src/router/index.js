import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import Spotify from '../views/Spotify.vue'
import NASA from '../views/NASA.vue'
import Cadence from '../views/Cadence.vue'
import Wolfram from '../views/Wolfram.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/spotify', component: Spotify },
  { path: '/nasa', component: NASA },
  { path: '/cadence', component: Cadence },
  { path: '/wolfram', component: Wolfram }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
/*
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Lvshijie
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import PPI_SHOOT1 from '../views/Tools/PPI_SHOOT1.vue'
Vue.use(VueRouter)
import Router from 'vue-router'

const originalPush = Router.prototype.push
Router.prototype.push = function push(location, onResolve, onReject) {
  if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject)
  return originalPush.call(this, location).catch(err => err)
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/Expression/index',
    name: 'ExpIndex',
    component: () => import('../views/Tools/Index'),

  },
  {
    path: '/Expression/PPI',
    name: 'ExpPPI',
    component: () => import('../views/Tools/ExpPPI'),

  },
  {
    path: '/Expression/PDI',
    name: 'ExpPDI',
    component: () => import('../views/Tools/ExpPDI'),

  },
  {
    path: '/Expression/indexShui',
    name: 'indexShui',
    component: () => import('../views/Tools/indexShui'),

  },

  {
    path: '/Methylation',
    name: 'Methylation',
    component: () => import('../views/Tools/Methylation'),
  },
  {
    path: '/Tools/PPI_SHOOT1',
    name: 'PPI_SHOOT1',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/result',
    name: 'Result',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Result.vue')
  },
  {
    path: '/search',
    name: 'Search',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Search.vue')
  },
  {
    path: '/show/:id',
    name: 'Show',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Show.vue')
  },
  {
    path: '/tutorial',
    name: 'Tutorial',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Tutorial.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

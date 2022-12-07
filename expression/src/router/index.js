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
    path: '/Expression',
    name: 'Expression',
    component: () => import('../views/Tools/Expression'),

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
    path: '/Tools/PPI_EAR1',
    name: 'PPI_EAR1',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PPI_SHOOT2',
    name: 'PPI_SHOOT2',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PPI_EAR2',
    name: 'Shoot1',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PPI_TASSEL',
    name: 'PPI_TASSEL',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PDI_SHOOT1',
    name: 'PDI_SHOOT1',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PDI_EAR',
    name: 'PDI_EAR',
    component: () => import('../views/Tools/PPI_SHOOT1.vue'),

  },
  {
    path: '/Tools/PDI_SHOOT2',
    name: 'PDI_SHOOT2',
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

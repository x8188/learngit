/*
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
import '../public/Element_custom_theme/theme/index.css'

import 'ant-design-vue/dist/antd.css';

Vue.use(ElementUI)
Vue.use(Antd);

import { MessageBox } from 'element-ui';
Vue.config.productionTip = false
// Vue.prototype.$message = Message
Vue.prototype.$msgbox = MessageBox;
Vue.prototype.$alert = MessageBox.alert;

import Steps from "./components/Steps.vue"
Vue.component(Steps.name,Steps)

import Table from "./components/Table.vue"
Vue.component(Table.name,Table)

import Back from "./components/Back.vue"
Vue.component(Back.name,Back)

import * as API  from './request' 
Vue.prototype.$API=API;

import './assets/iconfont/iconfont.css'

new Vue({
  router,
  store,
  el: '#app',
  components: { App },
  template: '<App/>',
  render: h => h(App)
}).$mount('#app')

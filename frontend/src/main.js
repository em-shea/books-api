import Vue from 'vue'
import App from './App.vue'
import router from './router'
import TreeView from 'vue-json-tree-view'

Vue.config.productionTip = false

Vue.use(TreeView)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

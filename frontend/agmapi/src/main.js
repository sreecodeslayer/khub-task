// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VDateRange from 'vuetify-daterange-picker'
import 'vuetify-daterange-picker/dist/vuetify-daterange-picker.css'
import VueMoment from 'vue-moment'
import Trend from 'vuetrend'

axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.baseURL = process.env.BASE_URL

Vue.use(VueAxios, axios)
Vue.use(Vuetify)
Vue.use(VueMoment)
Vue.use(VDateRange)
Vue.use(Trend)

Vue.config.productionTip = false
Vue.filter('calendarTime', function (value) {
  return Vue.moment(value).calendar(null, {sameElse: 'DD/MMM/YYYY'})
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

webpackJsonp([1],{"7zck":function(t,a){},"A3Z+":function(t,a){},NHnr:function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var s=e("7+uW"),n={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-app",[e("v-navigation-drawer",{staticClass:"indigo darken-2",attrs:{persistent:"","mini-variant":t.miniVariant,clipped:t.clipped,"enable-resize-watcher":"",fixed:"",app:""},model:{value:t.drawer,callback:function(a){t.drawer=a},expression:"drawer"}},[e("v-list",t._l(t.items,function(a,s){return e("v-list-tile",{key:s,attrs:{value:"true"}},[e("v-list-tile-action",{staticClass:"white--text"},[e("v-icon",{domProps:{innerHTML:t._s(a.icon)}})],1),t._v(" "),e("v-list-tile-content",{staticClass:"white--text"},[e("v-list-tile-title",{domProps:{textContent:t._s(a.title)}})],1)],1)}))],1),t._v(" "),e("v-toolbar",{staticClass:"indigo darken-2",attrs:{app:"",dark:"","clipped-left":t.clipped,"scroll-off-screen":""}},[e("v-btn",{attrs:{icon:""},on:{click:function(a){a.stopPropagation(),t.miniVariant=!t.miniVariant}}},[e("v-icon",{domProps:{innerHTML:t._s(t.miniVariant?"chevron_right":"chevron_left")}})],1),t._v(" "),e("v-toolbar-title",{attrs:{href:"#/"},domProps:{textContent:t._s(t.title)}}),t._v(" "),e("v-spacer")],1),t._v(" "),e("v-content",[e("router-view")],1),t._v(" "),e("v-footer",{staticClass:"grey lighten-2",attrs:{fixed:t.fixed,app:""}},[e("v-layout",{attrs:{column:"","align-center":""}},[e("span",{staticClass:"text-xs-center"},[t._v("© 2018")])])],1)],1)},staticRenderFns:[]},i=e("VU/8")({data:function(){return{clipped:!1,drawer:!0,fixed:!1,items:[{icon:"dashboard",title:"Home"}],miniVariant:!0,title:"AGMAPI"}},name:"App"},n,!1,null,null,null).exports,o=e("/ocq"),r=e("wuJz"),c={name:"Home",data:function(){return{commodities:[],commoditiesHeader:[{text:"Item",value:"commodity",sortable:!1},{text:"Market Center",value:"mandi",sortable:!1},{text:"State",value:"state",sortable:!1},{text:"Arrivals",value:"arrivals",sortable:!1},{text:"As on",value:"date",sortable:!1},{text:"Minimum Price",value:"min_price",sortable:!1},{text:"Maximum Price",value:"max_price",sortable:!1},{text:"Modal Price",value:"modal_price",sortable:!1}],mandis:[],chart:{type:"min",data:[]},stocksPagination:{},responseData:{},stocks:{data:[],totalPages:1,page:1,totalItems:0},insights:null,search:{commodity:"",mandi:{name:"",id:""},date:"",from:"",to:""},date:null,toggleDateFilter:!1,dialogDate:!1,modalDate:!1,modalRange:!1,stocksLoading:!1,dateRangeOptions:{startDate:Object(r.format)(Object(r.subDays)(new Date,7),"YYYY-MM-DD"),endDate:Object(r.format)(new Date,"YYYY-MM-DD"),format:"YYYY/MM/DD"},dateRange:null}},watch:{stocksPagination:{handler:function(){this.fetchReports()},deep:!0}},methods:{onChartTypeChange:function(){"min"===this.chart.type&&(this.chart.data=this.stocks.data.map(function(t){return parseInt(t.min_price)}),this.chart.gradient=["#B71C1C"]),"max"===this.chart.type&&(this.chart.data=this.stocks.data.map(function(t){return parseInt(t.max_price)}),this.chart.gradient=["#1A237E"]),"modal"===this.chart.type&&(this.chart.data=this.stocks.data.map(function(t){return parseInt(t.modal_price)}),this.chart.gradient=["#1B5E20"])},onDateRangeChange:function(t){this.search.from=t[0],this.search.to=t[1]},fetchReports:function(){var t=this,a=this.stocksPagination.page,e=this.stocksPagination.rowsPerPage,s="/stocks?commodity="+this.search.commodity+"&mandi="+this.search.mandi.id+"&date="+this.search.date+"&from="+this.search.from+"&to="+this.search.to+"&page="+a+"&perPage="+e;this.stocksLoading=!0,this.$http.get(s).then(function(a){t.responseData=a.data,t.stocks.totalPages=parseInt(t.responseData.total_pages),t.stocks.totalItems=parseInt(t.responseData.total),t.stocks.page=parseInt(t.responseData.page),t.stocks.data=t.responseData.stocks,t.insights=t.responseData.insights,t.stocksLoading=!1,t.onChartTypeChange()},function(t){})},preFetchData:function(){var t=this;this.$http.get("/commodities").then(function(a){t.commodities=a.data.commodities},function(t){}),this.$http.get("/mandis").then(function(a){t.mandis=a.data.mandis},function(t){})}},created:function(){this.preFetchData()}},l={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-container",{attrs:{fluid:"","grid-list-xs":""}},[e("v-slide-y-transition",{attrs:{mode:"out-in"}},[e("div",[e("v-layout",{attrs:{row:"",wrap:"","gird-list-sm":""}},[e("v-flex",{attrs:{xs12:""}},[e("v-card",[e("v-card-text",[e("v-layout",{attrs:{row:"",wrap:""}},[e("v-flex",{attrs:{xs3:""}},[e("v-select",{attrs:{items:t.commodities,"item-text":"name","item-value":"name",label:"Select commodity",autocomplete:""},on:{input:function(a){t.fetchReports()}},model:{value:t.search.commodity,callback:function(a){t.$set(t.search,"commodity",a)},expression:"search.commodity"}})],1),t._v(" "),e("v-flex",{attrs:{xs3:""}},[e("v-select",{attrs:{items:t.mandis,"item-text":"name",label:"Select mandi",autocomplete:""},on:{input:function(a){t.fetchReports()}},model:{value:t.search.mandi,callback:function(a){t.$set(t.search,"mandi",a)},expression:"search.mandi"}})],1),t._v(" "),t.toggleDateFilter?t._e():e("v-flex",{attrs:{xs3:""}},[e("v-dialog",{ref:"dialogDate",attrs:{persistent:"",lazy:"","full-width":"",width:"475px","return-value":t.search.date},on:{"update:returnValue":function(a){t.$set(t.search,"date",a)}},model:{value:t.modalDate,callback:function(a){t.modalDate=a},expression:"modalDate"}},[e("v-text-field",{attrs:{slot:"activator",label:"Select date for report","prepend-icon":"event",readonly:""},slot:"activator",model:{value:t.search.date,callback:function(a){t.$set(t.search,"date",a)},expression:"search.date"}}),t._v(" "),e("v-date-picker",{attrs:{color:"indigo darken-2","show-current":!0,landscape:!t.$vuetify.breakpoint.xs,scrollable:""},model:{value:t.search.date,callback:function(a){t.$set(t.search,"date",a)},expression:"search.date"}},[e("v-spacer"),t._v(" "),e("v-btn",{attrs:{flat:"",color:"info"},on:{click:function(a){t.modalDate=!1,t.modalRange=!0,t.toggleDateFilter=!t.toggleDateFilter}}},[t._v("Range")]),t._v(" "),e("v-btn",{attrs:{flat:"",color:"warning"},on:{click:function(a){t.search.from="",t.search.to="",t.search.date="",t.modalDate=!1}}},[t._v("Cancel")]),t._v(" "),e("v-btn",{attrs:{flat:"",color:"success"},on:{click:function(a){t.search.from="",t.search.to="",t.$refs.dialogDate.save(t.search.date),t.fetchReports()}}},[t._v("OK")])],1)],1)],1),t._v(" "),t.toggleDateFilter?e("v-flex",{attrs:{xs3:""}},[e("v-dialog",{ref:"dialogDateRange",attrs:{persistent:"",lazy:"","full-width":"",width:"800px"},model:{value:t.modalRange,callback:function(a){t.modalRange=a},expression:"modalRange"}},[e("v-text-field",{attrs:{slot:"activator",label:"Select date range report","prepend-icon":"event",readonly:""},slot:"activator",model:{value:t.search.date,callback:function(a){t.$set(t.search,"date",a)},expression:"search.date"}}),t._v(" "),e("v-card",[e("v-card-text",[e("v-daterange",{attrs:{options:t.dateRangeOptions},on:{input:t.onDateRangeChange}})],1),t._v(" "),e("v-card-actions",[e("v-spacer"),t._v(" "),e("v-btn",{attrs:{flat:"",color:"info"},on:{click:function(a){t.modalDate=!0,t.modalRange=!1,t.toggleDateFilter=!t.toggleDateFilter}}},[t._v("Date")]),t._v(" "),e("v-btn",{attrs:{flat:"",color:"warning"},on:{click:function(a){t.search.date="",t.search.from="",t.search.to="",t.modalRange=!1}}},[t._v("Cancel")]),t._v(" "),e("v-btn",{attrs:{flat:"",color:"success"},on:{click:function(a){t.search.date="",t.fetchReports(),t.modalRange=!1}}},[t._v("OK")])],1)],1)],1)],1):t._e()],1)],1)],1)],1)],1),t._v(" "),e("v-layout",{attrs:{row:"",wrap:""}},[t.search.commodity&&t.insights.commodity.low?e("v-flex",{attrs:{xs6:""}},[e("v-card",{attrs:{color:"teal darken-4",dark:""}},[e("v-card-title",[e("div",{staticClass:"title white--text"},[t._v(t._s(t.search.commodity))])]),t._v(" "),e("v-card-text",[e("v-layout",{attrs:{row:"",wrap:""}},[e("v-flex",{attrs:{xs12:""}},[e("div",{staticClass:"caption"},[t._v("The lowest occured in : "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.commodity.low.mandi.name))])]),t._v(" "),e("div",{staticClass:"body-2"},[t._v("Cost: "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.commodity.low.modal_price))])]),t._v(" "),e("div",{staticClass:"caption"},[t._v("The highest occured in : "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.commodity.high.mandi.name))])]),t._v(" "),e("div",{staticClass:"body-2"},[t._v("Cost: "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.commodity.high.modal_price))])])])],1)],1)],1)],1):t._e(),t._v(" "),t.search.mandi.id&&t.insights.mandi.low?e("v-flex",{attrs:{xs6:""}},[e("v-card",{attrs:{color:"teal darken-4",dark:""}},[e("v-card-title",[e("div",{staticClass:"title white--text"},[t._v(t._s(t.search.mandi.name))])]),t._v(" "),e("v-card-text",[e("v-layout",{attrs:{row:"",wrap:""}},[e("v-flex",{attrs:{xs12:""}},[e("div",{staticClass:"caption"},[t._v("The lowest priced crop is : "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.mandi.low.commodity.name))])]),t._v(" "),e("div",{staticClass:"body-2"},[t._v("Cost: "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.mandi.low.modal_price))])]),t._v(" "),e("div",{staticClass:"caption"},[t._v("The highest priced crop is : "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.mandi.high.commodity.name))])]),t._v(" "),e("div",{staticClass:"body-2"},[t._v("Cost: "),e("span",{staticClass:"red--text"},[t._v(t._s(t.insights.mandi.high.modal_price))])])])],1)],1)],1)],1):t._e()],1),t._v(" "),e("v-layout",{attrs:{row:"",wrap:""}},[e("v-flex",{attrs:{xs12:"",sm12:"",md6:"",lg8:""}},[e("v-card",[e("v-card-text",[e("v-data-table",{attrs:{headers:t.commoditiesHeader,"rows-per-page-items":[50,5,10,20,70,200],pagination:t.stocksPagination,loading:t.stocksLoading,items:t.stocks.data,"total-items":t.stocks.totalItems},on:{"update:pagination":function(a){t.stocksPagination=a}},scopedSlots:t._u([{key:"items",fn:function(a){return[e("td",[t._v(t._s(a.item.commodity.name))]),t._v(" "),e("td",[t._v(t._s(a.item.mandi.name))]),t._v(" "),e("td",[t._v(t._s(a.item.state.name))]),t._v(" "),e("td",[t._v(t._s(a.item.arrivals))]),t._v(" "),e("td",[t._v(t._s(t._f("calendarTime")(a.item.date)))]),t._v(" "),e("td",[t._v(t._s(a.item.min_price))]),t._v(" "),e("td",[t._v(t._s(a.item.max_price))]),t._v(" "),e("td",[t._v(t._s(a.item.modal_price))])]}}])},[e("v-progress-linear",{attrs:{slot:"progress",color:"success",indeterminate:""},slot:"progress"})],1)],1)],1)],1),t._v(" "),e("v-flex",{attrs:{xs12:"",sm12:"",md6:"",lg4:""}},[e("v-card",[e("v-card-title",{attrs:{"primary-title":""}},[e("div",{staticClass:"headline"},[t._v("Price Trends")])]),t._v(" "),e("v-card-text",[e("trend",{attrs:{data:t.chart.data,gradient:t.chart.gradient,"auto-draw":"",smooth:""}})],1),t._v(" "),e("v-card-actions",[e("v-radio-group",{attrs:{row:""},on:{change:t.onChartTypeChange},model:{value:t.chart.type,callback:function(a){t.$set(t.chart,"type",a)},expression:"chart.type"}},[e("v-radio",{attrs:{label:"Min Price",color:"red",value:"min","hide-details":""}}),t._v(" "),e("v-radio",{attrs:{label:"Max Price",color:"indigo",value:"max","hide-details":""}}),t._v(" "),e("v-radio",{attrs:{label:"Modal Price",color:"green",value:"modal","hide-details":""}})],1)],1)],1)],1)],1)],1)])],1)},staticRenderFns:[]};var d=e("VU/8")(c,l,!1,function(t){e("WhLl")},"data-v-72bad0b8",null).exports;s.a.use(o.a);var m=new o.a({routes:[{path:"/",name:"Home",component:d}]}),v=e("3EgV"),h=e.n(v),p=(e("7zck"),e("mtWM")),u=e.n(p),g=e("Rf8U"),f=e.n(g),j=e("goa7"),_=e.n(j),x=(e("A3Z+"),e("mjDs")),k=e.n(x),b=e("4Imv");u.a.defaults.headers.post["Content-Type"]="application/json",u.a.defaults.baseURL="/api/",s.a.use(f.a,u.a),s.a.use(h.a),s.a.use(k.a),s.a.use(_.a),s.a.use(b.a),s.a.config.productionTip=!1,s.a.filter("calendarTime",function(t){return s.a.moment(t).calendar(null,{sameElse:"DD/MMM/YYYY"})}),new s.a({el:"#app",router:m,components:{App:i},template:"<App/>"})},WhLl:function(t,a){},uslO:function(t,a,e){var s={"./af":"3CJN","./af.js":"3CJN","./ar":"3MVc","./ar-dz":"tkWw","./ar-dz.js":"tkWw","./ar-kw":"j8cJ","./ar-kw.js":"j8cJ","./ar-ly":"wPpW","./ar-ly.js":"wPpW","./ar-ma":"dURR","./ar-ma.js":"dURR","./ar-sa":"7OnE","./ar-sa.js":"7OnE","./ar-tn":"BEem","./ar-tn.js":"BEem","./ar.js":"3MVc","./az":"eHwN","./az.js":"eHwN","./be":"3hfc","./be.js":"3hfc","./bg":"lOED","./bg.js":"lOED","./bm":"hng5","./bm.js":"hng5","./bn":"aM0x","./bn.js":"aM0x","./bo":"w2Hs","./bo.js":"w2Hs","./br":"OSsP","./br.js":"OSsP","./bs":"aqvp","./bs.js":"aqvp","./ca":"wIgY","./ca.js":"wIgY","./cs":"ssxj","./cs.js":"ssxj","./cv":"N3vo","./cv.js":"N3vo","./cy":"ZFGz","./cy.js":"ZFGz","./da":"YBA/","./da.js":"YBA/","./de":"DOkx","./de-at":"8v14","./de-at.js":"8v14","./de-ch":"Frex","./de-ch.js":"Frex","./de.js":"DOkx","./dv":"rIuo","./dv.js":"rIuo","./el":"CFqe","./el.js":"CFqe","./en-au":"Sjoy","./en-au.js":"Sjoy","./en-ca":"Tqun","./en-ca.js":"Tqun","./en-gb":"hPuz","./en-gb.js":"hPuz","./en-ie":"ALEw","./en-ie.js":"ALEw","./en-il":"QZk1","./en-il.js":"QZk1","./en-nz":"dyB6","./en-nz.js":"dyB6","./eo":"Nd3h","./eo.js":"Nd3h","./es":"LT9G","./es-do":"7MHZ","./es-do.js":"7MHZ","./es-us":"INcR","./es-us.js":"INcR","./es.js":"LT9G","./et":"XlWM","./et.js":"XlWM","./eu":"sqLM","./eu.js":"sqLM","./fa":"2pmY","./fa.js":"2pmY","./fi":"nS2h","./fi.js":"nS2h","./fo":"OVPi","./fo.js":"OVPi","./fr":"tzHd","./fr-ca":"bXQP","./fr-ca.js":"bXQP","./fr-ch":"VK9h","./fr-ch.js":"VK9h","./fr.js":"tzHd","./fy":"g7KF","./fy.js":"g7KF","./gd":"nLOz","./gd.js":"nLOz","./gl":"FuaP","./gl.js":"FuaP","./gom-latn":"+27R","./gom-latn.js":"+27R","./gu":"rtsW","./gu.js":"rtsW","./he":"Nzt2","./he.js":"Nzt2","./hi":"ETHv","./hi.js":"ETHv","./hr":"V4qH","./hr.js":"V4qH","./hu":"xne+","./hu.js":"xne+","./hy-am":"GrS7","./hy-am.js":"GrS7","./id":"yRTJ","./id.js":"yRTJ","./is":"upln","./is.js":"upln","./it":"FKXc","./it.js":"FKXc","./ja":"ORgI","./ja.js":"ORgI","./jv":"JwiF","./jv.js":"JwiF","./ka":"RnJI","./ka.js":"RnJI","./kk":"j+vx","./kk.js":"j+vx","./km":"5j66","./km.js":"5j66","./kn":"gEQe","./kn.js":"gEQe","./ko":"eBB/","./ko.js":"eBB/","./ky":"6cf8","./ky.js":"6cf8","./lb":"z3hR","./lb.js":"z3hR","./lo":"nE8X","./lo.js":"nE8X","./lt":"/6P1","./lt.js":"/6P1","./lv":"jxEH","./lv.js":"jxEH","./me":"svD2","./me.js":"svD2","./mi":"gEU3","./mi.js":"gEU3","./mk":"Ab7C","./mk.js":"Ab7C","./ml":"oo1B","./ml.js":"oo1B","./mn":"CqHt","./mn.js":"CqHt","./mr":"5vPg","./mr.js":"5vPg","./ms":"ooba","./ms-my":"G++c","./ms-my.js":"G++c","./ms.js":"ooba","./mt":"oCzW","./mt.js":"oCzW","./my":"F+2e","./my.js":"F+2e","./nb":"FlzV","./nb.js":"FlzV","./ne":"/mhn","./ne.js":"/mhn","./nl":"3K28","./nl-be":"Bp2f","./nl-be.js":"Bp2f","./nl.js":"3K28","./nn":"C7av","./nn.js":"C7av","./pa-in":"pfs9","./pa-in.js":"pfs9","./pl":"7LV+","./pl.js":"7LV+","./pt":"ZoSI","./pt-br":"AoDM","./pt-br.js":"AoDM","./pt.js":"ZoSI","./ro":"wT5f","./ro.js":"wT5f","./ru":"ulq9","./ru.js":"ulq9","./sd":"fW1y","./sd.js":"fW1y","./se":"5Omq","./se.js":"5Omq","./si":"Lgqo","./si.js":"Lgqo","./sk":"OUMt","./sk.js":"OUMt","./sl":"2s1U","./sl.js":"2s1U","./sq":"V0td","./sq.js":"V0td","./sr":"f4W3","./sr-cyrl":"c1x4","./sr-cyrl.js":"c1x4","./sr.js":"f4W3","./ss":"7Q8x","./ss.js":"7Q8x","./sv":"Fpqq","./sv.js":"Fpqq","./sw":"DSXN","./sw.js":"DSXN","./ta":"+7/x","./ta.js":"+7/x","./te":"Nlnz","./te.js":"Nlnz","./tet":"gUgh","./tet.js":"gUgh","./tg":"5SNd","./tg.js":"5SNd","./th":"XzD+","./th.js":"XzD+","./tl-ph":"3LKG","./tl-ph.js":"3LKG","./tlh":"m7yE","./tlh.js":"m7yE","./tr":"k+5o","./tr.js":"k+5o","./tzl":"iNtv","./tzl.js":"iNtv","./tzm":"FRPF","./tzm-latn":"krPU","./tzm-latn.js":"krPU","./tzm.js":"FRPF","./ug-cn":"To0v","./ug-cn.js":"To0v","./uk":"ntHu","./uk.js":"ntHu","./ur":"uSe8","./ur.js":"uSe8","./uz":"XU1s","./uz-latn":"/bsm","./uz-latn.js":"/bsm","./uz.js":"XU1s","./vi":"0X8Q","./vi.js":"0X8Q","./x-pseudo":"e/KL","./x-pseudo.js":"e/KL","./yo":"YXlc","./yo.js":"YXlc","./zh-cn":"Vz2w","./zh-cn.js":"Vz2w","./zh-hk":"ZUyn","./zh-hk.js":"ZUyn","./zh-tw":"BbgG","./zh-tw.js":"BbgG"};function n(t){return e(i(t))}function i(t){var a=s[t];if(!(a+1))throw new Error("Cannot find module '"+t+"'.");return a}n.keys=function(){return Object.keys(s)},n.resolve=i,t.exports=n,n.id="uslO"}},["NHnr"]);
//# sourceMappingURL=app.79037881ab40e3843287.js.map
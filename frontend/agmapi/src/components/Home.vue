<template>
  <v-container fluid grid-list-xs>
    <v-slide-y-transition mode="out-in">
      <div>
        <v-layout row wrap gird-list-sm>
          <v-flex xs12>
            <v-card>
              <v-card-text>
                <v-layout row wrap>
                  <!-- Filter bar -->
                  <!-- Crop name selector -->
                  <v-flex xs3>
                    <v-select :items="commodities" item-text="name" item-value="name" v-model="search.commodity" label="Select commodity" autocomplete @input="fetchReports()"></v-select>
                  </v-flex>
                  <!-- Mandi name selector -->
                  <v-flex xs3>
                    <v-select :items="mandis" item-text="name" v-model="search.mandi" label="Select mandi" autocomplete @input="fetchReports()"></v-select>
                  </v-flex>
                  <!-- Date name selector -->
                  <v-flex xs3 v-if="!toggleDateFilter">
                    <v-dialog ref="dialogDate" persistent v-model="modalDate" lazy full-width width="475px" :return-value.sync="search.date">
                      <v-text-field slot="activator" label="Select date for report" v-model="search.date" prepend-icon="event" readonly ></v-text-field>
                      <v-date-picker color="indigo darken-2" :show-current="true" :landscape="$vuetify.breakpoint.xs?false:true" v-model="search.date" scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="info" @click="modalDate = false; modalRange = true; toggleDateFilter = !toggleDateFilter">Range</v-btn>
                        <v-btn flat color="warning" @click="search.from='';search.to='';search.date='';modalDate = false">Cancel</v-btn>
                        <v-btn flat color="success" @click="search.from='';search.to='';$refs.dialogDate.save(search.date);fetchReports()">OK</v-btn>
                      </v-date-picker>
                    </v-dialog>
                  </v-flex xs3>
                  <!-- Range - date selector -->
                  <v-flex xs3 v-if="toggleDateFilter">
                    <v-dialog ref="dialogDateRange" persistent v-model="modalRange" lazy full-width width="800px">
                      <v-text-field slot="activator" label="Select date range report" v-model="search.date" prepend-icon="event" readonly ></v-text-field>
                      <v-card>
                        <v-card-text>
                          <v-daterange :options="dateRangeOptions" @input="onDateRangeChange"></v-daterange>
                        </v-card-text>
                        <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn flat color="info" @click="modalDate = true; modalRange = false; toggleDateFilter = !toggleDateFilter">Date</v-btn>
                      <v-btn flat color="warning" @click="search.date='';search.from='';search.to='';modalRange = false">Cancel</v-btn>
                      <v-btn flat color="success" @click="search.date='';fetchReports(); modalRange = false">OK</v-btn>
                    </v-card-actions>
                    </v-card>
                    </v-dialog>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        <!-- Insights -->
        <v-layout row wrap>
          <v-flex xs6 v-if="search.commodity && stocks.data.length">
            <v-card color="teal lighten-3">
              <v-card-title>
                <div class="title white--text">{{search.commodity}}</div>
              </v-card-title>
              <v-card-text>
                <v-layout row wrap>
                  <v-flex xs12>
                    <div class="caption">The lowest occured in : <span class="red--text">{{insights.commodity.low.mandi.name}}</span></div>
                    <div class="body-2">Cost: <span class="red--text">{{insights.commodity.low.modal_price}}</span></div>
                    <div class="caption">The highest occured in : <span class="red--text">{{insights.commodity.high.mandi.name}}</span></div>
                    <div class="body-2">Cost: <span class="red--text">{{insights.commodity.high.modal_price}}</span></div>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs6 v-if="search.mandi.id && stocks.data.length" v-cloak>
            <v-card color="teal lighten-3">
              <v-card-title>
                <div class="title white--text">{{search.mandi.name}}</div>
              </v-card-title>
              <v-card-text>
                <v-layout row wrap>
                  <v-flex xs12>
                    <div class="caption">The lowest priced crop is : <span class="red--text">{{insights.mandi.low.commodity.name}}</span></div>
                    <div class="body-2">Cost: <span class="red--text">{{insights.mandi.low.modal_price}}</span></div>
                    <div class="caption">The highest priced crop is : <span class="red--text">{{insights.mandi.high.commodity.name}}</span></div>
                    <div class="body-2">Cost: <span class="red--text">{{insights.mandi.high.modal_price}}</span></div>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        <!-- Data table and graphs -->
        <v-layout row wrap>
          <v-flex xs12 sm12 md6 lg8>
            <v-card>
              <v-card-text>
                <!-- Filter bar -->
                <v-data-table :headers="commoditiesHeader" :rows-per-page-items="[50,5,10,20,70,200]" :pagination.sync="stocksPagination" :loading="stocksLoading" :items="stocks.data" :total-items="stocks.totalItems">
                  <v-progress-linear slot="progress" color="success" indeterminate></v-progress-linear>
                  <template slot="items" slot-scope="props" style="overflow-y: scroll;max-height: 100vh;">
                    <td>{{ props.item.commodity.name }}</td>
                    <td>{{ props.item.mandi.name }}</td>
                    <td>{{ props.item.state.name }}</td>
                    <td>{{ props.item.arrivals }}</td>
                    <td>{{ props.item.date | calendarTime }}</td>
                    <td>{{ props.item.min_price }}</td>
                    <td>{{ props.item.max_price }}</td>
                    <td>{{ props.item.modal_price }}</td>
                  </template>
                </v-data-table>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs12 sm12 md6 lg4>
            <v-card>
              <v-card-title primary-title>
                <div class="headline">Price Trends</div>
              </v-card-title>
              <v-card-text>
              <trend
                :data="chart.data"
                :gradient="chart.gradient"
                auto-draw
                smooth>
              </trend>
            </v-card-text>
            <v-card-actions>
              <v-radio-group v-model="chart.type" row @change="onChartTypeChange">
                
              <v-radio label="Min Price" color="red" value="min" hide-details></v-radio>
              <v-radio label="Max Price" color="indigo" value="max" hide-details></v-radio>
              <v-radio label="Modal Price" color="green" value="modal" hide-details></v-radio>
              </v-radio-group>
            </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </div>
    </v-slide-y-transition>
  </v-container>
</template>
<script>
import { format, subDays } from 'date-fns'

export default{
  name: 'Home',
  data () {
    return {
      commodities: [],
      commoditiesHeader: [
        {text: 'Item', value: 'commodity', sortable: false},
        {text: 'Market Center', value: 'mandi', sortable: false},
        {text: 'State', value: 'state', sortable: false},
        {text: 'Arrivals', value: 'arrivals', sortable: false},
        {text: 'As on', value: 'date', sortable: false},
        {text: 'Minimum Price', value: 'min_price', sortable: false},
        {text: 'Maximum Price', value: 'max_price', sortable: false},
        {text: 'Modal Price', value: 'modal_price', sortable: false}
      ],
      mandis: [],
      chart: {
        type: 'min',
        data: []
      },
      stocksPagination: {},
      stocks: {
        data: [],
        totalPages: 1,
        page: 1,
        totalItems: 0
      },
      insights: null,
      search: {
        commodity: '',
        mandi: {name: '', id: ''},
        date: '',
        from: '',
        to: ''
      },
      date: null,
      toggleDateFilter: false,
      dialogDate: false,
      modalDate: false,
      modalRange: false,
      stocksLoading: false,
      dateRangeOptions: {
        startDate: format(subDays(new Date(), 7), 'YYYY-MM-DD'),
        endDate: format(new Date(), 'YYYY-MM-DD'),
        format: 'YYYY/MM/DD'
      },
      dateRange: null
    }
  },
  watch: {
    stocksPagination: {
      handler () {
        this.fetchReports()
      },
      deep: true
    }
  },
  methods: {
    onChartTypeChange: function () {
      if (this.chart.type === 'min') {
        this.chart.data = this.stocks.data.map(function (a) { return parseInt(a.min_price) })
        this.chart.gradient = ['#B71C1C']
      }
      if (this.chart.type === 'max') {
        this.chart.data = this.stocks.data.map(function (a) { return parseInt(a.max_price) })
        this.chart.gradient = ['#1A237E']
      }
      if (this.chart.type === 'modal') {
        this.chart.data = this.stocks.data.map(function (a) { return parseInt(a.modal_price) })
        this.chart.gradient = ['#1B5E20']
      }
    },
    onDateRangeChange: function (range) {
      this.search.from = range[0]
      this.search.to = range[1]
    },
    fetchReports: function () {
      console.log(this.search)
      var page = this.stocksPagination.page
      var perPage = this.stocksPagination.rowsPerPage
      var url = '/stocks?commodity=' + this.search.commodity + '&mandi=' + this.search.mandi.id + '&date=' + this.search.date + '&from=' + this.search.from + '&to=' + this.search.to + '&page=' + page + '&perPage=' + perPage
      this.stocksLoading = true
      this.$http.get(url).then(
        (response) => {
          this.stocks.totalPages = parseInt(response.data.total_pages)
          this.stocks.totalItems = parseInt(response.data.total)
          this.stocks.page = parseInt(response.data.page)
          this.stocks.data = response.data.stocks
          this.insights = response.data.insights
          console.log(this.insights, this.insights.length)
          this.stocksLoading = false
          this.onChartTypeChange()
        },
        (err) => {}
      )
    },
    preFetchData: function () {
      this.$http.get('/commodities').then(
        (response) => {
          this.commodities = response.data.commodities
        },
        (err) => {}
      )
      this.$http.get('/mandis').then(
        (response) => {
          this.mandis = response.data.mandis
        },
        (err) => {}
      )
    }
  },
  created () {
    this.preFetchData()
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

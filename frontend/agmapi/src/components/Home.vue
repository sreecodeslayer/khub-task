<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <div>
        <v-layout row wrap gird-list-sm>
          <v-flex xs12>
            <v-card>
              <v-card-text>
                <v-layout row wrap gird-list-xs>
                  <!-- Filter bar -->
                  <!-- Crop name selector -->
                  <v-flex xs4>
                    <v-select :items="commodities" item-text="name" item-value="name" v-model="search.commodity" label="Select commodity" autocomplete @input="fetchReports()"></v-select>
                  </v-flex>
                  <!-- Mandi name selector -->
                  <v-flex xs4>
                    <v-select :items="mandis" item-text="name" item-value="id" v-model="search.mandi" label="Select mandi" autocomplete @input="fetchReports()"></v-select>
                  </v-flex>
                  <!-- Date name selector -->
                  <v-flex xs4>
                    <v-dialog ref="dialogDate" persistent v-model="modalDate" lazy full-width width="460px" :return-value.sync="search.date">
                      <v-text-field slot="activator" label="Select date for report" v-model="search.date" prepend-icon="event" readonly ></v-text-field>
                      <v-date-picker color="indigo darken-2" :show-current="true" :landscape="$vuetify.breakpoint.xs?false:true" v-model="search.date" scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="warning" @click="dialogDate = false">Cancel</v-btn>
                        <v-btn flat color="success" @click="$refs.dialogDate.save(search.date);fetchReports()">OK</v-btn>
                      </v-date-picker>
                    </v-dialog>
                  </v-flex>
                  <!-- Range - From name selector -->
                  <!-- Range - To name selector -->
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        <br>
        <v-layout row wrap gird-list-sm>
          <v-flex :class='$vuetify.breakpoint.xs ? "xs12" : "md6 lg8"'>
            <v-card>
              <v-card-text>
                <!-- Filter bar -->
                <v-data-table :headers="commoditiesHeader" :rows-per-page-items="[5,10,20]" :pagination.sync="stocksPagination" :loading="stocksLoading" :items="stocks.data" :total-items="stocks.totalItems">
                  <v-progress-linear slot="progress" color="success" indeterminate></v-progress-linear>
                  <template slot="items" slot-scope="props">
                    <td>{{ props.item.mandi.name }}</td>
                    <td>{{ props.item.state.name }}</td>
                    <td>{{ props.item.arrivals }}</td>
                    <td>{{ props.item.min_price }}</td>
                    <td>{{ props.item.max_price }}</td>
                    <td>{{ props.item.modal_price }}</td>
                  </template>

                </v-data-table>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </div>
    </v-slide-y-transition>
  </v-container>
</template>
<script>
export default{
  name: 'Home',
  data () {
    return {
      commodities: [],
      commoditiesHeader: [
        {text: 'Market Center', value: 'mandi', sortable: false},
        {text: 'State', value: 'state', sortable: false},
        {text: 'Arrivals', value: 'arrivals', sortable: false},
        {text: 'Minimum Price', value: 'min_price', sortable: false},
        {text: 'Maximum Price', value: 'max_price', sortable: false},
        {text: 'Modal Price', value: 'modal_price', sortable: false}
      ],
      mandis: [],
      stocksPagination: {},
      stocks: {
        data: [],
        totalPages: 1,
        page: 1,
        totalItems: 0
      },
      search: {
        commodity: '',
        mandi: '',
        date: '',
        from: '',
        to: ''
      },
      date: null,
      dialogDate: false,
      modalDate: false,
      stocksLoading: false
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
    fetchReports: function () {
      var page = this.stocksPagination.page
      var perPage = this.stocksPagination.rowsPerPage
      var url = '/stocks?commodity=' + this.search.commodity + '&mandi=' + this.search.mandi + '&date=' + this.search.date + '&from=' + this.search.from + '&to=' + this.search.to + '&page=' + page + '&perPage=' + perPage
      this.stocksLoading = true
      this.$http.get(url).then(
        (response) => {
          this.stocks.totalPages = parseInt(response.data.total_pages)
          this.stocks.totalItems = parseInt(response.data.total)
          this.stocks.page = parseInt(response.data.page)
          this.stocks.data = response.data.stocks
          this.stocksLoading = false
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

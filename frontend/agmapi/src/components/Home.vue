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
      mandis: [],
      search: {
        commodity: '',
        mandi: '',
        date: '',
        from: '',
        to: ''
      },
      date: null,
      dialogDate: false,
      modalDate: false
    }
  },
  methods: {
    fetchReports: function () {
      var url = '/stocks?commodity=' + this.search.commodity + '&mandi=' + this.search.mandi + '&date=' + this.search.date + '&from=' + this.search.from + '&to=' + this.search.to
      console.log(this.search, url)

      this.$http.get(url).then(
        (response) => {
          console.log(response.data)
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

<template>
  <v-app>
    <v-navigation-drawer persistent  class='indigo darken-2' :mini-variant="miniVariant" :clipped="clipped" v-model="drawer" enable-resize-watcher fixed app >
      <v-list>
        <v-list-tile value="true" v-for="(item, i) in items" :key="i" >
          <v-list-tile-action class="white--text">
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content class="white--text">
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app class='indigo darken-2' dark :clipped-left="clipped" scroll-off-screen>
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" href="#/"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-navigation-drawer>
  <v-footer :fixed="fixed"  class="grey lighten-2" app>
    <v-layout column align-center>
    <span class="text-xs-center">&copy; 2018</span>
    </v-layout>
  </v-footer>
</v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'dashboard',
        title: 'Home'
      }],
      miniVariant: true,
      title: 'AGMAPI'
    }
  },
  name: 'App'
}
</script>

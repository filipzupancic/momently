<template>
  <div class="container-fluid">
    <div class="row example-centered">

        <hr style="background-color: #000000; border-top: 1px; ">
      <div style="padding-left:10%; padding-right:10%;">
        <div class="col-md-12 example-title">
            <h2>Your memories</h2>
            <hr style="background-color: #d8ac87; border-top: 1px; padding:0.5px; width: 10%;">
        </div>
        <div style=" padding-bottom: 30px;">
          <HotelDatePicker @period-selected='inputUpdated' />
        </div>
        <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2" style="margin-top: 30px;">
            <ul v-if="results && results.length" class="timeline timeline-centered">
                <li v-for="(result) in results" :key="result" class="timeline-item">
                    <div class="timeline-info">
                        <span>{{ result.date }}</span>
                    </div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3 class="timeline-title">Event Title</h3>
                        <p>{{ result.content }}</p>
                    </div>
                </li>
            </ul>
            <ul class="timeline timeline-centered">
                <li class="timeline-item">
                    <div class="timeline-info">
                        <span>March 12, 2016</span>
                    </div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3 class="timeline-title">Event Title</h3>
                        <p>Nullam vel sem. Nullam vel sem. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. Donec vitae sapien ut libero venenatis faucibus. ullam dictum felis
                            eu pede mollis pretium. Pellentesque ut neque.</p>
                    </div>
                </li>
                <li class="timeline-item">
                    <div class="timeline-info">
                        <span>March 23, 2016</span>
                    </div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3 class="timeline-title">Event Title</h3>
                        <p>Nullam vel sem. Nullam vel sem. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. Donec vitae sapien ut libero venenatis faucibus. ullam dictum felis
                            eu pede mollis pretium. Pellentesque ut neque. </p>
                    </div>
                </li>
                <li class="timeline-item period">
                    <div class="timeline-info"></div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h2 class="timeline-title">April 2016</h2>
                    </div>
                </li>
                <li class="timeline-item">
                    <div class="timeline-info">
                        <span>April 02, 2016</span>
                    </div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3 class="timeline-title">Event Title</h3>
                        <p>Nullam vel sem. Nullam vel sem. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. Donec vitae sapien ut libero venenatis faucibus. ullam dictum felis
                            eu pede mollis pretium. Pellentesque ut neque. </p>
                    </div>
                </li>
                <li class="timeline-item">
                    <div class="timeline-info">
                        <span>April 28, 2016</span>
                    </div>
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <h3 class="timeline-title">Event Title</h3>
                        <p>Nullam vel sem. Nullam vel sem. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. Donec vitae sapien ut libero venenatis faucibus. ullam dictum felis
                            eu pede mollis pretium. Pellentesque ut neque. </p>
                    </div>
                </li>
            </ul>
        </div>
      </div>
    </div>
    <hr style="background-color: #d8ac87; border-top: 1px; padding:0.5px; width: 10%;">
    <div style=" padding-right:5%; padding-left:5px; padding-bottom:5%;">
      <h3>Conversation intensity chart</h3>
      <p style="padding-bottom: 20px;">Conversation intensity chart tells how many characters did you send in a specific period of time.</p>
    </div>
</div>
    
</template>

<script>
import './diary.css'
import axios from 'axios';
import HotelDatePicker from 'vue-hotel-datepicker'
import 'vue-hotel-datepicker/dist/vueHotelDatepicker.css';
<<<<<<< HEAD
=======
import Vue from 'vue'
import Bars from 'vuebars'


Vue.use(Bars)

>>>>>>> c26b453d87b1c4c81f77eece00be03a1b1b9065a

export default {
  name: 'Diary',
  props: {
    msg: String
  },
  components: {
    HotelDatePicker,
  },
  data() {
    return {
      results: [],
    }
  },
  beforeCreate () {
    axios.get('http://127.0.0.1:8000/events', {}, {
            headers: {
                'Content-Type' : 'form-data'
            }
        })
      .then(response => (this.results = response.data))

      console.log(this.results)
  },
<<<<<<< HEAD
  mounted() {
    
=======
  methods: {
    inputUpdated: (event, dateFrom, dateTo) => {
      console.log(event, dateFrom, dateTo);

      axios.get('http://127.0.0.1:8000/events',  
                {params: {
                  dateFrom: dateFrom.toISOString().split('T')[0],
                  dateTo: dateTo.toISOString().split('T')[0]
                }}, {
                  headers: {
                      'Content-Type' : 'form-data'
                  }
              })
      .then(response => (this.results = response.data))

    }


>>>>>>> c26b453d87b1c4c81f77eece00be03a1b1b9065a
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app > div > div > div > div:nth-child(2) > div > div.vhd__datepicker__clear-button > img {
  display:none;
}
</style>

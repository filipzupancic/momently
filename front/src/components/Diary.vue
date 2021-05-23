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
        </div>
      </div>
    </div>
    <hr style="background-color: #d8ac87; border-top: 1px; padding:0.5px; width: 10%;">
    <div style="content-align: center; padding-bottom:5%;">
      <h3>Conversation intensity chart</h3>
      <p style="padding-bottom: 20px;">Conversation intensity chart tells how many characters did you send in a specific period of time.</p>
      <AreaChart/>
    </div>
</div>
    
</template>

<script>
import './diary.css'
import axios from 'axios';
import HotelDatePicker from 'vue-hotel-datepicker'
import 'vue-hotel-datepicker/dist/vueHotelDatepicker.css';
import AreaChart from "./AreaChart.vue";

export default {
  name: 'Diary',
  components: {
    HotelDatePicker,
    AreaChart,
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
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app > div > div > div > div:nth-child(2) > div > div.vhd__datepicker__clear-button > img {
  display:none;
}
</style>

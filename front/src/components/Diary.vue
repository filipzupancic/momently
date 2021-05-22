<template>
  <div class="container-fluid">
    <div class="row example-centered">
        <div class="col-md-12 example-title">
            <h2>Your memories</h2>
            <ul v-if="info && info.length" class="list-group">
                <li v-for="(info) in plants" :key="(info)">
                    <p>{{ plant }}</p>
                </li>
            </ul>
            <p></p>
        </div>
        <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2">
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
    
</template>

<script>
import './diary.css'
import axios from 'axios';


export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      info: null,
    }
  },
  beforeCreate () {
    axios.get('http://127.0.0.1:8000/events', {}, {
            headers: {
                'Content-Type' : 'form-data'
            }
        })
      .then(response => (this.info = response))
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

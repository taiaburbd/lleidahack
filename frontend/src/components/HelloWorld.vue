<template>
    <div class="hero_area">
        <div class="hero-bg">
            <img src="images/hero-bg.jpg" alt="">
        </div>
        <!-- header section strats -->
        <header class="header_section">
            <div class="container">
                <nav class="navbar navbar-expand-lg custom_nav-container ">
                    <a class="navbar-brand" href="/">
                <span>
                  Eurecat Smart Garden
                </span>
              </a>
    
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class=""> </span>
              </button>
    
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav  ">
                            <li class="nav-item active">
                                <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#about"> About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#ourplants">Plant Info</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#why_section">Why we are</a>
                            </li>
    
                        </ul>
                    </div>
                </nav>
            </div>
        </header>
        <!-- end header section -->
        <!-- slider section -->
        <section class="slider_section ">
            <div id="customCarousel1" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="container ">
                            <div class="row">
                                <div class="col-md-7 col-lg-6 mx-auto ">
                                    <div class="detail-box">
                                        <h1>
                                            Make Your Garden Alive
                                        </h1>
                                        <p>
                                          Welcome to Eurecat Smart Garden, a digital space where plant care meets cutting-edge technology. Our platform harnesses the power of MQTT to gather real-time data from sensors embedded in your plants, providing a dynamic and insightful window into their well-being
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
    
                </div>
                <div class="container">
                    <ol class="carousel-indicators">
                        <li data-target="#customCarousel1" data-slide-to="0" class="active"></li>
                        <li data-target="#customCarousel1" data-slide-to="1"></li>
                        <li data-target="#customCarousel1" data-slide-to="2"></li>
                    </ol>
                </div>
            </div>
    
        </section>
        <!-- end slider section -->
    </div>
    
    <!-- plant section -->
    
    <section id="ourplants" class="plant_section layout_padding">
        <div class="container">
            <div class="heading_container heading_center">
                <h2>
                    Our <span>plants</span>
                </h2>
            </div>
            <div class="row">
                <div v-for="(index, item) in data" :key="index" class="col-sm-6 col-md-4 col-lg-3" @click="toggleDiv(index.thing_id)">
                    <div class="box d-flex flex-column align-items-center">
                      <div class="font-weight-bold">{{index.thing_id}}</div>
                        <div class="img-box">
                            <img :src="'images/p' + (item+1) + '.png'" alt="">
                        </div>
                        <div class="badge badge-success text px-4 py-3 mt-2 text-white">Show Summary</div>
                    </div>
                </div>
                <div v-if="isDivVisible" class="col-md-12 row my-3">
                    <div class="col-md-4 card p-4">
                        <p class="alert alert-success">Plant Summary: {{activePlant}}</p>
                        <table class="table table-sm">
                            <tr>
                                <th>item</th>
                                <th>value</th>
                            </tr>
                            <tr>
                                <td>airHumidity</td>
                                <td>{{ summary['airHumidity'] }}</td>
                            </tr>
                            <tr>
                                <td>humidity</td>
                                <td>{{ summary['humidity'] }}</td>
                            </tr>
                            <tr>
                                <td>light</td>
                                <td>{{ summary['light'] }}</td>
                            </tr>
                            <tr>
                                <td>temperature</td>
                                <td>{{ summary['temperature'] }}</td>
                            </tr>
    
                        </table>
    
                        <h6>{{ item }} <span class="badge bg-warning">{{ index}}</span></h6>
                        <button class="btn btn-primary" @click="plant_watering(activePlant)"> Start watering</button>
                        <button class="btn btn-info mt-2" @click="toggleDivDetails()">Show details</button>

                    </div>
                    <div class="mt-2" v-if="summary['prediction'] && summary['prediction'].need_watering==true">
                        <button class="btn btn-sm btn-danger">need_watering : {{ summary['prediction'].need_watering }}</button>
                        <div class="alert alert-danger" v-if="summary['prediction']">
                            <ul>
                              <li v-for="reason in summary['prediction'].reasons" v-bind:key="reason">
                                {{ reason }}
                              </li>
                            </ul>
                        </div>
                    </div>
                    <div v-if="summary['prediction'] && summary['prediction'].need_watering==false">
                        <span class="badge badge-info">need_watering : {{ summary['prediction'].need_watering }}</span>
                        <div class="alert alert-success" v-if="summary['prediction']">
                            {{ summary['prediction'].reasons }}
                        </div>
                    </div>
                    <div v-if="isDivVisibleDetails" class="col-md-6 card">
                        <p><strong> Plant Details: {{ activePlant }}</strong>
                            <table class="table table-sm table-striped">
                                <tr>
                                    <th>timestamp</th>
                                    <th>temperature</th>
                                    <th>humidity</th>
                                    <th>airHumidity</th>
                                    <th>light</th>
                                </tr>
                                <tr v-for="(index) in detail" :key="index">
                                    <td>{{ formatTimestamp(index.ts) }}</td>
                                    <td>{{ index.temperature }}</td>
                                    <td>{{ index.humidity }}</td>
                                    <td>{{ index.airHumidity }}</td>
                                    <td>{{ index.light }}</td>
                                </tr>
                            </table>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- end plant section -->
    
    <!-- about section -->
    
    <section id="about" class="about_section layout_padding-bottom">
        <div class="container  ">
            <div class="row">
                <div class="col-md-6 ">
                    <div class="img-box">
                        <img src="images/about-img.jpg" alt="">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="detail-box">
                        <div class="heading_container">
                            <h2>
                                About <span>Smart Garden</span>
                            </h2>
                        </div>
                        <p>
                          Welcome to Eurecat Smart Garden, a digital space where plant care meets cutting-edge technology. Our platform harnesses the power of MQTT to gather real-time data from sensors embedded in your plants, providing a dynamic and insightful window into their well-being. <br/><br/>Whether you are a seasoned gardener or a novice plant parent, Eurecat Smart Garden empowers you with the knowledge and tools to foster a thriving indoor garden. Embark on a journey of intelligent plant care with us. Your plants deserve the best, and we are here to ensure they thrive.
                        </p>
                        <!-- <a href="">
                  Read More
                </a> -->
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- end about section -->
    
    <!-- why section -->
    
    <section id="why_section" class="why_section layout_padding">
        <div class="container">
            <div class="heading_container heading_center">
                <h2>
                    Why Choose <span>Us</span>
                </h2>
            </div>
            <div class="row">
                <div class="col-md-6 mx-auto">
                    <div class="box">
                        <div class="img-box">
                            <img src="images/w1.png" alt="">
                        </div>
                        <div class="detail-box">
                            <h5>
                                Realtime Monitoring
                            </h5>
                            <p>
                              Our platform constantly collects data from sensors within your plants, ensuring you stay connected to their vital signs
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 mx-auto">
                    <div class="box">
                        <div class="img-box">
                            <img src="images/w2.png" alt="">
                        </div>
                        <div class="detail-box">
                            <h5>
                                AI Power Predictions
                            </h5>
                            <p>
                              Leveraging artificial intelligence, we analyze the collected data to predict whether your plants need watering
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 mx-auto">
                    <div class="box">
                        <div class="img-box">
                            <img src="images/w3.png" alt="">
                        </div>
                        <div class="detail-box">
                            <h5>
                                Precision Plant Care
                            </h5>
                            <p>
                              Move beyond traditional care routines, and automate your watering system
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- end why section -->
    

    <!-- footer section -->
    <footer class="footer_section">
        <div class="container">
            <a href="" class="footer-brand">
            Eurecat Smart Garden 
          </a>
    
        </div>
        <div class="footer-info">
            <div class="container">
                <p>
                    &copy; <span id="displayYear"></span> All Rights Reserved to myself
                </p>
            </div>
        </div>
    </footer>
</template>

<script>
import axios from 'axios';

export default {
    name: 'HelloWorld',
    props: {
        msg: String
    },
    data() {
        return {
            data: null,
            plantDetails: '',
            isDivVisible: false,
            isDivVisibleDetails: false,
            activePlant: false,
            summary: {},
            detail: {},
        };
    },
    created() {
        this.fetchData();
    },
    methods: {
        formatTimestamp(timestamp) {
            const date = new Date(timestamp);
            const year = date.getFullYear();
            const month = (date.getMonth() + 1).toString().padStart(2, '0');
            const day = date.getDate().toString().padStart(2, '0');
            const hours = date.getHours().toString().padStart(2, '0');
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const seconds = date.getSeconds().toString().padStart(2, '0');

            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },
        toggleDiv(plant) {

            axios.get('http://127.0.0.1:5000/plant/' + plant + '/summary')
                .then(response => {
                    // Handle the successful response
                    this.summary = response.data;
                    this.activePlant = plant;
                })
                .catch(error => {
                    // Handle the error
                    console.error('Error fetching data:', error.message);
                });
            this.isDivVisible = !this.isDivVisible;
        },
        toggleDivDetails() {
            axios.get('http://127.0.0.1:5000/plant/' + this.activePlant + '/detail?limit=10')
                .then(response => {
                    // Handle the successful response
                    this.detail = response.data;
                    console.log(response.data);
                })
                .catch(error => {
                    // Handle the error
                    console.error('Error fetching data:', error.message);
                });
            this.isDivVisibleDetails = !this.isDivVisibleDetails;
        },
        plant_watering(plant_id) {
            axios.get('http://127.0.0.1:5000/plant/' + plant_id + '/watering')
                .then(response => {
                    // Handle the successful response
                    this.data = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    // Handle errors
                    console.error('Error fetching data:', error);
                });
        },
        fetchData() {
            axios.get('http://127.0.0.1:5000/plants')
                .then(response => {
                    // Handle the successful response
                    this.data = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    // Handle errors
                    console.error('Error fetching data:', error);
                });
        },
    },
};
</script>
